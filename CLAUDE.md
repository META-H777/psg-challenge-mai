# PSG Challenge Mai 2026 — Handoff complet

> **Pour Claude Code** : ouvrir un nouvel onglet dans `~/PSG-Challenge-Mai-2026/` puis taper "lis le CLAUDE.md".
> Tu as ici tout ce qu'il faut pour reprendre le projet sans poser de questions.

---

## 1. Mission

Challenge commercial interne **Linkeo Clermont-Ferrand** sur le mois de mai 2026, mis en scène façon **PSG vs Arsenal** avec un cockpit live partageable. Le but : motiver les commerciaux à dépasser leurs objectifs (RDV, marge brute, fiches CRM, ventes) via la gamification.

- **Durée** : 1er — 31 mai 2026 (projet temporaire, jeté après)
- **Cible** : 8 commerciaux + 1 arbitre + 1 directeur commercial France qui suit
- **Récompense** : la meilleure des deux équipes gagne une surprise

---

## 2. Casting

### Équipe PSG (l'équipe de Romain)
| ID | Nom | Position | Rôle | KPIs perso |
|---|---|---|---|---|
| `romain` | **Romain Patry** (toi) | TEC · Capitaine | Technico-commercial | Renouv /100% · Parrainage /2 · VA /4 |
| `enzo` | Enzo Fereyrolles | ST | Commercial | RDV /20 · Marge /30K€ · CRM /600 · Ventes /4 |
| `alex` | Alex Karaguinsky | MID | Commercial | idem |
| `adrien` | Adrien Dussap | DEF | Commercial | idem |

### Équipe ARSENAL (l'équipe rivale)
| ID | Nom | Position | Rôle | KPIs |
|---|---|---|---|---|
| `geff` | **Samuel Geffry** | TEC · Capitaine | Technico (KPIs comme Romain) | Renouv /100% · Parrainage /2 · VA /4 |
| `lauriane` | Lauriane Didier | COM | Commerciale | RDV /20 · Marge /30K€ · CRM /600 · Ventes /4 |
| `mamadou` | Mamadou Sacko | COM | Commercial | idem |
| `maxime` | Maxime Gauthier | COM | Commercial | idem |

### Arbitre (neutre)
| ID | Nom | Rôle |
|---|---|---|
| `souppaya` | **Samuel Souppaya** | Responsable d'agence Linkeo — arbitre du match, tient la coupe |

Les photos sont des **portraits IA full-body générés via Banana (Gemini Nano Banana 2)** à partir des vraies têtes scrappées de https://www.linkeo-clermont-ferrand.com/notre-equipe.php → tunnel/stade Champions League en fond.

---

## 3. URLs critiques

| Quoi | URL |
|---|---|
| **Cockpit live (public)** | https://meta-h777.github.io/psg-challenge-mai/ |
| **API live (backend)** | https://178-104-250-119.sslip.io/api/state |
| **Healthcheck API** | https://178-104-250-119.sslip.io/healthz |
| **Repo GitHub (public)** | https://github.com/META-H777/psg-challenge-mai |
| **Dev local** | http://127.0.0.1:8088/?demo (python -m http.server) |
| **Source équipe Linkeo** | https://www.linkeo-clermont-ferrand.com/notre-equipe.php |

Mode démo (sans auth) activé par défaut. Le mode prod (`?prod=1`) déclencherait Firebase Auth, mais Firebase n'est **pas configuré** — on reste en mode démo pour les 3 semaines.

---

## 4. Architecture

```
┌──────────────────────────────────────────────────────────────┐
│  8 commerciaux + directeur commercial sur leur device       │
└──────────┬────────────┬───────────┬──────────────┬──────────┘
           │            │           │              │
           └────────────┴───────────┴──────────────┘
                            │
            GitHub Pages : meta-h777.github.io/psg-challenge-mai
            (Alpine.js + Tailwind CDN + ~75 KB HTML statique)
                            │
                            ↓ fetch HTTPS
                            │
         178-104-250-119.sslip.io  (Caddy v2.11.2 reverse proxy)
                            │
                            ↓ localhost:8089
                            │
                  Flask 3.1 + flask-cors
                            │
                            ↓
                /var/lib/psg-api/state.json
                (écriture atomique via fcntl.flock)
                            │
                          VPS Hetzner Ubuntu 24.04
                          (déjà payé, partagé avec Hermes Agent)
```

### Front
- `index.html` (un seul fichier, ~1800 lignes) — Alpine.js + Tailwind CDN + assets locaux
- `service-worker.js` — **kill switch** : se désinstalle tout seul + purge les caches obsolètes (un ancien SW v1 cache-first avait causé des problèmes, plus jamais ça)
- `manifest.json` — PWA basique
- `assets/img/players/` — 9 portraits full-body (5 PSG + 4 Arsenal) + arbitre + trophée UCL
- `assets/img/raw/` — photos d'origine scrappées Linkeo (sources des portraits IA)

### Back
- `/etc/systemd/system/psg-api.service` — autostart
- `/etc/caddy/Caddyfile` — `178-104-250-119.sslip.io { reverse_proxy localhost:8089 }`
- `/root/psg-api/app.py` — Flask app (90 lignes, atomic writes, CORS strict, whitelist clés)
- `/var/lib/psg-api/state.json` — la seule source de vérité partagée
- UFW : ports 22/80/443 ouverts, reste fermé

### Modèle de données API
```json
{
  "_meta": { "version": 3, "updatedAt": 1778532469, "updatedBy": "Romain" },
  "players": {
    "romain": { "kpis": [{"key": "REN", "current": 110, "target": 100, "label": "..."}, ...] },
    "enzo":   { "kpis": [...] },
    "alex":   { "kpis": [...] },
    "adrien": { "kpis": [...] }
  },
  "teamArsenal": {
    "geff": {...}, "lauriane": {...}, "mamadou": {...}, "maxime": {...}
  },
  "plan": {
    "parrainages": [
      { "commercial": "Romain", "type": "Top clients", "entreprises": ["", ...] }, ...
    ],
    "prospection": [{ "name": "Couvreur" }, ...]
  }
}
```

### Cycle de synchronisation
1. **À l'ouverture** : `loadFromLocalStorage()` (instant) → `syncFromShared()` (GET API, merge)
2. **Polling** : `setInterval(syncFromShared, 4000)` — récupère les modifs des autres
3. **À chaque saisie + bouton Sauvegarder** : `scheduleSharedPush()` (debounced 800ms) → POST API
4. **Indicateur header** : `🟢 SYNC LIVE` si version API > 0, sinon `⚪ OFFLINE`
5. **Failover** : si API down, localStorage prend le relais, badge passe gris

---

## 5. Onglets de la page

### Match (home)
Layout VS one-page (viewport-fit, no-scroll desktop). Sur mobile : grille verticale `psg → arbitre → arsenal`.
- Topbar : live dot + jour `J X/30` + score différentiel
- Colonne PSG : 4 mini-tiles photos + nom + %
- Colonne centre : photo full-body de Samuel arbitre + halo doré pulsé + "VS" italique serif
- Colonne Arsenal : 4 mini-tiles (palette rouge)
- Bandeau bas : 4 cards KPI équipe en typo mono `JetBrains Mono`

### Score (anciennement Mes Stats)
- 4 cartes FUT PSG éditables (KPIs inputs, bouton "Sauvegarder")
- 4 cartes FUT Arsenal éditables en dessous (palette rouge, bouton rouge)
- Persistence : localStorage + API live partagée

### Plan d'action
- **Module Parrainages** : 4 cards (Romain/Alex/Adrien : Top clients · Enzo : Top références), 5 inputs chacun. Adrien préremplis (Centre Chape, Sopreco, Plombiers Issoiriens, Comi Déboucheurs, Florest Couverture).
- **Module Activités à haut potentiel** : tags simples (juste un nom d'activité). Préremplis : Couvreur, Paysagiste, Plombier-chauffagiste, Travaux publics, Dératisation. Bouton "+ Ajouter une activité" pour qu'un commercial étoffe la liste collective.

---

## 6. Design system

Inspiré du **Tech-OS Cockpit Linkeo** (~/OS-Central/tech-os/cockpit/) avec adaptation gold/navy pour le thème PSG.

- **Palette** : ultra-dark `#050509 → #0A0A12` + accent unique doré `#FFC43D / #FFE57F`. Pour Arsenal : rouge `#DA291C → #F87171`.
- **Typo** : Inter (sans), JetBrains Mono (KPIs tabular-nums), Instrument Serif italique (1 mot d'accent par titre)
- **Signatures** :
  - Aurora ambient animée 28s
  - Star drift 80s parallax
  - Grain SVG turbulence fixe
  - Hero gold radial glow + grille 56×56
  - Magnetic spotlight sur cards (suit la souris)
  - Live dot pulsé doré
  - Fleur de lys SVG héraldique réutilisable via `<use href="#fleur-de-lys"/>` (sprite défini en tête de body)
  - Trophée Champions League : image générée Banana (525 KB) qui tourne 22s slow motion en 3D (front + back miroir), float vertical 6s, glare doré 5.2s, s'élève selon le % team

---

## 7. État actuel (snapshot 2026-05-09)

| Joueur | % objectif | Détail |
|---|---|---|
| 🟦 Romain (CAP) | 50% | Renouv 110/100% · Parrainage 1/2 · VA 0/4 |
| 🟦 Enzo | 0% | tout à 0 |
| 🟦 Alex | 1% | RDV 1/20 |
| 🟦 Adrien | 1% | RDV 1/20 |
| 🟥 Samuel G. (CAP) | 5% | Renouv 16/100 |
| 🟥 Lauriane | 10% | MB 11 693€ /30K |
| 🟥 Mamadou | 17% | MB 19 262€ /30K · RDV 1/20 |
| 🟥 Maxime | 0% | tout à 0 |
| **Match** | **PSG 13% vs Arsenal 8% · +5 pts PSG** | |

---

## 8. Commandes utiles

### Dev local
```bash
cd ~/PSG-Challenge-Mai-2026
python3 -m http.server 8088 --bind 127.0.0.1
# → http://127.0.0.1:8088/?demo
```

### Push une nouvelle version
```bash
cd ~/PSG-Challenge-Mai-2026
git add . && git commit -m "..." && git push
# GitHub Pages rebuild ~30 sec
```

### SSH VPS Hermes/PSG
```bash
ssh -i ~/.ssh/os-central root@178.104.250.119
# alias possible : ssh hetzner (configuré dans settings.json claude code)
```

### Logs / restart API
```bash
ssh hetzner "journalctl -u psg-api -n 50 --no-pager"
ssh hetzner "systemctl restart psg-api"
ssh hetzner "systemctl status psg-api caddy"
```

### Modifier l'état directement via API
```bash
# Lire
curl -s https://178-104-250-119.sslip.io/api/state | python3 -m json.tool

# Écrire (merge profond, whitelist clés top-level : players, teamArsenal, plan)
curl -s -X POST -H "Content-Type: application/json" https://178-104-250-119.sslip.io/api/state \
  -d '{"players":{"romain":{"kpis":[{"key":"REN","current":120}]}},"_by":"reset-manuel"}'

# Reset complet
ssh hetzner "rm -f /var/lib/psg-api/state.json && systemctl restart psg-api"
```

### Régénérer un portrait via Banana
```bash
export GOOGLE_AI_API_KEY=$(python3 -c "import json; print(json.load(open('/Users/Romain/.claude/settings.json'))['mcpServers']['nanobanana-mcp']['env']['GOOGLE_AI_API_KEY'])")
python3 ~/.claude/skills/banana/scripts/edit.py \
  --image ~/PSG-Challenge-Mai-2026/assets/img/raw/<NAME>.png \
  --prompt "Full body portrait head to toe ..."
# → sortie dans ~/Documents/nanobanana_generated/banana_edit_YYYYMMDD_HHMMSS_xxx.png
```

---

## 9. Sécurité / confidentialité

- Repo `META-H777/psg-challenge-mai` est **public** mais ne contient **aucun secret** (clés API en `REPLACE_ME`, emails en `PLACEHOLDER`, pas de tokens)
- API live **sans auth** : tes 8 collègues qui ont le lien peuvent écrire. Acceptable pour MVP sur 3 semaines. Si fuite externe, on perd au pire des KPIs commerciaux dont le contexte est jeté le 1er juin.
- CORS strict : seuls `meta-h777.github.io` et `localhost:8088` peuvent appeler l'API
- Whitelist clés top-level dans le POST : seuls `players`, `teamArsenal`, `plan` peuvent être modifiés
- UFW : VPS exposé uniquement sur 22/80/443
- HTTPS auto Let's Encrypt via Caddy + sslip.io (renouvellement automatique)
- Le repo privé `OS-Central` reste isolé, aucun lien depuis ce repo

---

## 10. Pistes d'amélioration (post-1er juin ou si rouge urgent)

### Idées partagées par Romain mais pas implémentées (à activer si les KPIs stagnent)
1. **Battle Telegram bot** : ping canal équipe à chaque saisie (`⚡ Enzo +1 RDV → PSG passe devant`)
2. **MVP du jour** : badge tournant sur le commercial avec le plus gros gain 24h
3. **Streak Duolingo** : compteur jours consécutifs avec ≥1 RDV
4. **Coaching IA contextuel** : Hermes génère 1 phrase par KPI faible (`Adrien, 12 jours restants, cible 2 RDV/jour, voici 5 boîtes à appeler`)
5. **Cagnotte parrainage entre commerciaux** : si Enzo file un lead à Adrien et ça close, +500€ pour Enzo
6. **Replay vidéo de victoire** : générer un clip Hedra/Sora quand un commercial atteint 30K€

### Prospection automatisée IA (en attente de feu vert de Romain)
- **Option C "go" (recommandée)** : cron Hermes lundi 7h → appelle `recherche-entreprises.api.gouv.fr` → analyse Claude Sonnet 4.6 → envoie top 30 leads classés sur Telegram
- **Option B** : module dans le cockpit, formulaire secteur+ville → 50 leads ressortent en 20 sec
- **Option A** : CLI `hermes chat -q "..."` one-shot

### Backend solide post-MVP
Si on prolonge le projet au-delà du 1er juin, migrer vers **Firebase Firestore** (déjà câblé dans le code, juste à activer + filer config) → real-time WebSocket vrai, plus de polling, + auth Google whitelist. Le code Firestore est déjà import dans le HTML, dormant.

---

## 11. Historique des décisions

- **2026-05-07** : init projet, design FUT FIFA cards
- **2026-05-08** : refonte minimaliste (2 onglets), trophée 3D rotatif, 4 cartes FUT
- **2026-05-08** : étude marché Tech-OS, refonte hero design (dark + mono + serif italique)
- **2026-05-08** : ajout équipe Arsenal complète (4 joueurs + Samuel arbitre central)
- **2026-05-08** : push GitHub Pages public, déploiement initial
- **2026-05-08** : kill switch service worker (purge anciens caches v1 cache-first)
- **2026-05-09 matin** : ajout 3 modules Plan d'action + simplification prospection en tags
- **2026-05-09 midi** : déploiement infra live partagée (VPS Hetzner + Caddy + Flask + sslip.io)
- **2026-05-09 après-midi** : restauration manuelle des KPIs perdus en localStorage avant le wiring live

---

## 12. Contraintes à respecter dans toute évolution

- **Pas de paiement** : projet temporaire, donc pas de billing tier (Firebase Pro, Vercel Pro, etc.)
- **Auto-deploy** : changements pushés sur main = GitHub Pages rebuild auto. Pas de pipeline custom.
- **Mobile-first** : 80% des collègues consultent depuis iPhone Telegram → la page DOIT marcher fluidement en portrait 375×812
- **Pas d'exfiltration** : KPIs commerciaux + noms clients = data interne Linkeo. Pas de service tier non autorisé.
- **Robustesse** : si l'API tombe, le cockpit doit continuer en mode dégradé (localStorage seul, badge gris OFFLINE)

---

## 13. Tâches qu'un nouvel onglet Claude Code peut prendre

- Modifier un KPI ou une cible (chercher dans `players:` ou `teamArsenal:` dans `index.html`)
- Ajouter une carte, un onglet, un module
- Régénérer une photo (Banana CLI)
- Pousser de la data manuelle via curl
- Reset l'état partagé (ssh)
- Lire les logs si quelque chose foire
- Implémenter une des pistes d'amélioration en §10

**Premier réflexe d'un nouvel onglet** : `git status` puis `git log --oneline -5` pour voir l'état, puis lire les dernières lignes d'`index.html` (la zone `<script>` Alpine state) pour comprendre la structure de données actuelle.

---

*Document maintenu manuellement, dernière mise à jour : 2026-05-09. Source de vérité = ce fichier + le code dans `index.html`.*

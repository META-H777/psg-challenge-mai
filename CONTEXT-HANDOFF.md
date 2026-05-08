# 🎯 PSG Challenge Mai 2026 — CONTEXT HANDOFF

**Date :** 8 mai 2026 (nuit du 7-8)
**Status :** MVP complet, prêt à déployer vendredi matin
**À lire en premier dans toute future session**

---

## 📁 Localisation

`/Users/Romain/PSG-Challenge-Mai-2026/` — **DOSSIER ISOLÉ d'OS-Central**

→ Confidentialité absolue : aucun lien avec espace privé Romain. Pas dans OS-Central git.

---

## 🎯 CONTEXTE MÉTIER (à ne pas oublier)

**Capitaine PSG :** Romain Patry (Technico-commercial Linkeo Clermont)
**Coéquipiers PSG :**
- Enzo FEREYROLLES — Commercial (Striker)
- Alex KARAGUINSKY — Commercial (Midfielder)
- Adrien DUSSAP — Commercial (Defender)

**Capitaine ARSENAL adverse :** Samuel GEFFRY (dit "Geff") — Technico-commercial

**Période :** 1-31 mai 2026
**Lancement officiel équipe :** Lundi 12 mai 9h
**Confidentialité :** ne pas en parler à l'équipe ARSENAL

### KPIs entreprise (objectifs)

| KPI | Par commercial | Total équipe (3 commerciaux) |
|---|---|---|
| Actions CRM | 600 | 1800 |
| RDV | 20 | 60 |
| Ventes | 4 | 12 |
| **Marge brute** | **30 000 €** | **90 000 €** |
| Ventes parrainage (Romain technico) | — | 2 |
| VA (Romain technico) | — | 4 |
| % client minimum | 100% | 100% |

### Données business critiques

- **Conversion RDV→vente :** 10-20% (médiane ~15%)
- **Marge moyenne par vente :** 4-20K€ (médiane ~7-10K€)
- **Produits Linkeo :** Site web · SEO · SEA · Photos & vidéo
- **Cible :** artisans Clermont-Ferrand (BTP/Resto/Beauté/Auto/Services)

---

## 📦 CE QUI EST PRÊT (état au 8 mai 02h)

### Code (16 fichiers + 5 portraits IA)

```
PSG-Challenge-Mai-2026/
├── index.html              # Cockpit single-page Alpine + Firebase + Tailwind
├── README.md               # Setup vendredi
├── RESUME-VENDREDI.md      # Plan du jour
├── CONTEXT-HANDOFF.md      # CE FICHIER
├── manifest.json           # PWA installable
├── service-worker.js       # Offline cache
├── firebase.json           # Config deploy
├── firestore.rules         # Sécurité 4 emails whitelist + capitaine permissions
├── docs/ (9 documents stratégiques)
│   ├── pitch-monday-morning.md       # Speech 5-7 min lundi 12
│   ├── plan-action-4-semaines.md     # Stratégie hebdo + crisis plan
│   ├── math-challenge.md             # Calculs leviers + scénarios
│   ├── scripts-appel-artisans.md     # 7 scripts (cold call → closing → référé)
│   ├── traitement-objections.md      # Top 10 objections + réponses
│   ├── strategie-parrainage.md       # Activation 50 clients existants
│   ├── templates-comm.md             # 7 SMS + 7 emails
│   ├── pricing-packs.md              # 3 packs upsell (STARTER → ACCÉLÉRATEUR)
│   └── prospects-clermont.md         # Sourcing API gov + workflow
├── data/seed-data.json     # Données initiales Firestore
├── assets/img/raw/         # 5 photos originales Linkeo
│   ├── romain.png
│   ├── enzo.png
│   ├── alex.png
│   ├── adrien.png
│   └── geff.png
├── assets/img/players/     # 5 portraits PSG/ARSENAL générés via Banana
│   ├── romain-psg.png      # Capitaine PSG, brassard CAPITAIN doré, fleurs de lys
│   ├── enzo-psg.png        # Striker PSG, ballon, particules dorées
│   ├── alex-psg.png        # Midfielder PSG, écusson Paris-Saint-Germain
│   ├── adrien-psg.png      # Defender PSG #5, spotlight stadium
│   └── geff-arsenal.png    # Capitaine ARSENAL, brassard rouge/blanc, écusson canon
└── scripts/
    └── generate-psg-portraits.py  # Script génération portraits via Banana edit
```

---

## 🎨 DESIGN COCKPIT (état actuel)

### Thème "Club de foot pro PSG"

- **Background :** noir profond avec fleur-de-lys SVG pattern + radial navy gradient
- **Couleurs primaires :** noir #000 + navy #001E3C + gold royal #FFC43D
- **Accent :** cyan-gold #00E5FF pour stats critiques
- **Accent club red :** #DA291C (pour ARSENAL/warnings uniquement)
- **Typo :**
  - Display: Bebas Neue (sports/impact)
  - Body: Inter
  - Cinzel (royal/medieval) pour labels uppercase tracking-widest

### Sections (6 onglets)

| Tab | Status | Contenu |
|---|---|---|
| ⚽ Match | ✅ | Battle banner XL avec photos capitaines (Romain vs Geff) + KPIs équipe + Burndown chart |
| 🏆 Joueurs | ✅ | **FUT cards FIFA-style** — rating + position (TEC/ST/MID/DEF) + photo XL + stats overlay (CRM/RDV/VEN/MAR) + barre marge brute par commercial avec traînée dorée + total équipe |
| 🎯 Pipeline | ✅ | Kanban 6 colonnes (Lead→Won) + filtre par joueur + bouton + Nouveau lead |
| ⚔️ Arsenal | ✅ | 8 ressources liées aux docs/*.md |
| 📅 Daily | ✅ | Form check-in + check-ins équipe (capitaine only) |
| 🎖️ Stratégie | ✅ | Plan 4 semaines + math + notes 1-1 (capitaine only) |

### FUT cards — features

- Rating gros (88, 85, 84, 83) en haut-gauche avec gradient gold
- Position FIFA (TEC/ST/MID/DEF) dessous
- Photo joueur 44 hauteur (h-44 sm:h-52)
- Border gold-500/20 par défaut, captain border doré + animation pulseGold
- Stats grid 2 colonnes (clé Cinzel cyan / valeur Bebas gold)
- Marge brute en barre **avec traînée dorée et glow** uniquement pour commerciaux (key MAR)
- Total équipe marge brute en bas (90K€ cumulés)

---

## 🚀 SETUP VENDREDI MATIN — 30 min

### 1. Création comptes (5 min — Romain)

- Gmail dédié : `psg.challenge.mai@gmail.com` (ou similaire)
- Project Firebase : `psg-challenge-mai-2026` (region eur3)
- Repo GitHub privé : `META-H777/PSG-Challenge-Mai-2026`

### 2. Configuration code (5 min — Romain ou Claude Code)

Dans `index.html` ligne ~67-85, remplacer :

```js
const firebaseConfig = {
  apiKey: 'REPLACE_ME',
  // ... copier depuis Firebase console
};

const PSG_TEAM_EMAILS = [
  'romain.PLACEHOLDER@gmail.com',  // remplacer
  'enzo.PLACEHOLDER@gmail.com',
  'alex.PLACEHOLDER@gmail.com',
  'adrien.PLACEHOLDER@gmail.com',
];
```

Idem dans `firestore.rules` (lignes 13-19).

### 3. Init git + push (2 min)

```bash
cd /Users/Romain/PSG-Challenge-Mai-2026
git init
git add -A
git commit -m "init: PSG Challenge Mai 2026 cockpit"
gh repo create META-H777/PSG-Challenge-Mai-2026 --private --source=. --push
```

### 4. Deploy Firebase rules (3 min)

```bash
npm install -g firebase-tools  # si pas déjà fait
firebase login
firebase use psg-challenge-mai-2026
firebase deploy --only firestore:rules
```

### 5. Activer GitHub Pages (3 min)

Repo settings → Pages → Source = `main`/root → URL générée :
**https://meta-h777.github.io/PSG-Challenge-Mai-2026/**

### 6. Test auth + 4 utilisateurs (10 min)

Tester avec ton email → ajouter Enzo, Alex, Adrien aux invités → tester leur connexion.

### 7. Seed initial data (2 min)

Console Firestore → manuellement créer collection `players` avec les 4 joueurs (référence : `data/seed-data.json`).

---

## 📅 PLAN WEEKEND CONFIRMÉ (8 mai férié + 10 mai dim)

### VENDREDI 8 mai (férié)

| Tranche | Mission | Output |
|---|---|---|
| 9h-13h | **Hermes V2 upgrade** (cf. `~/OS-Central/infra/hermes-v2-migration/CHECKLIST-VENDREDI.md`) | Hermes autonome 24/7 |
| 13h-14h | Brief Hermes pour weekend | 3 missions de fond |
| 14h-19h | **Cockpit PSG deploy** (étapes ci-dessus) | URL live |
| 19h-21h | TWELVE V2 boost (Hedra + casser statique) | Premier clip lip-sync |

### SAMEDI 9 mai — OFF (Hermes bosse autonome)

### DIMANCHE 10 mai

| Tranche | Mission |
|---|---|
| 9h-13h | TWELVE V2 deep work + publication ép.1 |
| 14h-17h | Backlog TODO (Tech OS sécurité 19 mai + débrief trading) |
| 17h-19h | Cockpit PSG polish + prépa pitch lundi |
| 19h-20h | Bilan hebdo dominical |

### LUNDI 12 mai 9h00

**PITCH ÉQUIPE PSG** dans le bureau Linkeo. Speech dans `docs/pitch-monday-morning.md`. Cockpit live à l'écran. Daily 9h démarre dès mardi 13.

---

## 🔧 4 CHANTIERS WEEKEND (récap macro)

### 1. **Hermes V2** (vendredi 9h-13h)
- Migration Nous v0.10 → Hermes Agent v0.13
- Provider Anthropic Sonnet 4.6
- Skills : claude-code, cron, curator, web-search
- MCPs : filesystem, git, github
- Cron : daily digest 22h, bilan dim 9h, watch securité 19 mai
- 📁 Plan : `~/OS-Central/infra/hermes-v2-migration/`

### 2. **TWELVE V2** (vendredi soir + dimanche matin)
- Top 5 actions ROI : casser statique, Hedra lip-sync, Suno V5 score, Niji 7 + Spider-Verse LoRA, n8n auto-publish
- Score visé : 5.5/10 → 7.7/10 en 1 weekend
- Budget +35-50$/mois
- 📁 Brief : `~/OS-Central/contenu-os/twelve/V2-PRIORITES-MAI.md`

### 3. **Backlog TODO** (dimanche après-midi)
- Tech OS Cockpit Linkeo sécurité (deadline 19 mai!)
- Mentorat trading débrief liquidations avril
- 📁 Source : `~/OS-Central/MASTER.md` + `~/OS-Central/backlog.md`

### 4. **Challenge Mai PSG** (vendredi après-midi + lundi pitch)
- Cockpit deploy Firebase + GH Pages
- Pitch équipe lundi
- Daily check-in dès mardi
- 📁 Tout dans : `/Users/Romain/PSG-Challenge-Mai-2026/`

---

## 💡 POUR REPRENDRE EN PROCHAINE SESSION CLAUDE CODE

### Read first
1. `~/PSG-Challenge-Mai-2026/CONTEXT-HANDOFF.md` (ce fichier)
2. `~/PSG-Challenge-Mai-2026/RESUME-VENDREDI.md` (plan vendredi)
3. `~/OS-Central/infra/hermes-v2-migration/CHECKLIST-VENDREDI.md` (Hermes plan)
4. `~/OS-Central/contenu-os/twelve/V2-PRIORITES-MAI.md` (TWELVE plan)
5. `~/OS-Central/MASTER.md` (état global)

### Vérifier état cockpit
```bash
open /Users/Romain/PSG-Challenge-Mai-2026/index.html
```
→ Mode démo bypass auth (URL `file://` détecté). Voir tous les onglets.

### Vérifier état OS-Central
```bash
cd /Users/Romain/OS-Central
git log --oneline -10
git status -sb
```

### Vérifier portraits PSG
```bash
ls -lh /Users/Romain/PSG-Challenge-Mai-2026/assets/img/players/
```
5 fichiers : romain-psg.png, enzo-psg.png, alex-psg.png, adrien-psg.png, geff-arsenal.png

---

## 🎨 DESIGN CHANGES APPLIQUÉS (nuit 7-8 mai)

### Itération 1 (initiale)
- Cockpit single-page Alpine.js + Firebase
- Tailwind dark theme bleu/rouge
- 6 onglets (Battle/Dashboard/Pipeline/Arsenal/Daily/Strategy)

### Itération 2 (refonte PSG navy/gold)
- Background fleur-de-lys SVG pattern
- Palette navy + gold royal
- Photos capitaines dans battle banner
- Player cards FUT-style basique

### Itération 3 (correction Romain technico + FUT FIFA full)
- ⚙️ **Logique métier** : Romain = TECHNICO capitaine (ventes parrainage + VA), Enzo/Alex/Adrien = COMMERCIAUX (30K€ marge chacun)
- 🎨 **Plus de noir** (background pur #000 avec accents navy/gold)
- 💎 **Cyan-gold accent** (#00E5FF) pour les stats keys (CRM/RDV/VEN/MAR)
- 🃏 **FUT cards FIFA-style** : rating + position FIFA + photo XL + stats grid 2 colonnes + marge bar avec traînée dorée
- 📊 **Marge bar** style Cockpit Linkeo : barre 14px avec gradient cyan→gold, glow externe, shimmer animation, glow renforcé quand 95%+ atteint
- 📸 **Photos battle banner XL** (w-64 sm:h-80, gold border-image gradient, drop-shadow)
- 🏆 **Score 0/0 initial** (challenge n'a pas commencé)
- 🎯 **Total équipe marge brute** affiché en bas du dashboard (90K€ cumulés)

---

## 🔐 SÉCURITÉ / CONFIDENTIALITÉ

- ✅ Dossier hors OS-Central
- ✅ Repo GitHub privé (à créer vendredi)
- ✅ Firebase rules whitelist 4 emails
- ✅ Auth Google obligatoire
- ✅ Aucune référence dans MASTER.md ou autres docs OS-Central
- ✅ URL semi-secrète (non indexée Google)

---

## 💰 BUDGET MENSUEL TOTAL (pour info Romain)

| Item | Coût/mois |
|---|---|
| **Challenge Mai (Firebase free tier)** | **0€** |
| Hermes V2 (Anthropic API + Hetzner existant) | 40-70€ |
| TWELVE V2 (Hedra + Suno V5 + Blotato) | 35-50$ |
| **Total nouveau** | **~80-130€/mois** |

ROI : 1 vente Linkeo via cockpit = 4-20K€ marge → ROI 50-200x sur le mois.

---

## 📝 PROMPTS RÉUTILISABLES

### Régénérer un portrait PSG
```bash
python3 /Users/Romain/PSG-Challenge-Mai-2026/scripts/generate-psg-portraits.py
```
(modifier la liste PLAYERS dans le script si besoin)

### Source des photos originales (Linkeo team page)
```
https://www.linkeo-clermont-ferrand.com/notre-equipe.php
```
URLs photos individuelles dans `scripts/generate-psg-portraits.py` ou via curl + grep `data-src`.

---

## 🚨 ALERTES À NE PAS OUBLIER

1. **Tech OS sécurité Cockpit Linkeo** — deadline 19 mai (auth Google + Firestore rules) — déjà alerte rouge dans MASTER.md
2. **Mentorat trading débrief** — bloquant pour reprendre les trades après les 2 liquidations d'avril
3. **TWELVE publication ép.1** — déjà raté la deadline mardi 6 mai, recible cette semaine
4. **Hermes V2 upgrade** — multiplicateur sur tous les autres chantiers, prio 1 vendredi matin

---

*Préparé dans la nuit du 7-8 mai 2026 par Claude Code en mode auto.*
*Romain peut clean la conv en sécurité — toute l'info utile est ici.*

# 🌅 Bonjour vendredi 8 mai — Résumé prep nuit

**Préparé pour toi entre 00h15 et 02h30 cette nuit. Tout est prêt pour démarrer.**

---

## 📦 Ce qui est prêt dans ce dossier

```
PSG-Challenge-Mai-2026/
│
├── 🏗️ INFRASTRUCTURE
│   ├── index.html              # Cockpit single-page complet (Auth + Dashboard + Pipeline + Daily + Strategy)
│   ├── manifest.json           # PWA installable
│   ├── service-worker.js       # Mode hors ligne
│   ├── firebase.json           # Config deploy
│   └── firestore.rules         # Sécurité whitelist 4 emails
│
├── 📚 docs/ (9 documents)
│   ├── pitch-monday-morning.md       # Speech 5-7 min pour lundi 12 mai
│   ├── plan-action-4-semaines.md     # Stratégie semaine par semaine détaillée
│   ├── math-challenge.md             # Calculs leviers + scénarios
│   ├── scripts-appel-artisans.md     # 7 scripts d'appel prêts
│   ├── traitement-objections.md      # Top 10 objections + réponses
│   ├── strategie-parrainage.md       # Process activation 50 clients existants
│   ├── templates-comm.md             # 7 SMS + 7 emails templates
│   ├── pricing-packs.md              # 3 packs upsell + add-ons
│   └── prospects-clermont.md         # Sourcing artisans via APIs gov gratuites
│
├── 📊 data/
│   └── seed-data.json          # Données initiales (joueurs, KPIs, mottos)
│
└── README.md                   # Setup instructions step-by-step
```

**Total : ~12 000 mots de contenu stratégique + 1 cockpit fonctionnel.**

---

## 🚀 Plan vendredi 8 mai

### 9h-13h — HERMES V2 MIGRATION

→ Voir `~/OS-Central/infra/hermes-v2-migration/CHECKLIST-VENDREDI.md`

Heure par heure : backup → update → Anthropic config → skills → Curator (Postgres) → MCPs → cron → Telegram → tests.

**Output : Hermes V2 opérationnel autonome 24/7.**

### 14h-15h — Brief Hermes pour weekend

3 missions de fond pour qu'il bosse pendant que tu fais autre chose :
1. Recherche innovations IA anime mai 2026
2. Sourcing 200 prospects artisans Clermont via API gov
3. Analyse liquidations trading avril

### 14h-19h — CHALLENGE MAI COCKPIT

| 14h-14h15 | Crée Gmail dédié `psg.challenge.mai@gmail.com` |
| 14h15-14h30 | Project Firebase `psg-challenge-mai-2026` (eur3) |
| 14h30-14h45 | Repo GitHub privé `META-H777/PSG-Challenge-Mai-2026` |
| 14h45-15h00 | Remplace placeholders firebaseConfig + emails dans `index.html` et `firestore.rules` |
| 15h-16h | Deploy : `firebase init` + `firebase deploy --only firestore:rules` + GitHub Pages |
| 16h-16h30 | Test auth Google + 4 utilisateurs |
| 16h30-17h | Seed data initial dans Firestore (depuis seed-data.json) |
| 17h-19h | Polish UI + test mobile + screenshots PWA installable |

→ **17h** : URL live à partager lundi.

### 19h-21h — TWELVE V2 BOOST

→ Voir `~/OS-Central/contenu-os/twelve/V2-PRIORITES-MAI.md`

5 actions priorisées par ROI :
1. Casser le statique (regen 5 clips avec movement camera explicite) — 1h
2. Hedra Character-3 setup + 1 plan test lip-sync — 1h

(Suite dimanche)

---

## 🗓️ Samedi 9 mai — OFF

Hermes bosse autonome sur les 3 missions briefées. Tu te reposes.

---

## 🗓️ Dimanche 10 mai

### 9h-13h — TWELVE V2 deep work

3. Suno V5 music score
4. Niji 7 + Spider-Verse LoRA
- Re-render ép.1 v3 final
- **Publication ép.1 sur TikTok / YT / IG**

### 14h-17h — Backlog TODO

- Tech OS Cockpit Linkeo sécurité (deadline 19 mai!)
- Mentorat trading débrief liquidations avril

### 17h-19h — Challenge Mai polish

- Review cockpit après 24h
- Ajustements UI / data
- Préparation pitch lundi matin

### 19h-20h — Bilan hebdo dominical

- `/bilan-hebdo` skill (ou dans cockpit)
- État OS-Central propre

---

## 🎯 Lundi 12 mai 9h00

**PITCH ÉQUIPE PSG.**

Tu suis le speech dans `docs/pitch-monday-morning.md`. Tu montres le cockpit live. Tu envoies le lien dans le groupe WhatsApp privé. Daily 9h démarre dès mardi 13.

→ **CHALLENGE LANCÉ.**

---

## 💰 Récap budget mensuel

| Item | Coût/mois |
|---|---|
| Anthropic API (Hermes V2) | 30-60€ |
| Hetzner CPX21 (existant) | 9€ |
| Hedra Character-3 (TWELVE) | $15-30 |
| Suno V5 (TWELVE) | $10 |
| Blotato auto-publish (TWELVE) | $10 |
| Firebase (PSG Cockpit) | 0€ free tier |
| Tout le reste | 0€ open-source |
| **Total nouveau** | **~70-130€/mois** |

→ ROI :
- 1 vente Linkeo = 4-20K€ marge → cockpit qui sécurise 1 vente = ROI 50x sur le mois
- 1 ép TWELVE viral = audience nouvelle, monétisation à venir
- Hermes économisé 30-40h/sem de boulot répétitif

---

## 🔐 Sécurité & confidentialité

✅ PSG-Challenge-Mai-2026 = **dossier indépendant**, aucun lien avec OS-Central
✅ Repo GitHub PSG = **privé**, whitelist 4 emails
✅ Firebase = project isolé
✅ Aucune mention dans MASTER.md ou autres docs OS-Central

---

## ☕ Avant de te lancer

1. Bois ton café
2. Lis le pitch lundi matin (5 min) — c'est ton ancrage émotionnel
3. Active snapshot Hetzner (5 min) — sécurité Hermes
4. Ouvre les 2 checklists :
   - `~/OS-Central/infra/hermes-v2-migration/CHECKLIST-VENDREDI.md`
   - Ce fichier (`RESUME-VENDREDI.md`)
5. Lance.

---

**On gagne ce challenge, on publie TWELVE, on upgrade Hermes. Tout en 2 jours. Trace.**

🫡

---

*Préparé dans la nuit du 7 au 8 mai 2026 par Claude Code en mode auto.*

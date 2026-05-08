# 🏆 PSG Challenge Mai 2026

**Cockpit confidentiel équipe PSG — challenge mai 2026 vs ARSENAL.**

> ⚠️ Confidentiel. Ne jamais lier à un autre repo perso, ne jamais partager hors équipe PSG (Romain · Enzo · Alex · Adrien).

---

## 🚀 Setup vendredi 8 mai (15 min total)

### 1. Créer le project Firebase (5 min)

1. Aller sur https://console.firebase.google.com
2. **Add project** → nom : `psg-challenge-mai-2026`
3. Désactiver Analytics (pas besoin)
4. Une fois créé, dans Project Settings (icon engrenage) :
   - **Build → Authentication** → Get started → **Sign-in method** → **Google** → Enable + sélectionner support email perso → Save
   - **Build → Firestore Database** → Create database → mode production → région **eur3** (Belgique)
   - **Project settings → General → Your apps** → icon `</>` → register app `psg-cockpit` → copier l'objet `firebaseConfig`

### 2. Configurer le cockpit (3 min)

Dans `index.html`, ligne ~64, remplacer le bloc `firebaseConfig` par celui copié de Firebase.

Puis ligne ~78, remplacer `PSG_TEAM_EMAILS` par les vrais emails Gmail des 4 joueurs :

```js
const PSG_TEAM_EMAILS = [
  'romain.gmail@gmail.com',  // remplacer
  'enzo.gmail@gmail.com',
  'alex.gmail@gmail.com',
  'adrien.gmail@gmail.com',
];
```

### 3. Déployer Firestore rules (2 min)

```bash
# install Firebase CLI si pas déjà fait
npm install -g firebase-tools
firebase login
cd /Users/Romain/PSG-Challenge-Mai-2026
firebase init firestore  # accepter defaults, target project psg-challenge-mai-2026
firebase deploy --only firestore:rules
```

### 4. Créer repo GitHub privé (3 min)

```bash
cd /Users/Romain/PSG-Challenge-Mai-2026
git init
git add -A
git commit -m "init: PSG Challenge Mai 2026 cockpit"
gh repo create META-H777/PSG-Challenge-Mai-2026 --private --source=. --push
```

### 5. Activer GitHub Pages (2 min)

Sur GitHub → repo settings → Pages → Source : `main` branch / `/root`. URL générée :
**https://meta-h777.github.io/PSG-Challenge-Mai-2026/**

→ Tester l'auth Google avec ton email. Si ✅ on est en prod.

---

## 📁 Structure du projet

```
PSG-Challenge-Mai-2026/
├── index.html              # Cockpit single-page app
├── manifest.json           # PWA installable
├── service-worker.js       # PWA offline cache
├── firebase.json           # Firebase deploy config
├── firestore.rules         # Sécurité Firestore (4 emails whitelist)
├── README.md               # Ce fichier
├── docs/
│   ├── pitch-monday-morning.md          # Speech lundi matin équipe
│   ├── plan-action-4-semaines.md        # Stratégie semaine par semaine
│   ├── math-challenge.md                # Calculs et leviers
│   ├── scripts-appel-artisans.md        # Scripts d'appel intro/closing
│   ├── traitement-objections.md         # Top 10 objections + réponses
│   ├── strategie-parrainage.md          # Activation clients existants
│   ├── templates-comm.md                # SMS/Email templates
│   ├── pricing-packs.md                 # Pricing + packs upsell haute marge
│   └── prospects-clermont.md            # Comment qualifier prospects (API)
├── data/
│   └── seed-data.json      # Données initiales (joueurs, KPIs)
└── deploy/
    └── firestore.rules     # (copie de la racine pour CI)
```

---

## 🎯 KPIs équipe (objectifs entreprise mai)

| KPI | /joueur | Total équipe |
|---|---|---|
| Actions CRM | 600 | 2400 |
| RDV | 20 | 80 |
| Ventes gagnantes | 4 | 16 |
| Marge | 30K€ | 120K€ |
| Ventes parrainage (Adrien) | 2 | 2 |
| VA (Adrien) | 4 | 4 |
| % client minimum | 100% | — |

→ **Vraie cible PSG : 110% sur tous les KPIs pour assurer la victoire avec marge.**

---

## 🔐 Sécurité

- Repo **privé** GitHub
- Firestore rules **whitelist 4 emails**
- Auth **Google obligatoire**
- **Aucune donnée ne sort du cockpit** sans l'autorisation Romain
- Pas de lien ni référence avec aucun autre projet de Romain

---

## 📞 En cas de problème

Romain (capitaine). Voilà.

---

*Repo créé pour gagner ce challenge. ARSENAL n'a aucune chance.* 🔥

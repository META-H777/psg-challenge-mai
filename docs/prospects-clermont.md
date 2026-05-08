# 📋 Comment qualifier des prospects artisans à Clermont-Ferrand

**Sources légales et gratuites :** APIs gouvernementales françaises.

---

## 🎯 Stack de qualification (ordre d'utilisation)

### 1. **API Recherche d'Entreprises** (gov.fr) — backbone

**URL :** https://recherche-entreprises.api.gouv.fr/docs/

**Caractéristiques :**
- ✅ Gratuit
- ✅ **Pas de clé API** nécessaire
- ✅ 7 requêtes / seconde
- ✅ Couvre toutes les entreprises FR (mises à jour quotidiennes)
- ✅ Filtres : code NAF, code postal, département, dirigeants

**Exemple de requête (recherche artisans BTP à Clermont) :**

```bash
curl 'https://recherche-entreprises.api.gouv.fr/search?activite_principale=43.39A&code_postal=63000&page=1&per_page=20'
```

**Codes NAF utiles pour artisans Clermont :**

| Secteur | Codes NAF |
|---|---|
| Boulangerie | 10.71B, 10.71C, 10.71D |
| Restauration rapide | 56.10C |
| Coiffure | 96.02A |
| Garage / réparation auto | 45.20A, 45.20B |
| BTP — gros oeuvre | 41.20A, 41.20B |
| BTP — second oeuvre | 43.21A, 43.22A, 43.31Z, 43.32A, 43.33Z, 43.34Z, 43.39A |
| Plomberie/chauffage | 43.22A, 43.22B |
| Électricité | 43.21A, 43.21B |
| Maçonnerie | 43.99C |
| Peinture/revêtement | 43.34Z |
| Esthéticienne | 96.02B |
| Photographe | 74.20Z |
| Couverture | 43.91A, 43.91B |

---

### 2. **API Sirene v3** (INSEE) — backup + bulk

**URL :** https://portail-api.insee.fr/

**Caractéristiques :**
- ✅ Gratuit avec compte INSEE (création 5 min)
- ✅ Plus de filtres avancés
- ✅ Données fraîches (J-1 max)
- ⚠️ Rate limit raisonnable (compte gratuit)

**Cas d'usage :** quand `recherche-entreprises` ne donne pas assez de résultats ou pour des bulk extractions.

---

### 3. **API Pappers** — enrichissement juridique/financier

**URL :** https://www.pappers.fr/api/documentation

**Caractéristiques :**
- 💰 **100 credits gratuits/mois** sur email pro
- ✅ Agrège SIRENE + INPI + BODACC + RNE en un seul appel
- ✅ Données financières (CA, résultat net, effectif)
- ✅ Dirigeants, bénéficiaires effectifs
- ✅ Procédures collectives, événements RNE

**Cas d'usage :** **enrichir un prospect avant l'appel** pour personnaliser le pitch.

**Exemple de requête :**

```bash
curl 'https://api.pappers.fr/v2/entreprise?api_token=TON_TOKEN&siret=12345678900012'
```

→ Tu récupères : raison sociale, dirigeant, CA dernier exercice, effectif, statut juridique, etc.

**Pour 4 commerciaux × 100 credits = 400 enrichissements/mois gratuits = ~13/jour. Largement suffisant.**

---

## 🛠️ Workflow opérationnel (chaque commercial)

### Étape 1 — Sourcing brut (15 min/jour)

Sur la page Arsenal du cockpit, on aura un formulaire "Source prospects" qui appelle automatiquement `recherche-entreprises` avec :
- Code postal Clermont (63000, 63100, 63110, 63170, etc.)
- Code NAF de ton secteur cible

→ Sortie : liste de **20-30 entreprises** par requête.

### Étape 2 — Filtrage qualité (10 min/jour)

Critères de qualification :
- ✅ Active (pas en cessation)
- ✅ Effectif < 50 (notre cible)
- ✅ Pas trop ancienne (>2 ans = plus stable)
- ❌ Pas de procédure collective récente
- ❌ Pas déjà client Linkeo (vérifier dans CRM Linkeo)

### Étape 3 — Enrichissement (5 min par prospect)

Pour les **5-8 prospects les plus prometteurs**, appel API Pappers pour récupérer :
- Nom du dirigeant (pour personnaliser pitch)
- CA / effectif (pour adapter pricing)
- Site web existant ? (déjà site → script #2 "déloger concurrent")

### Étape 4 — Vérification visibilité Google (5 min par prospect)

Recherche Google manuelle :
- Tape "[nom entreprise] Clermont"
- Note position : page 1 / 2 / 3+
- Note présence Google Business Profile + nb d'avis
- Capture d'écran si page 3+ → **angle d'attaque pour le pitch**

### Étape 5 — Création carte prospect dans cockpit (2 min)

Bouton "+ Nouveau lead" dans le cockpit :
- Nom entreprise
- Dirigeant
- Téléphone (depuis recherche-entreprises ou Google)
- Secteur
- Marge estimée (basé sur effectif × pack potentiel)
- **Notes :** position Google + accroche pitch

→ Lead prêt à être contacté.

---

## 📊 Cible journalière par commercial

- **Sourcing :** 30-50 prospects bruts/jour
- **Qualifiés :** 10-15 entrent dans le pipeline
- **Contactés (cold call/SMS) :** 5-10 prospects/jour
- **RDV pris :** 1-2 RDV/jour

→ Sur 20 jours ouvrés × 4 commerciaux = ~80-160 RDV potentiels (large couverture cible 80).

---

## 🚫 Ce qu'il NE faut PAS faire

### ❌ Scraping Pages Jaunes

CGU PJ interdisent le scraping. La CNIL a déjà sanctionné PJ pour usage de données. Si on scrappait, on serait dans la zone grise → risque juridique et réputationnel pour Linkeo. **NON.**

### ❌ Achat de fichiers prospects

- RGPD : ces fichiers sont souvent collectés sans consentement explicite
- Qualité douteuse, conversions faibles
- Risque sanctions CNIL

### ❌ Scraping massif Google Maps

Tolérable en très faible volume (10-20 requêtes/jour) pour vérifier visibilité. Mais **pas pour collecter des données personnelles** (emails, téléphones via scraping). Resterons sur info publique des fiches GBP.

### ✅ OK : enrichissement Google Maps manuel

Si tu vas sur la fiche Google Business Profile d'un prospect public et tu notes le téléphone affiché publiquement → c'est légal. Mais à la main, pas en automatisé masse.

---

## 🎯 Actions concrètes vendredi 9 mai (post-Hermes upgrade)

**Hermes en autonomie peut faire pendant ton boulot Linkeo :**
- Requêter `recherche-entreprises` API pour les 10 codes NAF cibles à Clermont
- Sortir une liste enrichie de 200-300 prospects (50-75 par commercial)
- Format CSV ou injection directe Firestore (collection `prospects`)
- Tu as 200 prospects qualifiés au démarrage du challenge

**Coût Hermes :** quasi nul (API gratuite, queries simples).

**Time-saving :** 4 × 4h de sourcing manuel = 16h économisées équipe.

---

## 📚 Annexes — codes postaux Clermont-Ferrand & alentours

```
63000  Clermont-Ferrand centre
63100  Clermont-Ferrand
63110  Beaumont
63170  Aubière
63540  Romagnat
63400  Chamalières
63800  Cournon-d'Auvergne
63270  Vic-le-Comte
63500  Issoire
63300  Thiers
63200  Riom
63430  Pont-du-Château
63360  Gerzat
63190  Lezoux
```

→ Élargir progressivement le rayon si besoin (priorité Clermont métro, puis villes 30 min, puis Issoire/Thiers).

---

*Process à roder semaine 1, automatisable via Hermes pour les semaines suivantes.*

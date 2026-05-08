// PSG Challenge Mai 2026 — Service Worker (network-first pour éviter cache obsolète)
const CACHE_NAME = 'psg-cockpit-v3';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
];

self.addEventListener('install', (e) => {
  // Force le SW à activer immédiatement, sans attendre la fermeture des onglets
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE_NAME).then((c) => c.addAll(ASSETS)));
});

self.addEventListener('activate', (e) => {
  // Supprime tous les anciens caches et prend le contrôle des onglets ouverts
  e.waitUntil(
    Promise.all([
      caches.keys().then((keys) =>
        Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
      ),
      self.clients.claim(),
    ])
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  // Network-first pour HTML/JS/CSS (le code qui évolue)
  // Cache-first uniquement pour les images/fonts (qui ne changent quasi jamais)
  const url = new URL(req.url);
  const isStaticAsset = /\.(png|jpe?g|webp|gif|svg|woff2?|ttf|eot|ico)$/i.test(url.pathname);

  if (isStaticAsset) {
    // Cache-first pour assets binaires
    e.respondWith(
      caches.match(req).then((cached) => cached || fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(CACHE_NAME).then((c) => c.put(req, copy));
        return res;
      }))
    );
  } else {
    // Network-first pour HTML/JS/CSS et toutes les autres requêtes
    e.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((c) => c.put(req, copy));
          return res;
        })
        .catch(() => caches.match(req))
    );
  }
});

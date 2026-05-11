// PSG Challenge Mai — kill switch : ce SW se désinstalle tout seul et purge les caches.
// Tous les navigateurs ayant l'ancien SW v1 (cache-first) reçoivent ce fichier
// et nettoient automatiquement leur état. Plus aucune ancienne version servie.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.map((k) => caches.delete(k)));
    const regs = await self.registration ? [self.registration] : [];
    for (const r of regs) {
      try { await r.unregister(); } catch (_) {}
    }
    const clients = await self.clients.matchAll({ type: 'window' });
    for (const c of clients) c.navigate(c.url);
  })());
});
self.addEventListener('fetch', (e) => {
  // Network-only : on ne sert rien depuis le cache, on laisse le browser fetch normalement
  e.respondWith(fetch(e.request).catch(() => new Response('', { status: 504 })));
});

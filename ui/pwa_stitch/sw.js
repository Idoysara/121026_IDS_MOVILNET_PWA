// Service Worker - Movilnet Core PWA
const CACHE_NAME = 'movilnet-pwa-v1';
const ASSETS_TO_CACHE = [
  '/ui/pwa_stitch/index.html',
  '/ui/pwa_stitch/manifest.json',
  '/ui/assets/logos/logo_oficial.png',
  '/ui/assets/logos/boton_4gmax.png',
  '/ui/assets/logos/logo_small.png',
  '/ui/assets/logos/favicon.gif'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE).catch((err) => {
        console.warn('Cache prefetch partial warning:', err);
      });
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Network first para endpoints de API, Cache first para assets estáticos
  if (event.request.url.includes('/api/')) {
    event.respondWith(fetch(event.request));
  } else {
    event.respondWith(
      caches.match(event.request).then((cachedResponse) => {
        return cachedResponse || fetch(event.request);
      })
    );
  }
});

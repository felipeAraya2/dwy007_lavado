
var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/galeria',
    '/quienes-somos',
    '/static/css/estilo.css',
    '/static/img/road_trip.png',
    '/static/img/road_trip2.png',
    '/static/img/open-menu.svg',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
  

     
    );
});



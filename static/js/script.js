// ScrollReveal instance
ScrollReveal().reveal('.hero h1', {
  origin: 'left',
  distance: '50px',
  duration: 1000,
  easing: 'ease-in-out',
});

ScrollReveal().reveal('.hero p, .hero button', {
  origin: 'bottom',
  distance: '30px',
  duration: 1000,
  delay: 300,
  easing: 'ease-in-out',
});

ScrollReveal().reveal('.content .box', {
  origin: 'bottom',
  distance: '40px',
  duration: 1000,
  interval: 200, // Animasi bergantian antar elemen
});

ScrollReveal().reveal('.about h1, .about .btn', {
  origin: 'top',
  distance: '40px',
  duration: 1000,
  easing: 'ease-in-out',
});

ScrollReveal().reveal('.box-daftar button', {
  origin: 'bottom',
  distance: '40px',
  duration: 1000,
  delay: 200,
  interval: 150,
});

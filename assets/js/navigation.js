document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.querySelector('.navbar-toggler');
  const menu = document.getElementById('navbarNav');
  if (!toggle || !menu) return;
  function closeMenu() { menu.classList.remove('show'); toggle.setAttribute('aria-expanded', 'false'); }
  toggle.addEventListener('click', function () {
    const expanded = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(expanded));
    menu.classList.toggle('show', expanded);
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && menu.classList.contains('show')) { closeMenu(); toggle.focus(); }
  });
  menu.querySelectorAll('a').forEach(function (link) { link.addEventListener('click', closeMenu); });
});

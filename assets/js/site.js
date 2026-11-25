// Mobile menu and the (unconnected) subscribe form.
(function () {
  var menu = document.querySelector('.menu');
  var open = document.querySelector('.menu-btn');
  var close = document.querySelector('.menu-close');
  function set(state) {
    menu.classList.toggle('open', state);
    document.body.style.overflow = state ? 'hidden' : '';
    open.setAttribute('aria-expanded', String(state));
    (state ? close : open).focus();
  }
  if (menu && open && close) {
    open.addEventListener('click', function () { set(true); });
    close.addEventListener('click', function () { set(false); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('open')) set(false); });
  }
  document.querySelectorAll('form.form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.parentNode.querySelector('.form-note');
      if (note) note.textContent = 'Thanks. This is a prototype, so sign-up is not connected yet.';
      form.reset();
    });
  });
})();

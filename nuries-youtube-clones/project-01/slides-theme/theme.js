// Slide runtime shared by every lesson of Project 1. Renderer API: window.show(id, step).
// Elements with class "s" and data-step="n" appear at step n (data-until hides them after a step).
// Preview keys: → / Space next step, ← back, Home, End, F fullscreen.
(function () {
  const stages = [...document.querySelectorAll('.stage')];
  const maxStep = (st) => Math.max(0, ...[...st.querySelectorAll('[data-step]')].map((e) => +e.dataset.step));
  let cur = 0, step = 0;
  const counter = document.createElement('div');
  counter.className = 'counter';
  document.body.appendChild(counter);
  function apply() {
    stages.forEach((st, i) => {
      st.classList.toggle('active', i === cur);
      st.querySelectorAll('[data-step]').forEach((e) =>
        e.classList.toggle('on', i === cur && +e.dataset.step <= step && (!e.dataset.until || step <= +e.dataset.until)));
    });
    counter.textContent = `${stages[cur].dataset.id} · step ${step}/${maxStep(stages[cur])}`;
  }
  window.show = (id, s) => { cur = Math.max(0, stages.findIndex((st) => st.dataset.id === id)); step = s ?? maxStep(stages[cur]); apply(); };
  function fit() { const s = Math.min(innerWidth / 1920, innerHeight / 1080); document.documentElement.style.setProperty('--scale', s); }
  if (new URLSearchParams(location.search).has('render')) document.body.classList.add('render'); else { addEventListener('resize', fit); fit(); }
  addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ') { if (step < maxStep(stages[cur])) step++; else if (cur < stages.length - 1) { cur++; step = 0; } apply(); }
    if (e.key === 'ArrowLeft') { if (step > 0) step--; else if (cur > 0) { cur--; step = maxStep(stages[cur]); } apply(); }
    if (e.key === 'Home') { cur = 0; step = 0; apply(); }
    if (e.key === 'End') { cur = stages.length - 1; step = maxStep(stages[cur]); apply(); }
    if (e.key.toLowerCase() === 'f') document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen();
  });
  const h = location.hash.slice(1).split(':');
  if (h[0]) window.show(h[0], h[1] ? +h[1] : undefined); else { step = maxStep(stages[0]); apply(); }
})();

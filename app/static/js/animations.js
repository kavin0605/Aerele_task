// Micro-interactions & Scroll Reveal
(function(){
  function inViewport(el){
    const r = el.getBoundingClientRect();
    return r.top < (window.innerHeight - 60) && r.bottom > 0;
  }

  function reveal(){
    document.querySelectorAll('.fade-up, .fade-in, .scale-in, .slide-in').forEach(el => {
      if (!el.dataset.revealed && inViewport(el)){
        el.dataset.revealed = '1';
        // Trigger animation by forcing reflow (ensures replay if needed)
        void el.offsetWidth;
        el.style.willChange = 'opacity, transform';
      }
    });
  }

  function attachRipple(){
    document.querySelectorAll('.btn').forEach(btn => {
      btn.addEventListener('pointerdown', e => {
        const rect = btn.getBoundingClientRect();
        btn.style.setProperty('--r-x', `${e.clientX - rect.left}px`);
        btn.style.setProperty('--r-y', `${e.clientY - rect.top}px`);
      });
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    // Stagger common lists
    document.querySelectorAll('.dashboard-grid, .stats-grid, .table tbody').forEach(node => node.classList.add('stagger'));

    // Add base animations to common components
    document.querySelectorAll('.dashboard-card, .stat-card, .table-container, header, nav').forEach(node => node.classList.add('fade-in'));
    document.querySelectorAll('.dashboard-card, .table-container, .info-box').forEach(node => node.classList.add('hover-float'));

    attachRipple();
    reveal();
  });

  window.addEventListener('scroll', reveal, { passive: true });
})();

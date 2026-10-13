/**
 * WrapUpBlooms - Water Ripple & Fluid Wave Micro-Interactions
 * Fluid ripple physics on click, undulating wave dividers, and water flow effects
 */

(function () {
  'use strict';

  // Liquid ripple on interactive elements
  function initWaterRipples() {
    const rippleTargets = document.querySelectorAll('.btn, .product-card, .flower-chip, .action-icon-btn');
    
    rippleTargets.forEach((target) => {
      target.addEventListener('click', function (e) {
        const rect = target.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const ripple = document.createElement('span');
        ripple.classList.add('water-ripple-effect');
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;

        target.appendChild(ripple);

        setTimeout(() => {
          ripple.remove();
        }, 800);
      });
    });
  }

  // Smooth undulating water wave SVG path animator
  function initWaveCurrents() {
    const wavePaths = document.querySelectorAll('.water-wave-animated path');
    if (!wavePaths.length) return;

    let time = 0;
    function animateWaves() {
      time += 0.02;
      wavePaths.forEach((path, i) => {
        const offset = Math.sin(time + i * 1.5) * 8;
        path.style.transform = `translateY(${offset}px)`;
      });
      requestAnimationFrame(animateWaves);
    }
    requestAnimationFrame(animateWaves);
  }

  // Scroll reveal with spring physics
  function initScrollReveal() {
    const revealElements = document.querySelectorAll('.product-card, .review-card, .customizer-card, .collection-pill-card');
    if (!('IntersectionObserver' in window)) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    revealElements.forEach((el) => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(24px)';
      el.style.transition = 'opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
      observer.observe(el);
    });

    const style = document.createElement('style');
    style.textContent = `
      .water-ripple-effect {
        position: absolute;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(250, 210, 225, 0.7) 0%, rgba(196, 123, 137, 0.2) 60%, transparent 100%);
        pointer-events: none;
        transform: translate(-50%, -50%) scale(0);
        animation: waterRippleExpand 0.75s ease-out forwards;
        width: 140px;
        height: 140px;
        z-index: 10;
      }
      @keyframes waterRippleExpand {
        to {
          transform: translate(-50%, -50%) scale(2.8);
          opacity: 0;
        }
      }
      .revealed {
        opacity: 1 !important;
        transform: translateY(0) !important;
      }
    `;
    document.head.appendChild(style);
  }

  document.addEventListener('DOMContentLoaded', () => {
    initWaterRipples();
    initWaveCurrents();
    initScrollReveal();
  });
})();

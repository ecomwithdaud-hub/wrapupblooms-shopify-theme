/**
 * WrapUpBlooms - Floating Petals Physics Engine
 * Delicate falling cherry blossom and rose petals with mouse breeze physics
 */

(function () {
  'use strict';

  let canvas, ctx, animId;
  let width, height;
  let petals = [];
  let mouse = { x: -1000, y: -1000, vx: 0, vy: 0, lastX: -1000, lastY: -1000 };
  let isRunning = true;

  const PETAL_COUNT = 38;
  const PETAL_COLORS = [
    { base: 'rgba(250, 210, 225, 0.85)', edge: 'rgba(196, 123, 137, 0.6)' }, // Soft blush
    { base: 'rgba(255, 230, 238, 0.9)',  edge: 'rgba(224, 168, 153, 0.5)' }, // Rose cream
    { base: 'rgba(253, 242, 245, 0.8)',  edge: 'rgba(250, 210, 225, 0.4)' }, // Whispering petal
    { base: 'rgba(255, 245, 240, 0.85)', edge: 'rgba(212, 175, 55, 0.35)' }  // Ivory gold hint
  ];

  class Petal {
    constructor() {
      this.reset(true);
    }

    reset(initial = false) {
      this.x = Math.random() * width;
      this.y = initial ? Math.random() * height : -30;
      this.size = Math.random() * 12 + 10; // 10 to 22px
      this.speedY = Math.random() * 0.9 + 0.6; // gentle drift
      this.speedX = Math.random() * 0.6 - 0.3;
      
      this.angle = Math.random() * Math.PI * 2;
      this.angularSpeed = (Math.random() - 0.5) * 0.02;
      
      this.flip = Math.random() * Math.PI;
      this.flipSpeed = Math.random() * 0.03 + 0.01;
      
      this.color = PETAL_COLORS[Math.floor(Math.random() * PETAL_COLORS.length)];
      this.swayFreq = Math.random() * 0.02 + 0.01;
      this.swayAmp = Math.random() * 1.5 + 0.5;
      this.tick = Math.random() * 1000;
    }

    update() {
      this.tick++;
      
      // Swaying motion like a leaf or petal in the air
      const sway = Math.sin(this.tick * this.swayFreq) * this.swayAmp;
      this.x += this.speedX + sway;
      this.y += this.speedY;
      
      this.angle += this.angularSpeed;
      this.flip += this.flipSpeed;

      // Mouse breeze interaction
      const dx = this.x - mouse.x;
      const dy = this.y - mouse.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 140) {
        const force = (1 - dist / 140) * 3;
        this.x += (dx / dist) * force + mouse.vx * 0.15;
        this.y += (dy / dist) * force * 0.5;
      }

      // Recycle when off screen
      if (this.y > height + 40 || this.x < -60 || this.x > width + 60) {
        this.reset();
      }
    }

    draw(ctx) {
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate(this.angle);
      const scaleX = Math.cos(this.flip);
      ctx.scale(scaleX, 1);

      // Draw delicate organic petal curve
      ctx.beginPath();
      ctx.moveTo(0, -this.size);
      ctx.bezierCurveTo(
        this.size * 0.7, -this.size * 0.8,
        this.size * 0.8, this.size * 0.5,
        0, this.size
      );
      ctx.bezierCurveTo(
        -this.size * 0.8, this.size * 0.5,
        -this.size * 0.7, -this.size * 0.8,
        0, -this.size
      );
      ctx.closePath();

      // Soft petal gradient fill
      const grad = ctx.createRadialGradient(0, 0, 1, 0, 0, this.size);
      grad.addColorStop(0, this.color.base);
      grad.addColorStop(1, this.color.edge);
      ctx.fillStyle = grad;
      ctx.fill();

      // Delicate petal vein spine
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.lineWidth = 0.75;
      ctx.beginPath();
      ctx.moveTo(0, -this.size * 0.7);
      ctx.lineTo(0, this.size * 0.7);
      ctx.stroke();

      ctx.restore();
    }
  }

  function init() {
    canvas = document.getElementById('petals-canvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'petals-canvas';
      document.body.prepend(canvas);
    }
    ctx = canvas.getContext('2d');

    resize();
    window.addEventListener('resize', resize);

    // Track mouse speed for breeze effect
    window.addEventListener('mousemove', (e) => {
      mouse.vx = e.clientX - mouse.lastX;
      mouse.vy = e.clientY - mouse.lastY;
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      mouse.lastX = e.clientX;
      mouse.lastY = e.clientY;
    });

    // Populate petals
    petals = [];
    for (let i = 0; i < PETAL_COUNT; i++) {
      petals.push(new Petal());
    }

    animate();
    setupToggleButton();
  }

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }

  function animate() {
    if (!isRunning) return;
    ctx.clearRect(0, 0, width, height);

    // Dampen mouse velocity
    mouse.vx *= 0.85;
    mouse.vy *= 0.85;

    for (let i = 0; i < petals.length; i++) {
      petals[i].update();
      petals[i].draw(ctx);
    }

    animId = requestAnimationFrame(animate);
  }

  function setupToggleButton() {
    const btn = document.getElementById('toggle-petals');
    if (btn) {
      btn.addEventListener('click', () => {
        isRunning = !isRunning;
        if (isRunning) {
          btn.innerHTML = '<span class="sparkle-dot"></span> Floating Blooms: ON';
          animate();
        } else {
          ctx.clearRect(0, 0, width, height);
          btn.innerHTML = '<span class="sparkle-dot" style="opacity:0.3"></span> Floating Blooms: PAUSED';
          cancelAnimationFrame(animId);
        }
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.WrapUpBloomsPetals = {
    toggle: () => {
      isRunning = !isRunning;
      if (isRunning) animate();
      else cancelAnimationFrame(animId);
    }
  };
})();

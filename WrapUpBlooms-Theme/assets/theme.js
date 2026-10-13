/**
 * WrapUpBlooms - Master Theme Controller
 * Handles Cart Drawer, Customizer, Modals, Accordions, and Sticky Nav
 */

(function () {
  'use strict';

  // State
  const cartState = {
    items: [
      {
        id: 1,
        title: "Personalized Leather Lipstick Case Keychain",
        customization: "Sophia • Rose (June)",
        price: 24.00,
        quantity: 1,
        image: "bespoke-lipstick-keychain.jpg"
      },
      {
        id: 2,
        title: "Custom Engraved LED Pocket Makeup Mirror",
        customization: "Emma • Wildflower Wreath",
        price: 28.50,
        quantity: 1,
        image: "bespoke-compact-mirror.jpg"
      }
    ],
    freeShippingThreshold: 60.00
  };

  // Sticky Header Scroll
  function initStickyHeader() {
    const header = document.querySelector('.site-header');
    if (!header) return;

    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // Interactive Live Customizer for Signature Item
  function initCustomizer() {
    const nameInput = document.getElementById('customizer-name-input');
    const displayElement = document.getElementById('live-engrave-name-display');
    const flowerDisplay = document.getElementById('live-engrave-flower-display');
    const flowerChips = document.querySelectorAll('.flower-chip');
    const addToCartBtn = document.getElementById('customizer-add-btn');

    if (nameInput && displayElement) {
      nameInput.addEventListener('input', (e) => {
        const val = e.target.value.trim();
        displayElement.textContent = val ? val : "Your Name";
      });
    }

    if (flowerChips.length && flowerDisplay) {
      flowerChips.forEach((chip) => {
        chip.addEventListener('click', () => {
          flowerChips.forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          const flowerName = chip.getAttribute('data-flower');
          const flowerMonth = chip.getAttribute('data-month');
          flowerDisplay.textContent = `${flowerName} (${flowerMonth})`;
        });
      });
    }

    if (addToCartBtn) {
      addToCartBtn.addEventListener('click', () => {
        const name = (nameInput && nameInput.value.trim()) || "Sophia";
        const activeChip = document.querySelector('.flower-chip.active');
        const flower = activeChip ? activeChip.getAttribute('data-flower') : "Wildflower";

        addItemToCart({
          id: Date.now(),
          title: "Personalized Leather Lipstick Case Keychain",
          customization: `${name} • ${flower}`,
          price: 24.00,
          quantity: 1,
          image: "bespoke-lipstick-keychain.jpg"
        });

        openCartDrawer();
      });
    }
  }

  // Cart Drawer UI & Events
  function initCartDrawer() {
    const triggers = document.querySelectorAll('.cart-trigger-btn, .btn-quick-add');
    const drawer = document.getElementById('cart-drawer');
    const overlay = document.getElementById('cart-drawer-overlay');
    const closeBtn = document.getElementById('cart-drawer-close');

    triggers.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        
        // If it's a quick add button on a card
        const card = btn.closest('.product-card');
        if (card) {
          const title = card.querySelector('.product-title')?.innerText || "Custom Keepsake";
          const priceText = card.querySelector('.current-price')?.innerText || "$25.00";
          const price = parseFloat(priceText.replace(/[^0-9.]/g, '')) || 25.00;
          const img = card.querySelector('.product-card-media img')?.getAttribute('src') || "bespoke-lipstick-keychain.jpg";

          addItemToCart({
            id: Date.now(),
            title: title,
            customization: "Custom Engraved",
            price: price,
            quantity: 1,
            image: img
          });
        }
        
        openCartDrawer();
      });
    });

    if (closeBtn) closeBtn.addEventListener('click', closeCartDrawer);
    if (overlay) overlay.addEventListener('click', closeCartDrawer);
  }

  function openCartDrawer() {
    const drawer = document.getElementById('cart-drawer');
    const overlay = document.getElementById('cart-drawer-overlay');
    if (drawer && overlay) {
      renderCartItems();
      drawer.classList.add('active');
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeCartDrawer() {
    const drawer = document.getElementById('cart-drawer');
    const overlay = document.getElementById('cart-drawer-overlay');
    if (drawer && overlay) {
      drawer.classList.remove('active');
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  function addItemToCart(item) {
    cartState.items.push(item);
    updateCartCount();
    showToast(`🌸 Added "${item.title}" to your blooms cart!`);
  }

  function renderCartItems() {
    const container = document.getElementById('cart-drawer-items-list');
    const subtotalEl = document.getElementById('cart-drawer-subtotal');
    const shippingMeterFill = document.getElementById('shipping-meter-fill');
    const shippingMeterText = document.getElementById('shipping-meter-text');
    if (!container) return;

    if (cartState.items.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 3rem 1rem;">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🌸</div>
          <h4 style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 0.5rem; color: var(--primary-deep);">Your cart is empty</h4>
          <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.5rem;">Pick a handcrafted bloom to personalize with love.</p>
          <button class="btn btn-primary" onclick="window.WrapUpBloomsTheme.closeCart();">Start Shopping</button>
        </div>
      `;
      if (subtotalEl) subtotalEl.textContent = '$0.00';
      if (shippingMeterFill) shippingMeterFill.style.width = '0%';
      if (shippingMeterText) shippingMeterText.textContent = 'Add $60.00 more to unlock Free Gift Box Packaging!';
      return;
    }

    let subtotal = 0;
    container.innerHTML = cartState.items.map((item, idx) => {
      subtotal += item.price * item.quantity;
      return `
        <div class="cart-item" data-index="${idx}">
          <img src="${item.image}" alt="${item.title}" class="cart-item-img" onerror="this.src='bespoke-lipstick-keychain.jpg'">
          <div class="cart-item-details">
            <h5 class="cart-item-title">${item.title}</h5>
            <span class="cart-item-customization">${item.customization}</span>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 6px;">
              <span class="cart-item-price">$${(item.price * item.quantity).toFixed(2)}</span>
              <button class="cart-item-remove-btn" onclick="window.WrapUpBloomsTheme.removeItem(${idx})" style="background: none; border: none; font-size: 0.75rem; color: var(--primary-rose); cursor: pointer; text-decoration: underline;">Remove</button>
            </div>
          </div>
        </div>
      `;
    }).join('');

    if (subtotalEl) subtotalEl.textContent = `$${subtotal.toFixed(2)}`;

    // Update free shipping bar
    if (shippingMeterFill && shippingMeterText) {
      const remaining = cartState.freeShippingThreshold - subtotal;
      const progress = Math.min(100, (subtotal / cartState.freeShippingThreshold) * 100);
      shippingMeterFill.style.width = `${progress}%`;
      
      if (remaining <= 0) {
        shippingMeterText.innerHTML = `🎉 <strong>Congratulations!</strong> You unlocked FREE Luxury Gift Box Packaging!`;
      } else {
        shippingMeterText.innerHTML = `🌸 Add <strong>$${remaining.toFixed(2)}</strong> more to get FREE Luxury Gift Packaging!`;
      }
    }
  }

  function updateCartCount() {
    const badges = document.querySelectorAll('.cart-count-badge');
    const totalCount = cartState.items.reduce((sum, item) => sum + item.quantity, 0);
    badges.forEach(b => b.textContent = totalCount);
  }

  function removeItem(index) {
    cartState.items.splice(index, 1);
    updateCartCount();
    renderCartItems();
  }

  // Toast Notification
  function showToast(msg) {
    const toast = document.createElement('div');
    toast.className = 'bloom-toast';
    toast.innerHTML = msg;
    toast.style.cssText = `
      position: fixed;
      bottom: 30px;
      right: 30px;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      border: 1px solid var(--accent-rose-gold);
      color: var(--primary-deep);
      padding: 14px 24px;
      border-radius: 999px;
      box-shadow: 0 10px 30px rgba(196, 123, 137, 0.25);
      font-size: 0.9rem;
      font-weight: 600;
      z-index: 2000;
      transform: translateY(20px);
      opacity: 0;
      transition: all 0.4s ease;
    `;
    document.body.appendChild(toast);

    setTimeout(() => {
      toast.style.transform = 'translateY(0)';
      toast.style.opacity = '1';
    }, 20);

    setTimeout(() => {
      toast.style.transform = 'translateY(20px)';
      toast.style.opacity = '0';
      setTimeout(() => toast.remove(), 400);
    }, 3200);
  }

  // FAQ Accordion
  function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach((item) => {
      const q = item.querySelector('.faq-question');
      if (q) {
        q.addEventListener('click', () => {
          const isOpen = item.classList.contains('active');
          faqItems.forEach(i => i.classList.remove('active'));
          if (!isOpen) item.classList.add('active');
        });
      }
    });
  }

  // Filter Tabs
  function initCollectionTabs() {
    const tabs = document.querySelectorAll('.collection-filter-tab');
    const cards = document.querySelectorAll('.product-grid-target .product-card');

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const cat = tab.getAttribute('data-category');
        cards.forEach((card) => {
          if (cat === 'all' || card.getAttribute('data-category') === cat) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    initStickyHeader();
    initCustomizer();
    initCartDrawer();
    initFAQ();
    initCollectionTabs();
    updateCartCount();
  });

  // Global helper API
  window.WrapUpBloomsTheme = {
    openCart: openCartDrawer,
    closeCart: closeCartDrawer,
    addItem: addItemToCart,
    removeItem: removeItem
  };
})();

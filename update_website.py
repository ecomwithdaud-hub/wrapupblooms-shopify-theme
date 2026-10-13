import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Announcement Bar to include phone
announcement_old = '''<span>✨ <strong>Use code BLOOM15 for 15% Off Your First Order</strong></span>'''
announcement_new = '''<span>📞 <strong>Call/Text: <a href="tel:9782338050" style="color: inherit; text-decoration: underline;">(978) 233-8050</a></strong></span>
        <span style="opacity: 0.5;">•</span>
        <span>✨ <strong>Use code BLOOM15 for 15% Off Your First Order</strong></span>'''

if announcement_old in html:
    html = html.replace(announcement_old, announcement_new)

# 2. Update Header: Add Contact nav link and Phone pill
nav_old = '''            <li><a href="#reviews" class="nav-link">Reviews</a></li>
          </ul>'''
nav_new = '''            <li><a href="#reviews" class="nav-link">Reviews</a></li>
            <li><a href="#contact-section" class="nav-link">Contact</a></li>
          </ul>'''

if nav_old in html:
    html = html.replace(nav_old, nav_new)

header_actions_old = '''        <div class="header-actions">
          <button class="action-icon-btn" aria-label="Search" onclick="alert('Search WrapUpBlooms catalog');">'''
header_actions_new = '''        <div class="header-actions">
          <a href="tel:9782338050" class="header-phone-pill" style="display: inline-flex; align-items: center; gap: 6px; font-size: 0.85rem; font-weight: 600; color: var(--primary-dark-rose); background: rgba(250, 210, 225, 0.45); padding: 6px 14px; border-radius: 999px; border: 1px solid var(--accent-rose-gold); text-decoration: none;">
            <span>📞</span>
            <span>(978) 233-8050</span>
          </a>
          <button class="action-icon-btn" aria-label="Search" onclick="alert('Search WrapUpBlooms catalog');">'''

if header_actions_old in html:
    html = html.replace(header_actions_old, header_actions_new)

# 3. Update Hero CTAs: "Contact Us Now to Get Your Mirror" and "Get Your Product"
hero_cta_old = '''        <div class="hero-cta-group">
          <a href="#featured-collection" class="btn btn-primary">
            <span>Shop Custom Gifts</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
          <a href="#water-showcase" class="btn btn-secondary">
            <span>Personalize Lipstick Case</span>
          </a>
        </div>'''

hero_cta_new = '''        <div class="hero-cta-group">
          <a href="#contact-section" class="btn btn-primary">
            <span>Contact Us Now to Get Your Mirror</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
          <a href="#water-showcase" class="btn btn-secondary">
            <span>Get Your Product</span>
          </a>
        </div>'''

if hero_cta_old in html:
    html = html.replace(hero_cta_old, hero_cta_new)

# 4. Update Story Section: Add Shop Members (Saddam, Naina) and Production Partners (Engraving Shop)
story_old_end = '''          <div style="display: flex; gap: 2rem; align-items: center; border-top: 1px solid var(--border-delicate); padding-top: 1.5rem;">
            <div>
              <div style="font-family: var(--font-serif); font-size: 1.5rem; font-style: italic; color: var(--primary-rose);">WrapUpBlooms Studio</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">Artisan Gifting Specialists</div>
            </div>
            <a href="#featured-collection" class="btn btn-secondary" style="margin-left: auto;">Explore Creations</a>
          </div>
        </div>
      </div>
    </div>
  </section>'''

story_new_end = '''          <div style="display: flex; gap: 2rem; align-items: center; border-top: 1px solid var(--border-delicate); padding-top: 1.5rem;">
            <div>
              <div style="font-family: var(--font-serif); font-size: 1.5rem; font-style: italic; color: var(--primary-rose);">WrapUpBlooms Studio</div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">Artisan Gifting Specialists</div>
            </div>
            <a href="#contact-section" class="btn btn-secondary" style="margin-left: auto;">Contact Us Now to Get Your Mirror</a>
          </div>
        </div>
      </div>

      <!-- Shop Members & Production Partners Section -->
      <div style="background: var(--bg-cream); border-radius: 32px; padding: 3rem; border: 1px solid var(--border-delicate); box-shadow: var(--shadow-soft); margin-top: 3.5rem;">
        <div style="text-align: center; max-width: 650px; margin: 0 auto 2.5rem;">
          <span class="section-subtitle-pill">Meet the Team</span>
          <h3 style="font-family: var(--font-serif); font-size: 2.2rem; color: var(--primary-deep); margin-bottom: 0.75rem;">Shop Members & Production Partners</h3>
          <p style="font-size: 0.95rem; color: var(--text-secondary);">The passionate artisans and skilled partners behind every personalized floral keepsake.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
          <!-- Shop Member: Saddam -->
          <div style="background: #FFF; padding: 2rem; border-radius: 24px; border: 1px solid var(--border-delicate); box-shadow: 0 4px 15px rgba(196, 123, 137, 0.06);">
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 1rem;">
              <div style="width: 50px; height: 50px; border-radius: 50%; background: var(--bg-petal); color: var(--primary-rose); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; font-weight: bold;">
                S
              </div>
              <div>
                <h4 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--primary-deep); margin-bottom: 2px;">Saddam</h4>
                <span style="font-size: 0.8rem; font-weight: 600; color: var(--primary-rose); text-transform: uppercase; letter-spacing: 0.05em;">Designer, Owner, Curator</span>
              </div>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
              Curates and oversees every custom keepsake collection. Dedicated to crafting memorable, romantic designs that celebrate life's heartfelt moments.
            </p>
          </div>

          <!-- Shop Member: Naina -->
          <div style="background: #FFF; padding: 2rem; border-radius: 24px; border: 1px solid var(--border-delicate); box-shadow: 0 4px 15px rgba(196, 123, 137, 0.06);">
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 1rem;">
              <div style="width: 50px; height: 50px; border-radius: 50%; background: var(--bg-petal); color: var(--primary-rose); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; font-weight: bold;">
                N
              </div>
              <div>
                <h4 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--primary-deep); margin-bottom: 2px;">Naina</h4>
                <span style="font-size: 0.8rem; font-weight: 600; color: var(--primary-rose); text-transform: uppercase; letter-spacing: 0.05em;">Designer, Crafter, Customer Service</span>
              </div>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
              Specializes in delicate artisan crafting, detailed assembly, and providing warm, responsive support for custom requests.
            </p>
          </div>

          <!-- Production Partner: Engraving Shop -->
          <div style="background: #FFF; padding: 2rem; border-radius: 24px; border: 1px solid var(--border-delicate); box-shadow: 0 4px 15px rgba(196, 123, 137, 0.06);">
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 1rem;">
              <div style="width: 50px; height: 50px; border-radius: 50%; background: var(--bg-blush); color: var(--accent-gold); display: flex; align-items: center; justify-content: center; font-size: 1.4rem;">
                ⚙️
              </div>
              <div>
                <h4 style="font-family: var(--font-serif); font-size: 1.25rem; color: var(--primary-deep); margin-bottom: 2px;">Engraving Shop</h4>
                <span style="font-size: 0.8rem; font-weight: 600; color: var(--primary-dark-rose); text-transform: uppercase; letter-spacing: 0.05em;">Production Partner &bull; NH, United States</span>
              </div>
            </div>
            <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;">
              A skilled craftsman and trusted partner who handles the physical engraving and localized dispatch for our US-bound orders.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>'''

if story_old_end in html:
    html = html.replace(story_old_end, story_new_end)

# 5. Add Contact Section with Phone (978) 233-8050 and Store Policies before Cart Drawer
faq_section_end = '''  </section>

  <!-- Slide-out AJAX Cart Drawer -->'''

contact_and_policies_section = '''  </section>

  <!-- Contact & Store Policies Section -->
  <section class="contact-policies-section" id="contact-section" style="padding: 6rem 0; background: linear-gradient(180deg, var(--bg-cream) 0%, #FFF5F8 100%); position: relative;">
    <div class="container">
      <div class="section-header-center">
        <span class="section-subtitle-pill">Get in Touch</span>
        <h2 class="section-title">Contact Us Now to Get Your Mirror</h2>
        <p>Whether you need a custom engraving quote, bridal party consultation, or have an order inquiry &mdash; we are always here to help you bloom.</p>
      </div>

      <div style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 3rem; align-items: start; margin-bottom: 4rem;">
        <!-- Contact Card -->
        <div style="background: #FFF; padding: 2.5rem; border-radius: 28px; border: 1.5px solid var(--border-delicate); box-shadow: var(--shadow-hover);">
          <h3 style="font-family: var(--font-serif); font-size: 1.75rem; color: var(--primary-deep); margin-bottom: 1rem;">
            Direct Artisan Studio Support
          </h3>
          <p style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 2rem; line-height: 1.7;">
            Reach Saddam or Naina directly. We respond promptly to all personalization questions and rush requests.
          </p>

          <div style="display: flex; flex-direction: column; gap: 1.25rem; margin-bottom: 2rem;">
            <div style="display: flex; align-items: center; gap: 16px; padding: 14px 20px; background: var(--bg-cream); border-radius: 16px; border: 1px solid var(--border-delicate);">
              <span style="font-size: 1.5rem;">📞</span>
              <div>
                <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Direct Phone / Text</div>
                <a href="tel:9782338050" style="font-size: 1.25rem; font-weight: 700; color: var(--primary-dark-rose); text-decoration: none;">(978) 233-8050</a>
              </div>
            </div>

            <div style="display: flex; align-items: center; gap: 16px; padding: 14px 20px; background: var(--bg-cream); border-radius: 16px; border: 1px solid var(--border-delicate);">
              <span style="font-size: 1.5rem;">⏱️</span>
              <div>
                <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Production & Support Hours</div>
                <div style="font-size: 1rem; font-weight: 600; color: var(--primary-deep);">Mon - Sat: 9:00 AM - 7:00 PM EST</div>
              </div>
            </div>
          </div>

          <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <a href="tel:9782338050" class="btn btn-primary" style="flex: 1;">
              <span>Call / Text: (978) 233-8050</span>
            </a>
            <a href="#water-showcase" class="btn btn-secondary">
              <span>Get Your Product</span>
            </a>
          </div>
        </div>

        <!-- Store Policies Card -->
        <div style="background: #FFF; padding: 2.5rem; border-radius: 28px; border: 1.5px solid var(--border-delicate); box-shadow: var(--shadow-soft);">
          <h3 style="font-family: var(--font-serif); font-size: 1.75rem; color: var(--primary-deep); margin-bottom: 1.5rem;">
            Store Policies
          </h3>

          <!-- Payment Methods -->
          <div style="margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border-delicate);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
              <span style="font-size: 1.3rem;">💳</span>
              <h4 style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--primary-deep); margin: 0;">Accepted Payment Methods</h4>
            </div>
            <p style="color: var(--text-secondary); font-size: 0.925rem; line-height: 1.7;">
              PayPal, Visa, Mastercard, Apple Pay, and Gift Cards. Also accepts Etsy Gift Cards and Etsy Credits.
            </p>
          </div>

          <!-- Returns & Exchanges -->
          <div>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
              <span style="font-size: 1.3rem;">🔄</span>
              <h4 style="font-family: var(--font-serif); font-size: 1.2rem; color: var(--primary-deep); margin: 0;">Returns & Exchanges</h4>
            </div>
            <p style="color: var(--text-secondary); font-size: 0.925rem; line-height: 1.7;">
              See item details for return and exchange eligibility.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Slide-out AJAX Cart Drawer -->'''

if faq_section_end in html:
    html = html.replace(faq_section_end, contact_and_policies_section)

# 6. Update Footer with Phone and Store Policies
footer_old = '''        <div style="font-size: 0.85rem; color: #D6BDC4;">
            ✨ Over 12,000+ 5-Star Reviews &bull; Free Gift Packaging Available
          </div>
        </div>'''

footer_new = '''        <div style="font-size: 0.95rem; color: #FFF; margin-bottom: 0.5rem;">
            📞 <strong>Direct Contact:</strong> <a href="tel:9782338050" style="color: var(--accent-blush); text-decoration: underline;">(978) 233-8050</a>
          </div>
          <div style="font-size: 0.85rem; color: #D6BDC4;">
            ✨ Over 12,000+ 5-Star Reviews &bull; Free Gift Packaging Available
          </div>
        </div>'''

if footer_old in html:
    html = html.replace(footer_old, footer_new)

customer_care_old = '''        <div>
          <h4 class="footer-heading">Customer Care</h4>
          <ul class="footer-links">
            <li><a href="#story">About WrapUpBlooms</a></li>
            <li><a href="#faq">Shipping & Production Times</a></li>
            <li><a href="#water-showcase">Birth Flower Chart</a></li>
            <li><a href="#faq">FAQ</a></li>
            <li><a href="#">Contact Support</a></li>
          </ul>
        </div>'''

customer_care_new = '''        <div>
          <h4 class="footer-heading">Customer Care</h4>
          <ul class="footer-links">
            <li><a href="#story">About WrapUpBlooms</a></li>
            <li><a href="tel:9782338050">📞 Call: (978) 233-8050</a></li>
            <li><a href="#contact-section">Contact Us Now to Get Your Mirror</a></li>
            <li><a href="#faq">Shipping & Production Times</a></li>
            <li><a href="#water-showcase">Birth Flower Chart</a></li>
            <li><a href="#faq">FAQ</a></li>
          </ul>
        </div>'''

if customer_care_old in html:
    html = html.replace(customer_care_old, customer_care_new)

# Add policies row in footer
footer_bottom_row_old = '''      <div class="footer-bottom">
        <div>
          &copy; 2026 WrapUpBlooms. All rights reserved. Handcrafted with passion.
        </div>
        <div style="display: flex; gap: 1rem; align-items: center;">
          <span>🔒 256-Bit SSL Encrypted Checkout</span>
          <span>&bull;</span>
          <span>🌸 Handcrafted in Small Batches</span>
        </div>
      </div>'''

footer_bottom_row_new = '''      <!-- Store Policies in Footer -->
      <div style="border-top: 1px solid rgba(255, 255, 255, 0.12); padding: 2rem 0 1.5rem; margin-bottom: 1.5rem; display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
        <div style="background: rgba(255, 255, 255, 0.05); padding: 1.25rem 1.5rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
          <h5 style="color: #FFF; font-family: var(--font-serif); font-size: 1.05rem; margin-bottom: 0.35rem;">
            💳 Accepted Payment Methods
          </h5>
          <p style="color: #D6BDC4; font-size: 0.85rem; line-height: 1.6; margin: 0;">
            PayPal, Visa, Mastercard, Apple Pay, and Gift Cards. Also accepts Etsy Gift Cards and Etsy Credits.
          </p>
        </div>

        <div style="background: rgba(255, 255, 255, 0.05); padding: 1.25rem 1.5rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
          <h5 style="color: #FFF; font-family: var(--font-serif); font-size: 1.05rem; margin-bottom: 0.35rem;">
            🔄 Returns & Exchanges
          </h5>
          <p style="color: #D6BDC4; font-size: 0.85rem; line-height: 1.6; margin: 0;">
            See item details for return and exchange eligibility.
          </p>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; 2026 WrapUpBlooms. All rights reserved. Handcrafted with passion.
        </div>
        <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
          <span>📞 (978) 233-8050</span>
          <span>&bull;</span>
          <span>🔒 256-Bit SSL Encrypted Checkout</span>
          <span>&bull;</span>
          <span>🌸 Handcrafted in Small Batches</span>
        </div>
      </div>'''

if footer_bottom_row_old in html:
    html = html.replace(footer_bottom_row_old, footer_bottom_row_new)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("live-preview.html", "w", encoding="utf-8") as f:
    f.write(html)

# Also update preview/index.html with relative path adjustments
preview_html = html.replace('src="images/', 'src="images/').replace('WrapUpBlooms-Theme/assets/', '../WrapUpBlooms-Theme/assets/')
with open("preview/index.html", "w", encoding="utf-8") as f:
    f.write(preview_html)

print("Updated index.html, live-preview.html, and preview/index.html successfully!")

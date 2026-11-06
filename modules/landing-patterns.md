# Landing / page patterns: 34

Format: id | pattern | section order | CTA | color | effects | rule. Pick by goal and product type.

1. **Hero + Features + CTA**: Hero (headline/image) > value prop > 3-5 key features > CTA > footer. CTA: sticky in hero + bottom. Hero brand/vibrant, cards #FAFAFA, CTA contrasting. FX: hero parallax, card hover lift, CTA glow. Rule: deep CTA placement; CTA label text 4.5:1 on button; parallax off under reduced motion.
2. **Hero + Testimonials + CTA**: Hero > problem > solution > testimonials carousel > CTA. CTA after social proof. Quotes italic muted #666. Rule: verified testimonials with photo, name, role; carousel needs prev/next + pause, stops on focus/hover/reduced motion, announces position.
3. **Product Demo + Features**: Hero > product video/mockup (center) > feature breakdown > optional comparison > CTA. Rule: demo only if it explains value better than static media; captions, transcript, visible play/pause, non-video fallback; no autoplay under reduced motion.
4. **Minimal Single Column**: headline > short description > up to 3 benefit bullets > one large CTA > footer. Lots of whitespace, no nav clutter, mobile-first.
5. **Funnel (3-step)**: Hero > step 1 problem > step 2 solution > step 3 action, mini-CTA per step. Progress indicator, progressive disclosure.
6. **Comparison Table + CTA**: Hero > problem > comparison table (you vs competitors) > optional pricing > CTA below table. Highlight your row; mention free trial.
7. **Lead Magnet + Form**: benefit headline > magnet preview (ebook/checklist) > minimal form > submit CTA. Ask only what is needed; show progress on submit.
8. **Pricing Page + CTA**: pricing headline > plan cards > feature table > FAQ > final CTA; sticky CTA in nav. Highlight the plan for the target audience; show real annual savings; FAQ handles objections.
9. **Video-First Hero**: video background > feature overlay > benefits > CTA. Overlay strong enough for text contrast; captions, visible pause, static poster under reduced motion; pause when offscreen.
10. **Scroll-Triggered Storytelling**: hook > chapter 1 problem > chapter 2 journey > chapter 3 solution > climax CTA; mini-CTA per chapter. Understandable without scroll effects; progress indicator; complete DOM reading order; simplify on mobile.
11. **AI Personalization Landing**: dynamic hero > relevant features > tailored testimonials > smart CTA. Needs consent-aware analytics and fallback for new users.
12. **Waitlist / Coming Soon**: hero with countdown > teaser > email capture > social proof. Form above fold + sticky; no fabricated scarcity; show waitlist count only if verified and dated; static deadline as text.
13. **Comparison Table Focus**: problem hero > comparison matrix > feature deep-dive > winner CTA. Be factual; your column highlighted; sticky header.
14. **Pricing-Focused Landing**: value hero > 3 pricing cards > feature comparison > FAQ > final CTA. Popular plan highlighted; free grey, enterprise dark; transparent totals.
15. **App Store Style**: hero with device mockup > screenshot carousel > feature icons > reviews/ratings > download CTAs (App Store + Google Play) throughout. Real screenshots and verified ratings only; buttons as well as swipe; stop auto-rotation on focus/reduced motion.
16. **FAQ / Documentation**: hero with search bar > popular categories > FAQ accordion > contact CTA. High readability, search autocomplete, helpful-feedback buttons, escalation path.
17. **Immersive / Interactive**: full-screen interactive element > guided tour > benefits > CTA after completion; skip option. Provide skip, keyboard, reduced-motion and non-3D fallback.
18. **Event / Conference**: hero (date, place, countdown) > speakers > agenda > sponsors > Register CTA (sticky + after speakers + bottom). Early-bird deadline as text; static final state for countdown.
19. **Product Review / Ratings**: hero with aggregate rating > rating breakdown > reviews > buy CTA. Verified purchases badge, filters, respond to negatives.
20. **Community / Forum**: value prop > popular topics > active members > Join CTA. Counts only if verified and dated; pause controls for live feeds.
21. **Before-After Transformation**: problem state > slider comparison > how it works > results CTA. Arrow buttons + keyboard steps (no drag-only); real metrics.
22. **Marketplace / Directory**: search-focused hero > categories > featured listings > trust/safety > "become a seller/host" CTA. Search is the primary CTA; carousels with prev/next + pause.
23. **Newsletter / Content First**: value prop + inline form > recent issues > subscriber count (only if verified) > author. Minimal, paper-like background, link a sample issue.
24. **Webinar Registration**: topic + timer + form > what you'll learn > speaker > bonuses > form again. State time + timezone as text; claim limited seats only if verified; pause for tickers.
25. **Enterprise Gateway**: mission/video hero > solutions by industry > by role > client logos > Contact Sales (+ Login secondary). Navy/grey, path selection "I am a...", pause for rotating logos.
26. **Portfolio Grid**: name/role > masonry project grid > about > contact. Neutral bg so work shines; filter by category; fast loading; hover overlay + lightbox.
27. **Horizontal Scroll Journey**: vertical intro > horizontal track > detail reveal > vertical footer. Keep a normal vertical navigation path; disable scroll-jacking under reduced motion.
28. **Bento Grid Showcase**: hero > bento grid of features > detail cards > specs > CTA. Cards #F5F5F7 or glass, hover scale 1.02; usable without hover; stack on mobile.
29. **Interactive 3D Configurator**: configurator hero > synced feature highlight > price/specs > purchase. Buttons + keyboard for rotate/zoom, 2D/spec fallback.
30. **AI-Driven Dynamic Landing**: prompt/input hero > generated result preview > how it works > value prop. "Show, don't tell", low-friction start; disable typing/shimmer under reduced motion.
31. **Feature-Rich Showcase**: hero > 4-6 feature cards > use cases/benefits > social proof/logos > CTA. One message per card; repeat CTA.
32. **Hero-Centric Design**: full-bleed hero > single value strip > key proof > primary CTA. One CTA; keep a cue to next content; static hero under reduced motion.
33. **Trust & Authority + Conversion**: mission/credibility hero > proof (logos, certs, stats) > solution > CTA path. Contact Sales/Get Quote; security badges, case studies, transparent pricing.
34. **Real-Time / Operations Landing**: hero with live preview/status > key metrics > how it works > CTA (trial/contact). Label "live" only if backed by a current source; show update time; pause controls.

## Section rules (all patterns)
- One idea and one heading per section; alternate dense and airy sections.
- Proof (numbers, logos, quotes) near every CTA; no fake counters, ratings or urgency.
- Footer has navigation, legal, contact.
- Motion must have a static final state under `prefers-reduced-motion`.

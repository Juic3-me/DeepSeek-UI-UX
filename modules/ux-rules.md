# UX, accessibility and interaction rules (130 guidelines, condensed)

Severity: H = must, M = should, L = nice. Each line: rule. Avoid: anti-pattern.

## Navigation
- [M] Anchor links scroll smoothly: `html{scroll-behavior:smooth}`. Avoid: jumps.
- [M] Sticky nav must not cover content: body padding or `scroll-padding-top` = nav height.
- [M] Mark the active item (color/underline + `aria-current`).
- [H] Never break the back button: use `history.pushState` for views, not `location.replace`.
- [M] URL reflects state (hash or query) so views can be shared.
- [L] Breadcrumbs only for 3+ levels of depth.
- [M] Navbar state change at 50-100px scroll, transition 0.3-0.4s `cubic-bezier(.4,0,.2,1)`; shrink header ~80px to 56px with explicit heights.
- [M] Auto-hide on scroll down / show on scroll up: `transform:translateY(-100%)`, 80px threshold, `requestAnimationFrame` throttle. Avoid `display:none` toggles.
- [M] Mobile menu animates (`max-height`+`opacity` or transform), not instant display toggle.
- [M] Page transitions: View Transitions API as progressive enhancement (`if (document.startViewTransition)`), name shared elements with `view-transition-name`.

## Animation
- [H] Animate 1-2 key elements per view. Avoid: everything moving.
- [M] 150-300ms for micro-interactions, <500ms for UI. Avoid: 1000ms.
- [H] Respect `prefers-reduced-motion` (`animation-duration:.01ms!important` fallback); every animation has a static final state.
- [H] Loading feedback for async (skeleton/spinner). Avoid: blank/frozen UI.
- [H] Never rely on hover alone (touch has no hover): primary actions work on click/tap.
- [M] Infinite animation only for loaders. Avoid: bouncing icons.
- [M] Animate `transform` and `opacity`, not width/height/top/left.
- [L] ease-out for entering, ease-in for exiting. Avoid: linear.
- [M] Scroll-linked effects via CSS `animation-timeline: scroll()/view()` over JS scroll listeners; fall back gracefully.
- [H] Parallax/scroll-jacking causes nausea: disable under reduced motion.
- [M] Rapid interactions may cancel animation but final state, focus and content must remain correct.

## Layout
- [H] z-index scale (10 dropdown, 20 sticky, 30 modal, 40 toast, 50 tooltip). Avoid: `z-index:99999`.
- [M] Test that `overflow:hidden` is not clipping content; understand stacking contexts.
- [M] Fixed elements account for safe areas and each other.
- [H] Reserve space for async content: `aspect-ratio`, width/height on images, skeletons. Avoid: layout shift.
- [M] `min-height:100dvh` instead of `100vh` on mobile.
- [M] Text container max 65-75ch (`max-w-prose`).
- [M] Essential text must reflow without clipping at narrow widths, zoom and text scaling; long URLs/identifiers wrap; chips/tags wrap or use an operable `+n`; badges not color-only; truncated labels keep an accessible full value.

## Touch and mobile
- [H] Targets >= 44x44px (WCAG 2.2 AA minimum 24x24px). Avoid: 24px icon buttons on touch.
- [M] 8px gaps between targets.
- [M] Avoid horizontal-swipe conflicts with system gestures; use platform-native gestures.
- [M] `touch-action:manipulation` removes tap delay.
- [L] `overscroll-behavior:contain` where pull-to-refresh is unwanted; haptics sparingly.
- [H] Primary actions in the thumb zone (bottom of screen, bottom nav, FAB).

## Interaction states
- [H] Visible `:focus-visible` ring on all interactive elements (2px, offset 2px). Avoid: `outline:none` without replacement.
- [M] Hover: cursor + subtle change; active: pressed feedback (`active:scale-95`); disabled: reduced opacity + `cursor:not-allowed`.
- [H] Loading buttons: disable and show spinner during async; prevent double submit.
- [H] Errors near the field with `aria-invalid`, `aria-describedby`, `role="alert"`; success feedback via toast/check.
- [H] Confirm destructive actions (alertdialog with Cancel / Delete) or offer undo.
- [M] Buttons use verbs ("Book a table"), not "Submit".

## Accessibility
- [H] Text contrast >= 4.5:1 (large text/UI 3:1). Avoid: gray-400 on white.
- [H] Do not convey meaning by color alone: add icon/text.
- [H] Images: meaningful `alt`; decorative `alt=""`; icon-only buttons need `aria-label`; decorative SVG `aria-hidden`.
- [M] Sequential headings h1-h6, one h1. Semantic HTML (`nav main article`), not div soup.
- [H] All functionality via keyboard; tab order matches visual order; no clickable `<div>`.
- [H] Labels via `<label for>`; errors announced with `aria-live`/`role=alert`.
- [M] Skip link on nav-heavy pages.
- [H] Drag-only interactions need a single-pointer alternative (buttons, arrows).
- [H] Respect motion sensitivity.

## Forms
- [H] Visible labels above/beside inputs; placeholder is not a label.
- [M] Error under each field; validate on blur; mark required (`*` or "(required)").
- [M] Correct `type` (email, tel, number, url), `autocomplete`, `inputmode` on mobile.
- [M] Password show/hide toggle; inputs look interactive (border/background).
- [H] Submit shows loading then success/error state.

## Responsive
- [M] Mobile-first; test 320/375/414/768/1024/1440.
- [H] Touch-sized targets on mobile; body text >= 16px; inputs >= 16px (no iOS zoom).
- [H] `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`.
- [H] No horizontal scroll; images `max-width:100%; height:auto`; tables in `overflow-x:auto` wrappers or card layout.

## Typography
- [M] Line-height 1.5-1.75; 65-75 characters per line; modular scale (12/14/16/18/24/32); fallback font similar to webfont; clear heading vs body difference.

## Performance
- [H] Responsive images (`srcset`, WebP/AVIF, correct size); `loading="lazy"` below fold.
- [M] `font-display:swap`; third-party scripts `async/defer`; split code by route; monitor bundle; inline critical CSS; cache headers.
- [M] Blur-up image placeholders; skeleton shimmer matching content layout.
- [M] No autoplay heavy video (click-to-play, preload none); compress 3D/image assets.

## Feedback and content
- [H] Spinner/skeleton for operations >300ms. [M] Empty states explain + give an action; error recovery gives next step; progress steps ("Step 2 of 4"); toasts auto-dismiss 3-5s.
- [M] Truncate with ellipsis + expand; [L] relative or locale dates, formatted numbers, realistic placeholder data (no lorem ipsum).
- [M] Onboarding is skippable. Search: autocomplete, helpful "no results" with suggestions. Bulk actions for lists [L].

## AI and chat interfaces
- [H] Label AI-generated content; never present AI as a human. [M] Stream responses token by token; show confidence when relevant; progressive disclosure for advanced AI options; expectation-setting copy (what it can/cannot do); retry + alternatives on error; graceful non-AI fallback; thumbs up/down or regenerate [L].
- [H] Chat threads: distinct bubbles for user vs assistant; `aria-label` for who spoke.
- [H] Voice UI needs visual fallback (multimodal).

## Dashboards
- [H] KPI hierarchy: most important metric largest, top-left. [H] Chart by data story (line trend, bar comparison, donut 2-4 parts only). [M] Persist filters in URL/localStorage. [M] Real-time presence: show collaborators' cursors/avatars.

## Spatial / sustainability
- Gaze hover and depth (visionOS): respond to look before pinch; glass material + z-offset. Sustainability: avoid autoplay video, compress assets.

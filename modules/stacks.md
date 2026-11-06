# Stack defaults

If the user names no stack, deliver one self-contained `index.html` (HTML + CSS variables + minimal vanilla JS; Tailwind via CDN only if asked). Otherwise follow these defaults.

- **HTML + Tailwind**: mobile-first utilities (`md:` `lg:`), `max-w-6xl mx-auto px-4`, design tokens via CSS variables or Tailwind theme, `focus-visible:ring-2`, `motion-safe:`/`motion-reduce:` variants, `min-h-dvh`.
- **React / Next.js**: function components, tokens in CSS variables or Tailwind theme, `next/image` with width/height and `priority` for hero only, `next/font` for fonts, server components by default, `Link viewTransition` optional, no `useEffect` for data that can be fetched on the server.
- **Vue / Nuxt**: `<script setup>`, composables for shared state, `NuxtImg`, scoped CSS with variables; Nuxt UI for components.
- **Svelte / SvelteKit**: runes or stores, `transition:` directives respect reduced motion, scoped styles.
- **Astro**: ship zero JS by default, islands (`client:visible`) only for interactive parts.
- **shadcn/ui**: use its tokens (`--background`, `--foreground`, `--primary`, `--ring`, `--radius`), compose variants, keep Radix accessibility.
- **Angular / Laravel (Blade, Livewire)**: component templates with semantic HTML, server-side validation messages shown next to fields.
- **Mobile (SwiftUI, Jetpack Compose, React Native, Flutter)**: follow platform guidelines (HIG / Material 3), 44pt/48dp targets, Dynamic Type and font scaling, safe areas, system dark mode, native gestures, haptics sparingly.
- **Three.js**: lazy-load, cap pixel ratio, pause when offscreen, always provide a non-3D fallback and reduced-motion state.
- **Desktop (WPF, WinUI 3, JavaFX, Avalonia)**: density-appropriate tables, keyboard shortcuts, high-contrast themes, resource dictionaries / CSS for tokens.

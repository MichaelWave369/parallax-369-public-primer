# Accessibility Review Receipt — v0.2 Candidate

**Scope:** GitHub Pages site, public Markdown guides, templates, and synthetic examples  
**Review type:** Manual structural and source review  
**Status:** Candidate review complete; not a certification or substitute for user testing

## Review boundaries

This review evaluates the public artifacts visible in this repository. It does not evaluate GitHub's interface, browser extensions, third-party Markdown renderers, or private Parallax systems.

## Checks performed

### Document structure

- The site uses a single primary `main` region.
- Sections use descriptive headings in a logical hierarchy.
- The page provides a keyboard-focusable skip link.
- Links use descriptive labels rather than raw URLs as their only accessible name.
- Markdown templates use headings and lists rather than layout-only tables.

### Keyboard operation

- The stage explorer uses the tab and tabpanel pattern.
- Left Arrow, Right Arrow, Home, and End move among stage tabs.
- Focus is visibly indicated with a high-contrast outline.
- Core content and repository links remain reachable without pointer input.

### Motion and display

- The stylesheet honors `prefers-reduced-motion` by reducing animation and transition duration.
- Text reflows into single-column layouts at narrow viewport widths.
- Essential meaning is not communicated by color alone; stage numbers, headings, labels, and status words accompany color.
- The site uses system fonts and does not depend on externally loaded typography.

### Content clarity

- Stage names are paired with action verbs: Specify, Build, Prove.
- Status terms are written in text rather than represented only by symbols.
- Claims are scoped and the site distinguishes educational material from certification.
- The glossary added in v0.2 defines recurring governance and receipt terms.

### Printable artifact

- v0.2 adds a one-page printable primer with semantic HTML and a print-specific stylesheet.
- Decorative elements are removed in print.
- Links remain readable as text and the document does not require JavaScript to understand.

## Findings

### A11Y-001 — Interactive stage content depends on JavaScript

**Severity:** Low  
**Observation:** The visual stage explorer uses JavaScript to switch tab panels. The repository's stage guides and resource links provide equivalent complete content outside the explorer.  
**Disposition:** Accepted with mitigation. The explorer is an enhancement, not the sole location of the method.

### A11Y-002 — Mobile header navigation is visually hidden

**Severity:** Low  
**Observation:** At smaller widths, the compact header hides the anchor navigation to preserve layout. The page remains linearly scrollable and the repository button remains visible.  
**Disposition:** Accepted for v0.2. A future compact menu may improve discoverability but is not required to access content.

### A11Y-003 — Contrast requires rendered-environment verification

**Severity:** Medium  
**Observation:** Source review indicates strong foreground/background separation, but exact contrast can vary with transparency, display settings, and browser rendering.  
**Disposition:** Needs user testing. Public feedback requests should identify the page, display mode, and affected text.

### A11Y-004 — Markdown accessibility varies by renderer

**Severity:** Informational  
**Observation:** The source documents use conventional headings and lists, but final rendering is controlled by GitHub or another downstream renderer.  
**Disposition:** Documented limitation.

## Release recommendation

**Proceed as a v0.2 public candidate** with the findings above preserved. Do not describe this review as WCAG certification, comprehensive assistive-technology validation, or proof that no accessibility barriers remain.

## Future evidence requested

- keyboard-only review in at least two desktop browsers;
- screen-reader review of the landing page and printable primer;
- zoom and reflow review at 200% and 400%;
- contrast sampling of muted text and translucent panels;
- feedback from people using the templates in real workflows.

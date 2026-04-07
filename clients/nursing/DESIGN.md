# Design System Document: The Precision-Care Framework

## 1. Overview & Creative North Star: "The Clinical Architect"
The Creative North Star for this design system is **"The Clinical Architect."** In a field defined by both rigorous technical data and profound human empathy, this system rejects the "standard portfolio" look in favor of an editorial, high-end medical journal aesthetic. 

We break the "template" look through **intentional asymmetry**—offsetting technical headers against wide-margin body text—and **tonal layering**. The goal is to move away from rigid, boxed-in layouts and toward a breathable, fluid experience that feels like a premium digital consultation. We utilize "white space" as a functional component, representing the clarity and calm a professional nurse brings to a high-pressure environment.

---

## 2. Colors: Tonal Depth & Signature Textures
Our palette is rooted in medical authority but softened by empathetic accents. We avoid the harshness of pure black and white.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to define sections. Sectioning must be achieved through background shifts. For example, a `surface-container-low` section should sit directly against the `surface` background. This creates a modern, seamless transition that feels "built" rather than "drawn."

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers, like stacked sheets of frosted glass.
*   **Base:** `surface` (#f8f9ff) – The expansive, clean clinic floor.
*   **Level 1:** `surface-container-low` (#f2f3f9) – For large content blocks.
*   **Level 2:** `surface-container-lowest` (#ffffff) – Used for high-priority cards or "hero" insights to create a soft, natural lift.

### The "Glass & Gradient" Rule
To elevate the "Clinical Clean" aesthetic, main CTAs and Hero backgrounds should utilize a **Signature Gradient**. Transition from `primary` (#004370) to `primary-container` (#005b96) at a 135-degree angle. For floating overlays (like mobile navs or quick-glance vitals), use **Glassmorphism**: apply `surface_variant` at 70% opacity with a `24px` backdrop-blur.

---

## 3. Typography: Technical Precision vs. Human Narrative
The contrast between **Space Grotesk** and **Inter** represents the intersection of medical technology and patient care.

*   **Display (Space Grotesk):** Large, technical, and unapologetic. Use `display-lg` for numeric data or short, impactful impact statements. The mono-linear construction of Space Grotesk implies precision and "Clinical Clean."
*   **Headlines (Space Grotesk):** Use for section titles. Implement with generous letter-spacing (-0.02em) to maintain a high-end editorial feel.
*   **Body & Titles (Inter):** Inter is our "Humanity" font. It provides high legibility for long-form case studies. Use `body-lg` for narrative descriptions to ensure the reader feels the empathy in the text.
*   **Labels (Inter):** Small-caps or heavy weights should be used for data labels (e.g., "CERTIFICATIONS" or "BLOOD PRESSURE") to provide a "technical chart" aesthetic.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows and borders create visual noise. We achieve depth through **Ambient Light Physics**.

*   **The Layering Principle:** Instead of a shadow, place a `surface-container-lowest` card inside a `surface-container-high` wrapper. The shift in tone provides all the "lift" needed.
*   **Ambient Shadows:** If an element must "float" (e.g., a floating action button), use a diffused shadow: `box-shadow: 0 12px 32px rgba(25, 28, 32, 0.06);`. The shadow color is derived from `on-surface` (#191c20), not black.
*   **The Ghost Border Fallback:** For accessibility in form fields, use a "Ghost Border": `outline-variant` (#c1c7d1) at **20% opacity**. It should be felt, not seen.

---

## 5. Components
Each component must feel like a specialized medical instrument: precise, refined, and purposeful.

### Buttons (The "Surgical" Interaction)
*   **Primary:** A gradient fill (`primary` to `primary-container`) with `rounded-md` (0.375rem). No border. White text.
*   **Secondary:** `surface-container-highest` background with `on-primary-fixed-variant` text.
*   **Tertiary:** No background. Underlined with a 2px `secondary` stroke that appears only on hover.

### Cards & Lists (The "Non-Linear" Layout)
*   **Forbid Divider Lines:** Use `1.5rem` to `2rem` of vertical white space to separate list items. 
*   **Portfolio Cards:** Use `surface-container-lowest` with a `rounded-lg` (0.5rem) corner. The header should use a `secondary-fixed` (#8ef4e9) accent tab to denote "active" or "specialized" status.

### Input Fields & Checkboxes
*   **Inputs:** Use `surface-container-low` with a bottom-only "Ghost Border." Focus states shift the background to `surface-container-highest` and the border to 100% opacity `primary`.
*   **Checkboxes:** Use `rounded-sm` (0.125rem). The "checked" state uses `secondary` (#006a63) to signify health and empathy.

### Specialty Component: The "Vital Metric" Chip
*   A specialized chip for displaying certifications or key stats. Background: `secondary-container` (#8bf1e6) at 40% opacity. Text: `on-secondary-container` (#006f67). This creates a "soft glow" effect reminiscent of high-end medical monitors.

---

## 6. Do’s and Don’ts

### Do:
*   **Do** use asymmetrical layouts. Place a technical headline on the far left and the body text in a narrow, readable column on the right.
*   **Do** use `tertiary` (#663300) sparingly for "Warning" or "High-Alert" information in clinical case studies—it provides a sophisticated alternative to "emergency red."
*   **Do** prioritize `body-lg` for storytelling. Professionalism is conveyed through the quality of the narrative.

### Don't:
*   **Don't** use 100% black text. Use `on-surface` (#191c20) to maintain a soft, premium feel.
*   **Don't** use "Drop Shadows" on cards. Use tonal shifts or the "Ghost Border" fallback.
*   **Don't** clutter the grid. If in doubt, increase the spacing by one tier on the scale. High-end design requires room to breathe.
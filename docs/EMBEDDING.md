# Embedding Atypix on a website

This guide describes the HTML exported by both Atypix editions in the current repository version, reviewed on 17 October 2026. For the editing interface, see the [instruction manual and FAQ](ATYPIX-MANUAL.md).

## The two short answers

**To move all the lettering together, put the complete export inside your own outer wrapper and animate that wrapper.** Atypix then controls the lettering inside it, while your website controls where the complete composition goes. If only whole-block movement is needed, put a static SVG in the wrapper instead.

**When in view uses IntersectionObserver on the generated `.atypix` container.** The browser reports intersection with the viewport, taking relevant clipping into account. The current runtime configures a 25% threshold but checks `isIntersecting` to start: it is not a strict “at least 25% visible” gate. Loop and Ping-pong pause out of intersection and resume on return. Once does not automatically restart on each visit.

## Contents

- [Choose the right asset](#choose-the-right-asset)
- [What the snippet contains](#what-the-snippet-contains)
- [Animate the whole artwork as one block](#animate-the-whole-artwork-as-one-block)
- [Coordinate wrapper movement and lettering playback](#coordinate-wrapper-movement-and-lettering-playback)
- [How When in view works](#how-when-in-view-works)
- [A strict custom viewport trigger](#a-strict-custom-viewport-trigger)
- [Advanced timeline control](#advanced-timeline-control)
- [Responsive sizing and clipping](#responsive-sizing-and-clipping)
- [Multiple snippets and library loading](#multiple-snippets-and-library-loading)
- [CMS, website builders, and dynamic insertion](#cms-website-builders-and-dynamic-insertion)
- [Accessibility and reduced motion](#accessibility-and-reduced-motion)
- [Deployment checks](#deployment-checks)

## Choose the right asset

| Requirement | Suggested approach |
| --- | --- |
| Still lettering on a page | Export SVG; use an image element |
| Whole word slides in, no internal animation | Static SVG inside a motion wrapper |
| Letters draw, pop, or extrude independently | Full animated HTML snippet |
| Internal lettering plus whole-title movement | Full snippet inside a motion wrapper |
| Editable design backup | Save JSON separately |
| Video or GIF | Separate recording/rendering workflow |

A static SVG avoids running a lettering timeline when the website only needs to translate or fade a finished graphic. A CSS or Web Animations entrance can move that image just as easily as a live snippet.

## What the snippet contains

A complete animated export has three essential pieces:

1. Layered SVG artwork inside a generated `<div class="atypix" id="…">`.
2. A script loading GSAP from the configured CDN.
3. An inline script containing the lettering runtime and a call using the exported motion settings.

The generated root has a relative positioning context, isolated stacking, and an aspect ratio matching the composition. Its internal SVG layers supply the actual artwork. The export contains paths, so the website does not have to load the editor's font catalog, font files, opentype.js, or Paper.js.

The runtime initializes a GSAP timeline. Its initialization function is scoped inside the exported script rather than installed as a convenient page-global API. The normal snippet does not expose a named global player controller.

**Copy settings** is different: those settings alone do not provide the artwork, GSAP, or runtime. For a first embed, copy or download the complete animated HTML.

## Animate the whole artwork as one block

### Use an outer motion wrapper

Use three levels if you need a clipping stage:

```html
<section class="lettering-stage" aria-labelledby="campaign-heading">
  <h1 id="campaign-heading" class="visually-hidden">Make something move</h1>

  <div id="campaign-motion" class="lettering-motion" aria-hidden="true">
    <!-- Paste the COMPLETE freshly exported Atypix HTML here. -->
    <!-- Keep its generated .atypix root, SVG markup, and scripts intact. -->
  </div>
</section>
```

```css
.lettering-stage {
  position: relative;
  overflow: hidden;
  padding: 2rem 0;
}

.lettering-motion {
  width: min(100%, 70rem);
  margin-inline: auto;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
```

The semantic heading supplies the meaningful page text. The artwork wrapper is decorative in this example, so it is hidden from assistive technology to avoid a duplicate announcement. Use the actual wording of your artwork. If the artwork should be announced instead, give it one deliberate accessible label and avoid also announcing duplicate equivalent text.

`overflow: hidden` deliberately clips the moving artwork at the stage boundary. Remove it if the design should travel visibly outside that stage. Allow enough padding for decorative edges and shadows.

Animate `#campaign-motion`, not Atypix's internal `.letter` elements or SVG paths. Internal transforms belong to the lettering animation. The generated root's opacity is also used for the Loop reset fade, so the outer wrapper is the safer place for your host-page translation and opacity.

### Option A: CSS entrance

Add this to the wrapper styles:

```css
.lettering-motion {
  animation: lettering-enter 800ms cubic-bezier(.2, .7, .2, 1) both;
}

@keyframes lettering-enter {
  from { transform: translateX(-110vw); opacity: 0; }
  to   { transform: translateX(0); opacity: 1; }
}

@media (prefers-reduced-motion: reduce) {
  .lettering-motion { animation: none; }
}
```

This entrance starts when the CSS animation is applied. It does not wait for Atypix's own timeline to finish. The reduced-motion rule only removes the outer movement; it does not stop the lettering runtime inside. For a complete reduced-motion alternative, use the strategy later in this guide.

Viewport units move relative to the viewport. By comparison, `translateX(-100%)` moves relative to the wrapper's own width and does not necessarily put a small centered block completely off screen.

### Option B: JavaScript entrance and exit

The Web Animations API can move the wrapper without depending on GSAP. Place this script after the wrapper exists:

```html
<script>
  const letteringWrapper = document.getElementById('campaign-motion');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let wrapperAnimation;

  function enterLetteringBlock() {
    wrapperAnimation?.cancel();
    wrapperAnimation = letteringWrapper.animate(
      [
        { transform: 'translateX(-110vw)', opacity: 0 },
        { transform: 'translateX(0)', opacity: 1 }
      ],
      {
        duration: reducedMotion.matches ? 0 : 800,
        easing: 'cubic-bezier(.2, .7, .2, 1)',
        fill: 'both'
      }
    );
    return wrapperAnimation.finished;
  }

  function exitLetteringBlock() {
    wrapperAnimation?.cancel();
    wrapperAnimation = letteringWrapper.animate(
      [
        { transform: 'translateX(0)', opacity: 1 },
        { transform: 'translateX(110vw)', opacity: 0 }
      ],
      {
        duration: reducedMotion.matches ? 0 : 650,
        easing: 'ease-in',
        fill: 'both'
      }
    );
    return wrapperAnimation.finished;
  }

  // Call these from your site's buttons, slideshow, or page transitions.
  // enterLetteringBlock();
  // exitLetteringBlock();
</script>
```

These functions animate the complete composition. They do not restart or reverse the internal lettering timeline. The exit assumes the entrance has finished and the wrapper is at its neutral position; for interruptible gestures, use the current computed state as your starting frame instead.

The functions return completion promises. If your application cancels an animation while awaiting its completion, handle that rejected promise as part of its transition lifecycle.

### Option C: Existing GSAP page choreography

If your website already uses GSAP, place wrapper movement in its own timeline:

```js
// Run after GSAP and the wrapper have loaded.
const scene = gsap.timeline();
scene.fromTo(
  '#campaign-motion',
  { x: '-110vw', opacity: 0 },
  { x: 0, opacity: 1, duration: 0.8, ease: 'power2.out' }
);
// Add a later exit wherever your page sequence needs it:
scene.to('#campaign-motion', {
  x: '110vw', opacity: 0, duration: 0.65, ease: 'power2.in'
}, '+=3');
```

This still controls only the wrapper. Three seconds in this example is a chosen host-page delay, not a measurement of the exported lettering's duration. Do not treat it as automatic synchronization with every possible Atypix design.

## Coordinate wrapper movement and lettering playback

There are several valid timing choices:

### Both begin during page initialization

Use Atypix **On load** and begin the wrapper entrance at roughly the same stage of page setup. The letters may animate while the wrapper is still off screen. That can be intentional, but it can also mean the visitor misses the beginning.

### Letters begin as the moving artwork reaches the viewport

Use Atypix **When in view**. The observer watches the generated inner root. Moving an ancestor changes the root's geometric location, so wrapper motion can cause intersection and start the lettering.

An opacity-only wrapper fade does not reliably postpone this start. The artwork can geometrically intersect while transparent. Likewise, an overlay covering the artwork is not a dependable start gate.

### The wrapper arrives, then letters begin

This requires explicit coordination rather than assuming that On load means “after my website entrance.” Delay the runtime initialization until the wrapper entrance completes, or use the advanced editor controller described below.

With a full custom integration, keep a stable outer stage as the trigger, run the wrapper entrance, and only then initialize or play the lettering. Do not create a dependency in which the wrapper waits for lettering completion while lettering waits for an off-screen wrapper to enter view.

For an SVG that only needs whole-block motion, none of these internal timeline decisions are necessary.

## How When in view works

### What is being observed?

The runtime observes the **generated `.atypix` root element**, which contains the complete artwork. It does not observe each word or individual letter separately. It also does not automatically observe your outer page section.

There is no custom observer root, so the browser uses its viewport as the reference. There is no expanded root margin. Relevant ancestor clipping and scrolling affect the reported intersection. The dimensions refer to the container's layout box, not a pixel-by-pixel test of painted letter shapes.

### The current start logic

Conceptually, both exported runtimes do this:

```js
const observer = new IntersectionObserver(([entry]) => {
  seen = entry.isIntersecting;
  if (seen) {
    // Play if initialization is ready and autoplay still owns playback.
  } else {
    // Apply the runtime's once/loop off-screen behavior.
  }
}, { threshold: 0.25 });

observer.observe(artworkRoot);
```

The `0.25` threshold asks the browser for notifications around quarter-visibility crossings. However, the callback uses **`entry.isIntersecting`**, not **`entry.intersectionRatio >= 0.25`**, as its start condition.

That difference matters. IntersectionObserver sends an initial observation, and an element can be intersecting with less than a quarter visible. Consequently, if the browser reports that partial observation as intersecting, the runtime accepts it without another ratio check. Browser behavior around these boundaries can differ; do not promise a strict 25% start in page choreography. A precise ratio requirement needs an explicit ratio check, as shown below.

### Initialization readiness

The runtime waits through two `requestAnimationFrame` callbacks before allowing automatic playback. This gives its initial layer setup time to paint. For When in view, both initialization readiness and the intersection condition must be satisfied.

The option called On load refers to this runtime startup process. It is not a listener guaranteeing that every image, font, third-party widget, or asynchronous component elsewhere on the host page has finished.

### Off-screen behavior by playback mode

| Playback mode | Starts while initially outside intersection? | After starting, then leaving intersection | On return |
| --- | --- | --- | --- |
| Once + When in view | Waits | Does not automatically pause; observer can disconnect | No automatic replay |
| Loop + When in view | Waits | Pauses runtime-owned playback | Resumes from its position |
| Ping-pong + When in view | Waits | Pauses runtime-owned playback | Resumes, including its current direction |
| On load | Does not wait for intersection | No intersection-based pause | No intersection-based restart |

The runtime distinguishes its own automatic pause from a caller's manual pause. Do not expect re-entering the viewport to override every deliberate pause made by a custom integration.

Browsers can throttle animation frames in background tabs. That is separate from Atypix deliberately handling intersection; the export does not implement a general page-visibility lifecycle for every host situation.

### What “visible” does not mean

Intersection is geometric. It does not reliably establish that:

- The wrapper's opacity is greater than zero.
- An overlay or sticky element is not covering the lettering.
- The user is paying attention or has read the text.
- The lettering has sufficient contrast.
- A hidden carousel slide should be considered the active slide.

A root with no usable layout, a `display: none` ancestor, or a badly sized container cannot provide the normal expected trigger. CSS transforms can alter its observed position. For carousels, menus, route transitions, and other application state, use the application's own lifecycle when geometry alone does not match the intended behavior.

### Unsupported browsers

If IntersectionObserver is unavailable, the runtime falls back to starting after initialization. It does not keep the artwork waiting forever for an observer API that does not exist.

### Scroll containers and iframes

The default root is the browser viewport, with ancestor clipping affecting intersection. It is not a custom trigger relative to an arbitrary application panel. If you need a particular scroll container as the reference, provide your own observer with that container as `root`.

Inside an iframe, the runtime executes in the iframe's browsing context. The browser handles its intersection rules and ancestor clipping; the snippet does not install a custom parent-page scroll protocol. For precise parent-controlled choreography, observe the iframe or stable stage in the parent and communicate intentionally. Cross-origin parent/child code cannot simply access each other's DOM; use a deliberately designed `postMessage` integration with origin validation where needed.

## A strict custom viewport trigger

For a precise “start once when at least 25% of this stable stage intersects” rule, explicitly check the ratio. This is an **advanced replacement for the final initialization call**, not an extra script pasted after an already-running snippet.

Keep the generated artwork, GSAP loading, runtime function, and complete exported settings. Inside the same exported script scope, replace its final `animateLettering(...)` invocation with this pattern. Replace the example ID and `exportedSettings` variable with the exact generated root ID and complete settings object from your export:

```js
const artworkRoot = document.getElementById('YOUR-GENERATED-ATYPIX-ID');
const stage = document.getElementById('campaign-stage');
const exportedSettings = /* paste the complete exported settings object here */ {};
let hasStarted = false;

function startLettering() {
  if (hasStarted) return;
  hasStarted = true;
  animateLettering(artworkRoot, {
    ...exportedSettings,
    whenVisible: false
  });
}

if ('IntersectionObserver' in window) {
  const watcher = new IntersectionObserver(entries => {
    const ready = entries.some(entry =>
      entry.target === stage &&
      entry.isIntersecting &&
      entry.intersectionRatio >= 0.25
    );
    if (ready) {
      watcher.disconnect();
      startLettering();
    }
  }, { threshold: [0, 0.25] });
  watcher.observe(stage);
} else {
  startLettering();
}
```

Give the stable outer element `id="campaign-stage"`. Observe that stage rather than an inner wrapper that starts translated off screen, if the page section should initiate the entrance.

This pattern delays runtime initialization itself. It works without relying on the editor-only manual option. It starts once; it does **not** reproduce the built-in looping pause/resume behavior because it intentionally disables the runtime's own visibility observer. Add a deliberate lifecycle if your integration needs both strict triggering and later pause/resume.

A very tall target might never reach a 25% intersection ratio on a small viewport. Choose a sensibly sized stage or a different threshold for your layout.

If an outer entrance must complete first, call `startLettering()` from that entrance's completion handler instead of immediately inside the observer. The stage observer can initiate the outer entrance, then its completion can initialize the letters. Account for interrupted/canceled transitions in your website code.

## Advanced timeline control

The normal export runs an initialization call inside a function scope and discards the returned timeline. There is no documented universal `window.atypix.play()` command available after pasting it.

For custom control, edit the final call inside that same script scope. **The following manual-start pattern applies to current exports from both pages**, which now share the timeline-editor runtime. Older exports made before this replacement may not implement the same `manual` option or `cancelAutoplay` helper.

```js
const artworkRoot = document.getElementById('YOUR-GENERATED-ATYPIX-ID');
const exportedSettings = /* complete settings copied from this export */ {};
const letteringTimeline = animateLettering(artworkRoot, {
  ...exportedSettings,
  whenVisible: false,
  manual: true
});
letteringTimeline.cancelAutoplay();

// Expose only if your host application needs an external handle.
window.campaignLettering = letteringTimeline;
```

Your host can then intentionally call `play()`, `pause()`, or `restart()` on that GSAP timeline. Choose the method based on the desired behavior: play resumes; restart starts again. Keep the wrapper's separate animation independent unless you are deliberately building a coordinated master sequence.

Cancel automatic ownership before controlling the timeline yourself. Simply calling `pause()` immediately after initialization is not a universal way to stop an original-edition export's delayed autoplay.

For a page transition where the wrapper arrives before letters play, a custom editor integration can wait for the wrapper animation's completion and then call `letteringTimeline.play(0)`. A manual entrance can leave the initial lettering invisible while waiting, so provide a static alternative when JavaScript or animation is unavailable.

If a single-page app removes the artwork, stop and release custom timelines and disconnect any observers your host created. Atypix's built-in observer notices a disconnected root when it receives a callback; this is not a substitute for an explicit lifecycle in a long-lived application.

## Responsive sizing and clipping

Let the generated aspect-ratio root size naturally inside a width-controlled wrapper. Set the desired maximum width on your own wrapper. Avoid fixed heights that squeeze or crop a composition with a different aspect ratio.

```css
.my-lettering-slot {
  width: min(100%, 56rem);
  margin-inline: auto;
}
```

Do not apply broad site rules such as `svg { height: 100vh; }` to the export. Scope website SVG styling so Atypix's layered SVG geometry keeps its intended dimensions. Likewise, avoid generic transforms on every nested `div`.

Test at desktop, tablet, and phone widths. The letters scale as artwork; the exported words do not reflow into a new typographic line break like ordinary HTML text. If a mobile layout needs a different composition, create and select a separate asset rather than expecting automatic text wrapping inside paths.

For a still image:

```html
<img
  src="/assets/campaign-lettering.svg"
  alt="Make something move"
  style="display:block;width:100%;height:auto"
>
```

Use an empty alt attribute instead when equivalent nearby accessible text already describes the artwork and it is decorative.

## Multiple snippets and library loading

Fresh exports generate root IDs and internal references for their own instance. Keep them intact. Duplicating one exact snippet several times can create duplicate IDs and interfere with gradients, masks, and element lookup. Generate a fresh snippet for each instance or deliberately rewrite **all** relevant IDs and references in a custom build process.

Each standard snippet includes a GSAP script reference. For an optimized page with several exports, load one compatible GSAP library through your website's dependency system and remove redundant script references from the snippets carefully. Ensure GSAP exists before any snippet initialization executes.

Do not just add `async` to the library reference: that can make the initialization run before the library is ready. A module/bundler or deferred script integration must explicitly preserve its dependency order.

Avoid globally styling every `.letter` class on your site without checking scope. For host styles, prefer selectors rooted in your own outer wrapper.

## CMS, website builders, and dynamic insertion

Use the host platform's supported HTML/embed and script mechanism. A rich-text field may escape or remove scripts. A builder's edit view may deliberately disable scripts even though the published page supports them, or vice versa. Verify the actual published output.

When JavaScript assigns a string to `innerHTML`, inserted script tags do not ordinarily execute. Treat loading an animated component as a real component lifecycle rather than assuming a string insertion starts every embedded script.

Sites with a Content Security Policy may need the library loaded through an approved source and the initialization script placed in an approved external file or given an appropriate nonce/hash. Adapt the integration to the site's policy rather than weakening it indiscriminately.

If self-hosting the library, keep a deliberate version and follow the dependency's applicable terms. The normal export uses GSAP 3.13.0; test compatibility when consolidating it with a different site version.

For iframe embeds, host the exported content as an actual page or supported iframe document. An HTML fragment is not an image source. Give the iframe an accessible title and correct sizing. Parent-page wrapper motion can move the entire iframe, but coordinating its internal timeline requires explicit integration.

## Accessibility and reduced motion

### Preserve meaningful text

Outlined lettering is visual artwork. Important headings should have a deliberate accessible representation in the host document. The wrapper example uses a visually hidden heading and marks the artwork decorative. Do not accidentally announce both that heading and several repeated SVG labels.

If the artwork itself is the single meaningful image, use an appropriate label instead. Choose one clear strategy for the context. Use real headings and ordinary text for information that must remain selectable, responsive, and easy to translate.

### Reduced-motion behavior is a host responsibility today

The current exported lettering runtime does not automatically replace itself with a still design when `prefers-reduced-motion` is enabled. A CSS rule that disables your wrapper entrance only addresses that outer motion.

A robust integration provides a static SVG alternative and initializes the animated snippet only for the desired motion preference. Do not rely on `display: none` alone to stop an already initialized animation, and do not pause an entrance at a frame where all its letters are hidden.

One component architecture is:

1. Render the static SVG by default.
2. Check `window.matchMedia('(prefers-reduced-motion: reduce)')` in the host.
3. Only load and initialize the animated markup/runtime when motion is permitted.
4. Replace or hide the static presentation once the animated component is ready.
5. If supporting preference changes while the page is open, stop the live player and restore the static presentation when the preference changes to reduce.

This requires a real host integration, not merely a CSS media query around an already-running snippet. Keep the accessible text consistent in either presentation.

Long-running loops may also need user-facing pause controls according to the page's requirements. A custom controller can supply them; a decorative animation should not make it hard to read adjacent content.

## Deployment checks

Before publishing:

- Verify the complete snippet was used and its generated IDs remain intact.
- Confirm GSAP loads before initialization and that the host permits script execution.
- Test the actual published page through a full playback cycle.
- Test a below-the-fold placement with the intended start option.
- Test leaving and re-entering the viewport in Once and in the chosen repeating mode.
- Check wrapper movement separately from internal lettering motion.
- Inspect ancestor overflow, responsive width, and shadows at narrow sizes.
- Confirm reduced-motion and accessible-text behavior.
- Avoid assuming that opacity, overlays, or carousel state are equivalent to intersection.
- Keep the design JSON so wording or styling changes can be regenerated.

The editor creates the artwork and its internal sequence. Your website determines placement, page transitions, accessibility strategy, and application lifecycle. An outer motion wrapper is the clean boundary between those responsibilities.

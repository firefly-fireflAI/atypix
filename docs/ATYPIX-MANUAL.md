# Atypix instruction manual and FAQ

This manual describes the current repository version of Atypix, reviewed on 17 October 2026. It covers the original interface and the newer timeline editor. Controls can differ between those editions; differences are called out below. Saved designs and exported HTML are different deliverables, and this guide explains when to use each.

For website code and the detailed explanation of **On load / When in view**, read the companion [website embedding guide](EMBEDDING.md).

## Contents

1. [What Atypix makes](#what-atypix-makes)
2. [Your first design](#your-first-design)
3. [How settings relate to one another](#how-settings-relate-to-one-another)
4. [Navigating the workspace](#navigating-the-workspace)
5. [Text](#text)
6. [Font](#font)
7. [Style](#style)
8. [Detail](#detail)
9. [Letter](#letter)
10. [Color](#color)
11. [3D](#3d)
12. [Finish](#finish)
13. [Animation fundamentals](#animation-fundamentals)
14. [The original animation interface](#the-original-animation-interface)
15. [The timeline editor](#the-timeline-editor)
16. [Saving and restoring designs](#saving-and-restoring-designs)
17. [Exporting](#exporting)
18. [Practical recipes](#practical-recipes)
19. [Troubleshooting](#troubleshooting)
20. [Frequently asked questions](#frequently-asked-questions)
21. [Glossary](#glossary)
22. [Production checklist](#production-checklist)

## What Atypix makes

Atypix turns text into outlined letter shapes, applies decoration and dimensional effects, and builds animation from separate visual parts. The finished lettering is artwork rather than ordinary editable website text. Its appearance does not depend on a visitor having the source font installed.

You can make a single word, several lines, irregular hand-positioned lettering, a flat wordmark, dimensional display lettering, or a looping animated heading. Atypix works especially well for short, expressive display text. A paragraph containing many decorated characters creates much more geometry and animation work than a short title.

The principal deliverables are:

| Deliverable | Use it for | Editable as an Atypix design? | Animated? |
| --- | --- | --- | --- |
| Atypix design JSON | Backup, transfer, later editing | Yes | Stores animation settings |
| SVG | Scalable still artwork | No; keep the JSON too | No |
| PNG | Transparent still image | No | No |
| WebP | Browser-friendly still image | No | No |
| Animated HTML | Live lettering on a website | Not a replacement for JSON | Yes |
| Copied settings | Updating an existing runtime integration | Settings only | Requires existing artwork and runtime |

Atypix does not currently provide a built-in animated GIF or video export. Downloading PNG or WebP does not record the animation.

### Which edition should I open?

Use [Atypix](https://firefly-fireflai.github.io/atypix/Atypix.html) if you prefer the older animation controls. Use [Atypix editor](https://firefly-fireflai.github.io/atypix/Atypix-editor.html) for the timeline, shared versus per-line animation editing, scrubbing, and the newer part controls.

The lettering workflow is shared: Text, Font, Style, Detail, Letter, Color, 3D, Finish, and Save & export. The two pages remain separate while the newer animation interface develops. Do not assume a browser draft saved by one page will automatically appear in the other. Download JSON to move a design deliberately between pages.

## Your first design

1. Open either edition and choose a style preset as a starting point.
2. Open **Text** and replace the sample words. Adjust the size of each line and the gap between lines.
3. Click the line's font-name button, or open **Font**, select the correct line, and choose a font family.
4. Open **Color** and choose a palette. Make broad palette changes before spending time on individual letter colors.
5. Open **3D** and adjust extrusion depth and direction. Choose the shading treatment separately.
6. Open **Finish** and choose grain, grain color, edge character, and any drop shadow.
7. Click a letter to refine its size, rotation, position, face style, or effects in **Letter**.
8. Switch to **Animate**, choose an animation preset, and refine timing.
9. Download the **Atypix design JSON** before exporting artwork.
10. Export SVG or an image for a still asset, or animated HTML for a live website embed.

A preset is a complete starting design. Applying another style preset late in the process can replace more than the face treatment: it can change colors, layout, effects, animation, and, for stored example presets, the words themselves. Use Undo immediately if you were only experimenting.

For an efficient workflow, settle the words and general layout first, then the typeface, then global styling, then letter exceptions, and finally animation. Changing the words after carefully positioning individual letters can require reviewing those letter settings again.

## How settings relate to one another

There are three useful levels to keep in mind:

- **Whole design:** palette, shared finish, general extrusion, outline defaults, and playback behavior.
- **Line:** text, font, size, spacing, alignment, style cycle, and letter timing. The timeline editor can also give each line its own part animation settings.
- **Letter:** position, rotation, scale, face choice, colors, and supported effect overrides.

A letter normally inherits applicable settings. An override changes that letter while leaving other letters alone. A **Use global** choice means the letter continues following the global setting; it does not merely copy today's value. That distinction matters when you later adjust the whole design.

For example, if the global outline is 3 and one letter has an explicit width of 1, changing the global outline to 5 leaves that letter at 1. Restoring its global-width choice makes it follow 5. Setting an individual width to 0 removes its outline even while other letters retain theirs.

A face style, a style preset, and an animation preset are separate concepts. A face style determines the visual treatment of a letter. A style preset is a broader design starting point. An animation preset changes how the existing artwork moves or appears.

## Navigating the workspace

### Preview modes

**Still** displays the finished design for inspection. **Animate** previews the configured sequence. Use the replay controls to watch it again after a change. Selecting a letter for detailed editing can return the preview to Still so you can inspect and click the artwork reliably.

The preview background color helps you judge the artwork on a light, dark, or brand-colored surface. It is not automatically baked into exported artwork. The standard image and SVG exports have transparent surroundings.

The small swatch and eyedropper control change that preview background. Browser support determines whether an actual screen eyedropper is available; otherwise the native color chooser is used.

### Tabs and smaller screens

The main tabs organize the tools by task. At narrower widths, the section picker and control visibility controls help manage the workspace. Some control areas scroll: if a setting seems absent, check both the selected tab and the remaining content inside its panel.

The Letter effects tabs wrap when necessary. The font panel adapts from several columns to fewer columns and then a stacked layout. A narrower layout does not mean that a font has lost weights or styles.

### Numeric values

Sliders offer a quick visual adjustment. The displayed numeric values are editable where supported, which is useful for precise values or repeating a setting. Stay within the control's supported range. A number such as line size describes artwork geometry, not the final CSS width of a website embed.

### Undo, redo, and reset

Undo and Redo help compare changes and recover from an unwanted preset or color operation. History belongs to the current editing session and is limited; it is not a substitute for downloaded backups. Reset returns the design to its starting state. Save important work before using it.

## Text

The Text tab controls the words and the basic arrangement of lines. It is deliberately separate from font discovery, so typing and layout do not require navigating the font browser.

### Entering words and adding lines

Edit each line's text field. Add another line when you need a separate size, font, alignment, or animation start. Remove an unnecessary line rather than using a long sequence of spaces to imitate a gap.

Atypix lays out characters individually. Spaces affect the arrangement but do not become visible decorated letters. Avoid treating the input as a full desktop publishing text box with paragraph wrapping and advanced shaping.

### Size

Line size changes the base size of that line's glyphs. Individual letters can then scale relative to that base in the Letter tab. If an entire line should grow, use its line size; if only one letter needs emphasis, use that letter's scale.

The final export can be displayed at a different physical size. For example, an SVG made from a large working size can still be placed in a 400-pixel-wide container without losing the scalability of its path outlines.

### Letter spacing

Letter spacing adjusts the separation between characters. Negative spacing can bring letters together or create overlap. That can look effective with dimensional lettering, but inspect the face, extrusion, and shadow together: a depth direction can make overlapping letters feel different from a flat word.

Use letter position offsets for a specific awkward pair after establishing the overall spacing. Moving every letter individually to compensate for an unsuitable line-wide spacing value makes later editing harder.

### Alignment and leading

Choose left, center, or right alignment for each line. Leading controls the space between lines. Negative values can deliberately bring them closer or overlap them. Atypix's controls arrange artwork; the leading value should not be assumed to match a CSS `line-height` value in another application.

### Font-name buttons

The uppercase font-name button opens Font for that line. Its label is the family name; there is no extra “Change” prefix. This is a shortcut to the same font-selection tools available through the main Font tab.

## Font

### The two information boxes

The first box, **Font for this line**, selects which line you are editing and provides **Edit text**. The separate font box identifies the selected family and offers its available weight, style, favorite action, and font/license link.

Before selecting a family, confirm the line selector. Each line can use a different typeface. Choosing a new family for one line does not mean that every line now uses it.

### Finding a family

Search by family name. The views are:

- **Curated:** a small starting selection suited to expressive display lettering.
- **All fonts:** the wider generated Google Fonts catalog.
- **Recent:** families selected recently in this browser.
- **Favorites:** families you have marked for quick access.

Search filters the available family names. Results are shown in batches; use **Show more** when available. Selecting a family preserves the font-list scroll position so you can compare nearby choices without repeatedly returning to the top.

The result labels are interface text, not downloaded live specimens of every listed family. Only the selected font downloads. This keeps browsing from fetching thousands of fonts.

### Weights and styles

Available weights and styles depend on the family. A family with Regular only cannot supply a genuine Bold or Italic instance through those controls. Choose a family with the needed instance rather than expecting every option to exist everywhere.

Atypix resolves supported static TrueType instances for its outline parser. It is not an editor for arbitrary variable-font axes. Catalog presence is not a promise that every family, language, or glyph combination has been tested.

### Loading and failures

A selected font must download and parse before Atypix can build its outlines. If a request fails, check network access, browser privacy restrictions, and any blocker affecting font hosts. The current artwork is preserved when a replacement cannot load rather than silently replacing it with an unrelated family.

A saved family that is no longer available may need an explicit replacement. Keep the original JSON while experimenting. A warning about availability should not be interpreted as permission to overwrite your only backup.

### Missing characters and script limitations

A font can be valid but lack a particular character. Check any missing-glyph warning and choose a family containing the required glyphs.

The current engine positions individual characters and does not implement full connected-script shaping. Arabic and other scripts requiring contextual shaping, joining, or complex reordering may not render correctly even if the font contains the relevant characters. Combining marks and sophisticated typographic behavior also deserve careful inspection. Use another shaping-capable design tool when those requirements are essential.

### Fonts and licenses

Use **Font & license** to inspect the family's source and licensing information. Exported paths do not require the website visitor to download that font. Outlining the artwork does not remove the need to follow the applicable license when using or redistributing font files themselves.

Favorites and recent-family lists are browser conveniences. They are not an account-based collection synchronized between devices.

## Style

### Complete presets

The available design presets include Handletter, Riso, Candy Pop, Bugle, Jellybeans, Pow, Lollipop, Glass, Marquee, and Dropcap. Their purpose is to provide intentional combinations rather than a single isolated effect.

Try presets near the start of a design. Some preserve the current words while resetting layout and overrides; stored example designs can replace the words and arrangement too. Save JSON before applying a preset if you want a durable branch of your work.

### Face treatments

The face is the front of a letter. Treatments include inline, fill, dots, risograph, stripes, stars, teardrops, rope, Glass, plain, flat, and line art.

**Plain** removes face decoration while retaining the filled dimensional treatment. **Flat** removes extrusion for that letter. **Line art** uses an outline-based treatment rather than a filled dimensional face. Make sure an outline is present when using line art, or the result may appear to vanish.

A line's style cycle can alternate treatments across its letters. Individual Letter face choices override that cycle. A blank character does not consume a visible style-cycle step.

### Global outline

The Style outline controls establish the default width and pattern for all inheriting letters. Set width to **0** to remove the outline. Choose Solid, Dashed, or Dotted for a visible outline; the spacing controls determine the rhythm of patterned outlines.

There is no current Animation → Outline “None” option. Removing an outline is a design decision made with outline width, not an animation entrance choice. Once no relevant outline exists, its animation controls can disappear automatically.

## Detail

Detail refines the current face treatments. It is contextual: controls appear for decorations that exist in the design. Selecting a plain or flat treatment does not expose every decorative control just in case you might later use it.

The edge inset moves decoration inward from the boundary of a glyph. Use it to keep dots or patterns from crowding the edge. Inner-stroke thickness affects relevant inline or Glass details.

Dots have size and spacing controls. Risograph has dot size, spacing, and ink opacity. Stripes expose angle, width, and gap. Stars expose size, point count, and spacing. Teardrops expose size and spacing. Rope has angle, spacing, and thickness.

These controls can change the density of geometry significantly. Tiny, tightly spaced marks create a different visual texture and can cost more to preview or animate. Judge both the full-size design and the actual website display size: a lovely pattern at editing size can merge into visual noise in a small heading.

If you choose Dots as extrusion shading, the risograph-style detail controls also influence the dots, alongside the density control in 3D. Face decoration and extrusion shading are still separate visual layers.

## Letter

Select a letter from the selector or click it in the artwork. Confirm the selected letter before changing an override, particularly when the same character occurs several times.

### Position and face

Scale changes its size relative to the line. Rotation turns it. Horizontal and vertical offsets move it from its normal position. Start with small offsets, then inspect the word as a whole so local improvements do not accidentally damage spacing elsewhere.

The face selector displays the effective face treatment. A letter still follows the line's style cycle until you explicitly choose a replacement. **Reset face** restores that inheritance. **Reset letter** clears the letter's broader overrides, so use the narrower action when only the face should revert.

### Letter colors

The Letter colors section lets a character depart from the global palette. The palette controls appear above the effects tabs in document order, beside the basic letter settings when space permits. The visible result can combine per-letter colors with inherited geometry and motion.

### The seven effects tabs

Select a tab to show its settings underneath. The selected panel scrolls into view; reduced-motion preferences avoid the smooth scrolling transition. Keyboard users can move between tabs using the arrow keys and Home/End.

| Tab | What it changes |
| --- | --- |
| Letter outline | Width and pattern inheritance or overrides |
| Outline spacing | Dash length and gap for this letter |
| Letter 3D shadow | Shading treatment on the extrusion |
| Letter extrusion | Depth and direction |
| Letter animation | Timing offset |
| Letter drop shadow | Distance and opacity |
| Letter finish | Grain amount and edge wobble |

The divider above these tabs separates them from the earlier letter controls. A tab label is shown once; the selected settings do not need a repeated heading inside the panel.

### Outline and spacing

Keep global width enabled when the character should follow the design. Disable inheritance and set its own width for an exception. Width 0 removes that letter's outline. The pattern can likewise inherit or choose Solid, Dashed, or Dotted.

Dash length and gap describe the patterned outline, not the spacing between letters. Their appearance depends on the glyph's contours, so inspect curved and angular characters separately.

### 3D shadow versus drop shadow

**Letter 3D shadow** shades the extrusion itself. Its None option removes shading, not the dimensional side surface. **Letter drop shadow** concerns the shadow cast behind the artwork. These are intentionally different controls.

A global-shading reset restores the letter's connection to the global 3D shadow treatment. Letter drop distance and opacity override those aspects, while direction and softness remain global Finish settings.

### Extrusion, timing, and finish

Per-letter extrusion depth and direction let a character have its own dimensional treatment. A Flat face remains flat.

The animation timing offset shifts the selected letter's parts relative to the line's timing and stagger. A negative offset requests an earlier start, but playback still begins at timeline time zero; content scheduled before that boundary can already be underway at the start.

Letter finish overrides grain amount and wobble amount. Grain type, grain color, and the other global edge-character controls remain in Finish. Choosing global Grain None suppresses grain even if a letter retains a nonzero amount.

## Color

### Color roles

The palette assigns colors to specific parts of the lettering. The face and outline can each use a top and bottom color. Matching those pairs produces a solid color; different values produce a gradient.

Other swatches address decoration, dots, stripes, extrusion, the shaded underside, and drop shadow. A color can be configured without being visible: a drop-shadow color has nothing to color if drop distance or opacity is zero.

Use a temporary extreme color when learning which swatch controls a subtle layer, then Undo or restore the intended color. This is often easier than trying to distinguish two almost-identical dark colors in a complex preset.

### Palettes and letter exceptions

Start with a palette such as Tangerine, Candy, Sea glass, Cobalt club, Cherry cola, Monochrome, or Paper & ink, or use the available Rainbow and Risograph color modes. Monochrome describes a color approach, not a face style.

Changing the global palette clears letter color overrides so the palette can apply consistently. If you have carefully colored individual characters, save first or use Undo to recover after an experiment.

### Copying colors

Copy/Paste Color transfers a single color. Copy/Paste Swatches transfers a set. Copy to All Swatches deliberately makes multiple color roles identical. Copy to All Letters applies a complete color set across letters.

Choose the narrowest action that matches your intention. Making every swatch identical can remove the visual distinction between the face, side, and shading even though the geometry is still present.

## 3D

### Extrusion

Extrusion is the depth projecting from the face. Increase depth for a more dimensional block; reduce it for a restrained result. The direction determines which way the depth travels. In the artwork coordinate system, 0 degrees points right and 90 degrees points down.

Depth and direction also affect overlap. Two tightly spaced letters can cover one another differently when the extrusion points left instead of right. Check the complete word after changing direction, including during animation.

### Shading on the extrusion

Choose None, Hatching, Smooth, or Dots. None keeps the side surface while removing its shading treatment. Hatching adds directional marks, Smooth gives a continuous treatment, and Dots uses a dotted ink treatment rather than merely placing dots on top of a solid shaded area.

Hatching intensity and angle apply to Hatching. Dot density applies to Dots. If a control disappears after changing the shading style, it has become irrelevant to the selected treatment rather than being lost.

The shading direction is distinct from extrusion direction. It affects how the depth reads as lit and shaded. Adjust them together when trying to make several lines appear consistently illuminated.

## Finish

### Grain

Choose None, Speck, Fine dust, Coarse paper, or Grunge. Grain amount controls its strength. Grain color is configurable; it does not have to be white. Older designs without a stored grain color use the default warm light color.

Grunge produces clustered, multi-scale texture patches. It is an overlay treatment clipped to the lettering, not a destructive eraser that punches transparent holes through the letters. If you need true distressed cutouts for a print workflow, further vector or image editing may be necessary.

Grain None disables grain globally and makes its amount/color controls irrelevant. Choosing a very similar grain and face color can make the effect difficult to see even when enabled. Inspect a contrasting test color before assuming a texture failed.

### Edge character

Wobble changes the regularity of the outlines. Frequency affects the scale of the variation; jitter adds irregularity. Small changes can create a convincing hand-worked edge. Large values can noticeably distort small counters and fine details.

Texture should be judged at the final display size. Very fine grain can disappear or shimmer when scaled down, while heavy wobble can make a small word difficult to read.

### Drop shadow

Distance moves the shadow away from the artwork; direction sets its angle; softness blurs it; opacity sets its visibility. Distance or opacity at zero can eliminate the visible shadow. Use these controls for separation from a website background rather than extrusion shading.

Softness and multiple textured layers can increase rendering cost. A still image is an option when you need a highly complex appearance but do not need the lettering to animate independently.

## Animation fundamentals

### Parts

Atypix can animate Face, Outline, Extrusion, Drop shadow, and Decoration separately. Each part has a different job: the face supplies the front shape, the outline traces its edge, extrusion creates depth, drop shadow sits behind it, and decoration supplies the face pattern.

Only relevant parts are shown. If no outline exists, there is no useful outline animation panel. Turning an effect back on can restore its panel and retained settings. The editor also considers relevant animated start/end states when deciding whether a part exists.

Removing a part from the design is different from choosing how it enters. Use outline width to remove outlines and depth to remove extrusion. Hidden controls do not mean that their settings have been permanently deleted.

### Letter timing

Line start places a line in the overall sequence. Spread distributes letter starts across a period. Order determines which character starts first: for example, left to right, center outward, or random where offered. A per-letter timing offset provides a final exception.

A spread is not necessarily a delay added in full between every adjacent pair. Think of it as distributing the line's starts over a span. Compare the preview before increasing it by a large amount.

### Part timing and easing

Duration is how long an individual part transition takes. Starts/anchor choices determine what that timing is relative to. A short delay measured from a letter's face start is different from the same delay measured from its face end.

Easing changes how movement accelerates and settles. Linear is even. Other motion feels can accelerate, overshoot, bounce, or spring. Strength modifies the applicable feel. Use expressive easing selectively: applying strong bounce to every layer can make the structure harder to read.

### Once, Loop, and Ping-pong

| Mode | Behavior |
| --- | --- |
| Once | Plays the configured sequence once |
| Loop | Plays forward, holds, fades the complete artwork, resets, repeats |
| Ping-pong | Plays forward, holds, plays backward, holds, repeats |

Ping-pong reverses the actual configured sequence. A timeline playhead moving backward is expected. It is not a warning that the exported file will lose the return journey. The animated HTML export includes Ping-pong behavior.

Hold adds time at the turning points for Ping-pong. Speed scales playback, including the perceived hold time. A faster global speed makes both transitions and pauses feel shorter.

Reverse, where available in the editor, reverses the configured sequence itself. It is separate from Ping-pong, which repeatedly alternates direction, and separate from an extrusion transition that shrinks.

### Start: On load or When in view

On load starts after initialization and two animation-frame callbacks. It does not wait for every unrelated image or component on the host website to finish loading.

When in view uses the browser's IntersectionObserver on the generated artwork container. Looping playback pauses when the artwork leaves intersection and resumes when it returns. Once playback does not automatically restart on every visit.

The observer is configured with a 25% threshold, but the current start condition checks intersection itself rather than requiring a ratio of at least 25%. Therefore, do not rely on an exact quarter-visible start. The [embedding guide](EMBEDDING.md#how-when-in-view-works) explains this distinction, visibility limitations, and strict custom triggers.

### Performance

The performance indicator is a practical measurement on the current browser and device. It is not a guarantee for every visitor's phone. More characters, denser patterns, grain, wobble, blur, and animated geometry can increase work.

If playback becomes uneven, simplify one expensive ingredient at a time and replay. Test the exported artwork on a representative device too. An editing session and a deployed page have different surroundings, resources, and competing animation work.

## The original animation interface

The original Atypix page retains its older control arrangement. Animation preset buttons provide Draw in, Paint, Pop, Drop, and Soft fade starting points. Overall controls include speed, playback mode, hold, and start behavior.

Line controls set letter start, spread, and order. Compact groups configure the face entrance, decoration, outline, drop shadow, and extrusion. Choose an animation preset to establish coordinated timing, then change individual values deliberately.

This edition does not expose the newer timeline editor's full per-line part editing and transport interface. If you need independent part sequences for different lines, open the timeline editor and transfer the design with JSON.

## The timeline editor

### Presets and scope

Preset buttons sit at the top for quick comparison. The editor includes Draw in, Paint, Pop, Drop, Soft fade, Bloom, and Swing.

**Same for all lines** uses shared part settings. **Per line** lets the selected line have its own configuration. Check the scope before editing: changing a shared setting affects the shared sequence, while editing a selected line is more specific. Copy-to-other-lines controls are useful when one line should establish a common starting point.

### Timeline and transport

The line tracks show timing relationships. Play and Replay preview the configured motion. The scrubber lets you inspect a point in the sequence. Scrubbing pauses playback so that the selected frame can be examined.

A selected-line-only preview helps isolate a line while editing. It does not mean that the other lines have been deleted from the design or will necessarily disappear from the normal export.

Ping-pong makes the playhead travel backward during the return phase. Endpoint holds keep it stationary. Treat this as a representation of playback direction rather than as a second editable sequence.

### Controls beneath the timeline

Letter timing for the selected line and Playback settings applying to all lines appear directly beneath the timeline. The part tabs follow: Face, Outline, Extrusion, Drop shadow, and Decoration.

Select a part to show its compact settings beneath the tab row. Face is the default panel. Parts absent from the artwork are hidden. The selected panel shows its settings directly, without additional collapsed disclosure sections.

### Timing anchors

The Starts choices position a part with the letters, after the letters, at a specific time, or after other parts finish, as applicable. Custom Count from and Offset controls refine those relationships.

Before changing an offset, identify its anchor. “After face ends, minus a small offset” creates overlap. “After face starts, plus the same offset” produces a different sequence. If everything seems unexpectedly late, inspect anchors before making all durations shorter.

### Animated extrusion and drop-shadow states

The editor can specify extrusion start/end depth and direction, and supported drop-shadow start/end properties. **Match current design** keeps an endpoint connected to the static design rather than copying an arbitrary number.

These controls animate an effect's state. They do not necessarily redefine the final Still artwork. Static exports show the design's still representation rather than a recording of the current scrubber frame.

### Reverse and combined motion

Reverse applies according to the selected editing scope. In per-line editing, inspect the selected line before using it. Combining Reverse with Ping-pong can deliberately start with the opposite journey and then return, but a simple forward sequence is usually easier to debug first.

## Saving and restoring designs

### Download JSON as your master

Use **Download Atypix Design JSON** in Save & export. This file stores editable design settings, words, fonts, colors, per-letter changes, and animation settings. Keep it alongside the assets you deliver.

A useful naming scheme includes the project, variation, and revision: `spring-heading-cobalt-v03.json`. Save a new version before a large preset, palette, or layout experiment. A filename describes your own organization; it does not change the design format.

### Load JSON

Use the load control to open a previously downloaded design. Wait for fonts to load before judging the result. If a family is unavailable, resolve that warning explicitly.

Loading a design replaces the current working design. Save the current one first if you need both. A JSON file is design data; do not paste it into a website expecting an animated heading to appear.

### Browser drafts

Atypix saves a local browser draft after edits. This helps recover normal local work but is not a durable backup service. Private browsing, cleared site data, another browser, another device, or a different origin can mean that the draft is unavailable.

The original page and the editor use separate draft storage keys. Favorites and recent fonts are also local conveniences. None of these imply cloud account synchronization or a GitHub commit of your design.

### What cannot restore the editable design?

An exported SVG, PNG, WebP, or HTML snippet is not the JSON master. The artwork can look identical while lacking the original editable controls and inheritance relationships. Keep both the editable master and the final deliverable.

## Exporting

### Static SVG

Choose SVG for scalable still lettering. The shapes are paths, so a website does not need the original typeface installed. The SVG can include filters and texture that other vector applications interpret differently. Check it in the actual destination tool before assuming perfect cross-application rendering.

A static SVG does not contain the live Atypix lettering timeline. Placing it in an image tag is an excellent choice for a still heading graphic or for animating the complete image with website CSS.

### PNG and WebP

Choose the desired output width. Atypix renders a still image at that width while preserving the artwork's aspect ratio. Use sufficient pixels for the intended display size and density, but avoid unnecessarily enormous assets.

Transparent surroundings allow the artwork to sit over your website background. The preview canvas color is not an automatic image background. WebP support and encoding behavior depend on the browser; where the requested format cannot be produced, the app can fall back to PNG.

### Animated HTML

Copy the snippet or download the animated HTML. It contains the layered SVG markup, the runtime, serialized motion settings, and a GSAP CDN script reference. It does not require the font catalog, font parser, or font files to redraw the exported outlines.

The snippet is a fragment suitable for a website's HTML/script integration, not an image URL. A builder that strips scripts will not run it merely because the SVG markup survived. Test the published page, not just the builder's edit preview.

New exports generate their own IDs. Generate fresh snippets for multiple artwork instances rather than duplicating a block with identical IDs. SVG gradients, masks, and other internal references depend on those identifiers.

### Copy settings and Show code

Copied settings assume the appropriate artwork, GSAP, and runtime already exist. They are useful for an existing integration, but are not the complete embed. Show code is an advanced inspection aid; choose the full snippet when starting a normal website embed.

### Dependency and hosting choices

A normal animated snippet loads GSAP from the configured CDN. A production site can consolidate compatible GSAP loading or self-host it under its own dependency policy. Preserve execution order: library first, runtime and initialization afterward.

An exported static SVG needs no GSAP. An animated snippet still needs JavaScript. Hosting a downloaded snippet does not automatically make its external library reference available offline.

## Practical recipes

### A restrained dimensional wordmark

Start with a bold display family and a plain face. Reduce extrusion depth, choose a consistent direction, and use Smooth or subtle Hatching shading. Set grain to None or a small amount. Compare at the smallest intended display size before adding outlines.

Export SVG for a still identity asset. Save JSON so a future wording or color change does not require rebuilding it from scratch.

### A playful hand-arranged title

Set the overall text and font first. Choose a palette and suitable preset. In Letter, alternate small rotations and vertical offsets, with occasional scale changes. Keep enough spacing for the most rotated letters and inspect shadows where characters overlap.

Use a relatively simple entrance initially. Once the composition reads clearly, add stagger and a little overshoot. Excessively irregular layout plus strong motion can obscure the words.

### A two-line animated heading

Give the first line the main display role and make the second smaller. In the editor, establish a shared animation, then switch to per-line settings only if the second line needs a different entrance. Set its line start to create the desired relationship.

Preview Once before switching to Loop or Ping-pong. This separates sequencing problems from repeat behavior. Export HTML and test it at the real container width.

### A grungy colored texture

Choose Grunge in Finish, select a contrasting grain color, and begin with a modest amount. Add small wobble if appropriate. Inspect thin strokes and counters so texture does not destroy legibility.

Remember that Grunge is a clipped overlay. For a cut-paper or transparent chipped-ink result, use further editing outside Atypix rather than expecting the grain control to erase geometry.

### A moving block on a website

Finish the lettering animation in Atypix, then place its complete snippet inside your own outer motion wrapper. Animate the wrapper for entrance or exit and leave the generated internal elements to Atypix. See the working patterns in the [embedding guide](EMBEDDING.md#animate-the-whole-artwork-as-one-block).

If the letters do not need to animate separately, use a static SVG inside that wrapper. This is simpler and avoids loading the lettering runtime just to move a finished graphic.

## Troubleshooting

### A font does not load

Confirm network access and wait for the loading attempt to finish. Try another supported family to distinguish a general connection problem from a family-specific issue. Check the console/network panel if you are developing the site. Preserve the JSON while resolving an unavailable saved family.

### A letter looks broken or has a strange diagonal

Compare a plain face with decoration, grain, and wobble reduced. This helps separate outline geometry from texture or decoration. Inspect the same letter in a different family and the same family at another weight.

The renderer includes contour handling for overlapping font outlines, including fixes for cases such as Eczar and Google Sans X. That is not a guarantee that every possible glyph outline is perfect. A useful report includes the family, weight/style, exact text, edition, screenshot, and JSON.

### An outline or animation panel is missing

Check whether an outline exists. Global width 0, a letter override, or a face treatment can make it absent. The animation interface hides irrelevant parts. For drop shadow, check both distance and opacity; for extrusion, check depth and whether the face is Flat.

### Grain is invisible

Check that the global grain preset is not None, its amount is nonzero, and its color contrasts with the artwork. Inspect the relevant letter override. Fine texture may disappear when the artwork is very small.

### The page is slow

Reduce letter count or decoration density, then simplify grain, wobble, blur, and shading. Test one change at a time. Check the final embed on a real target device. A static export may be more appropriate if the artwork is complex and only needs whole-block movement.

### The HTML appears but does not animate

Make sure you used the full animated snippet and that the host allows its scripts. Check GSAP loading and script order. If using When in view, bring the artwork into the viewport. If inserting via JavaScript, remember that assigning HTML with `innerHTML` does not ordinarily execute inserted script tags.

### The artwork is clipped

Inspect the host container's `overflow`, fixed height, and transforms. The generated artwork uses an aspect-ratio container and layered content. Do not give its internal wrappers arbitrary heights or apply broad website rules to every SVG/path/div. Clip a deliberate outer stage only when that is part of the effect.

### Playback starts earlier than expected

On load means runtime initialization, not every page resource finishing. When in view is geometric intersection, not proof that a person has read the text or that an overlay is absent. Its current check is not a strict 25% ratio gate. Use a host-controlled trigger for precise choreography.

### Ping-pong looks like the timeline is rewinding

That is the intended return phase. The same behavior is included in animated HTML. Exporting a still image will not capture either direction as an animation.

## Frequently asked questions

### 1. Is Atypix a normal website text editor?

It is a lettering artwork tool. The exported appearance uses outlined geometry rather than ordinary selectable, reflowing HTML text. Keep important page text accessible in the host page and use the artwork appropriately.

### 2. Do website visitors need the font installed?

No, finished SVG paths carry the shapes. The editor needs the selected font to build or rebuild a design, but the exported artwork does not need that font to draw those paths.

### 3. Does browsing All fonts download every family?

No. The catalog supplies family information; only the selected font downloads. The result list is not a live-font specimen wall.

### 4. Why is a family missing a weight or italic option?

The available instances depend on the family and supported source files. Atypix does not synthesize every weight or style for every family.

### 5. Can I use any language supported by Google Fonts?

Not reliably. A font containing glyphs is only one requirement. The current character-by-character engine does not supply full connected-script shaping. Inspect actual words and use a shaping-capable tool when the language requires it.

### 6. Can different lines use different fonts?

Yes. Select the target line in Font or use its font button in Text. Check that selector before browsing families.

### 7. Can one letter use a different face treatment?

Yes. Choose it in Letter and change the face selector. Reset face restores the line's inherited style-cycle behavior.

### 8. Can I put a completely different font on one letter?

The standard font controls apply at line level. Letter face treatments are visual styles, not font-family selectors. Plan separate lines or use another composition workflow if you require mixed families within one line.

### 9. What is the difference between Plain and Flat?

Plain removes decoration while retaining dimensional styling. Flat removes the extrusion for that letter. Choose based on geometry as well as the visible face.

### 10. How do I remove an outline?

Set the relevant global or letter outline width to 0. Animation → Outline does not currently offer a None entrance. Removing the design's outline can hide its animation panel.

### 11. Does 3D shadow None remove extrusion?

No. It removes shading from the extrusion. Reduce extrusion depth or choose a Flat face to remove the depth itself.

### 12. Why does changing the palette undo individual letter colors?

A global palette change clears those color overrides so it can apply consistently. Save a version before trying a new palette, or Undo the change.

### 13. Does grain have to be white?

No. Finish includes a grain color picker. Choose any appropriate color and judge it against the face and extrusion colors.

### 14. Does Grunge make transparent holes?

No. It creates a textured overlay clipped to the lettering. It is not a destructive cutout operation.

### 15. Why can a configured color have no visible effect?

Its layer might not exist, might have zero opacity or distance, or might be covered or too similar to adjacent colors. Check the relevant geometry and effect before changing the palette repeatedly.

### 16. Are presets safe to use late in a project?

They are useful experiments, but complete style presets can replace substantial settings and sometimes example words. Download JSON first if you need a permanent checkpoint.

### 17. Are animation presets the same as style presets?

No. Animation presets establish motion. Style presets establish a broader visual design. Their effects and scope differ.

### 18. Can each line animate differently?

The timeline editor supports per-line part settings. The original edition has its older timing controls and does not expose the same newer editing interface.

### 19. Why are animation settings hidden for some parts?

The UI only shows parts present in the relevant artwork or applicable animated states. Restore the effect to expose its controls again.

### 20. Is an earlier letter start the same as a shorter duration?

No. Start timing determines when movement begins. Duration determines how long it takes. Easing determines the rate of change during that duration.

### 21. Does Ping-pong export correctly?

Animated HTML includes forward playback, hold, reverse playback, hold, and repetition. A backward-moving editor playhead represents that reverse phase. SVG, PNG, and WebP remain still exports.

### 22. What is the difference between Loop and Ping-pong?

Loop finishes forward, holds, fades the complete artwork, and resets. Ping-pong returns through the actual animation in reverse, with endpoint holds and no loop-reset fade.

### 23. Does Speed affect Hold?

The timeline's speed scaling affects the perceived hold as well as transitions. Test the full repeated cycle after changing global speed.

### 24. Does When in view play again every time I scroll back?

Once does not automatically restart on every re-entry. Loop and Ping-pong pause out of intersection and resume rather than beginning again. Use custom integration if you need a different lifecycle.

### 25. Does When in view know whether an overlay covers the artwork?

No. The current observer uses geometric intersection. It is not a perceptual visibility detector and does not account for every way a user can be prevented from seeing content.

### 26. Is the trigger exactly 25% visible?

Not in the current runtime. The observer has a 25% notification threshold, but playback checks `isIntersecting`. Initial partial intersection can therefore start it below 25%. See the embedding guide for precise triggers.

### 27. Can I animate the complete title off the screen?

Yes. Put the complete exported artwork inside an outer wrapper and animate the wrapper. Keep Atypix's generated internal transforms independent. A static SVG also works if only whole-title movement is needed.

### 28. Can I put several snippets on one page?

Yes, using independently generated IDs and sensible library loading. Fresh exports are safer than copying one identical block repeatedly. Consolidate GSAP loading carefully if optimizing a page with several snippets.

### 29. Will pasting the snippet into any website builder work?

Only if that builder and publishing configuration permit the required HTML and JavaScript. Some edit previews, sanitized content blocks, and CMS fields strip scripts. Follow the host's supported embed mechanism.

### 30. Can I embed the animated result as an image?

An image tag displaying an SVG or PNG is a still asset in this workflow. The animated HTML needs live markup and script execution, or an appropriately hosted iframe integration.

### 31. Is the preview background exported?

The standard artwork exports have transparent surroundings. The canvas color is a preview aid. Add the desired background in the destination composition or website.

### 32. Is JSON my final website asset?

No. JSON is the editable design master. Export animated HTML for live lettering or SVG/images for still artwork.

### 33. Can I reopen an SVG and recover all controls?

Not through the Atypix JSON-load workflow. Keep the design JSON. Flattened artwork is not a complete record of editable settings and inheritance.

### 34. Are browser drafts backed up to GitHub?

No. They live in local browser storage. Downloaded files also do not automatically become repository commits. Save and publish project assets through your normal file workflow.

### 35. Can I transfer a design between devices?

Download JSON, transfer that file, and load it on the other device. Fonts still need to be available to the editor. Local favorites and recent lists should not be assumed to transfer.

### 36. Does Atypix export video or GIF?

There is no built-in video/GIF exporter in the current interface. Use an external capture or rendering workflow if that format is required, and verify its frame rate, transparency, and output quality separately.

### 37. Will a still export match my scrubbed animation frame?

Still exports represent the design's static artwork. They are not screenshots of the current timeline time or a recording of animated endpoint settings.

### 38. Does the animated HTML work offline?

Not automatically: the normal snippet references GSAP on a CDN. An offline integration must provide its dependencies locally and preserve correct script order.

### 39. Does the snippet automatically respect reduced-motion preferences?

The exported lettering runtime does not currently implement an automatic reduced-motion bypass. Provide a static alternative or control whether the animated integration is initialized. Merely stopping an entrance before its first frame can leave letters hidden.

### 40. Should the lettering be my only accessible heading?

Prefer meaningful host-page text and a deliberate accessible labeling strategy. Do not expose duplicate announcements from an accessible heading plus multiple artwork layers. The embedding guide gives a practical decorative-artwork pattern.

### 41. Why is my exported SVG different in another editor?

SVG filters, clipping, and compositing support vary between applications. Compare in the intended destination and consider a raster export if exact appearance matters more than editability or scaling.

### 42. Can I change the words by editing the snippet's text label?

No. The visible shapes are paths. Changing an accessibility label does not regenerate those paths. Edit the text in Atypix and export again.

### 43. Can CSS recolor every part after export?

It can modify SVG styling, but the export may use gradients, patterns, masks, and filters rather than one simple fill. Use Atypix's color controls and regenerate unless you are deliberately maintaining a custom SVG integration.

### 44. Why does a hidden animation keep using resources?

Geometric intersection, CSS opacity, document background throttling, and manual pause are different mechanisms. When in view handles intersection for looping playback; opacity alone is not a reliable stop signal. Coordinate custom hiding and lifecycle behavior in the host integration when needed.

### 45. What should I include in a bug report?

Include the edition, browser/device, exact reproduction steps, expected and actual behavior, a screenshot, and the design JSON when possible. For embedding problems, also describe the host platform, script placement, and console/network errors without including credentials.

## Glossary

| Term | Meaning in Atypix |
| --- | --- |
| Face | Front shape of a letter |
| Decoration | Pattern or detail applied to the face |
| Extrusion | Dimensional side/depth geometry |
| 3D shadow | Shading treatment on the extrusion |
| Drop shadow | Shadow behind the artwork |
| Outline | Stroke treatment around a glyph |
| Counter | Interior opening, such as the hole in an O |
| Grain | Surface texture overlay |
| Wobble | Irregularity applied to edges |
| Leading | Space between lines in the composition |
| Spread | Span over which letter starts are distributed |
| Anchor | Timing reference for a part transition |
| Override | A specific setting replacing inherited behavior |
| Runtime | JavaScript that plays the exported lettering |
| Viewport | Browser viewing area used for intersection checks |
| Master | Saved JSON used to continue editing |

## Production checklist

Before delivery:

- Proofread every word, including punctuation and accented characters.
- Check the chosen family, weight, and style on every line.
- Inspect spacing, overlaps, counters, and fine decoration at the final display size.
- Check grain and contrast against the actual destination background.
- Review Once, Loop, or Ping-pong through a complete cycle, including holds.
- Confirm whether playback should begin on initialization or intersection.
- Save the JSON master and give exported assets clear names.
- Test the actual exported format in its destination, not just the editor preview.
- For websites, verify script execution, responsive sizing, accessible text, and reduced-motion handling.
- Keep the JSON alongside the delivered assets for future revisions.

For exact HTML patterns, viewport behavior, multiple snippets, and custom start triggers, continue to the [website embedding guide](EMBEDDING.md).

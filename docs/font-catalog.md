# Editor font catalog

Both `Atypix.html` and `Atypix-editor.html` use the Text / Font split and share `assets/google-fonts.json`. Their respective animation interfaces remain separate.

Text contains words, line controls, size, spacing, alignment and leading. Font selects a line, searches family names, and offers the available weight/style combinations, recent choices, favorites and license links. Search results are capped at 40 with Show more. Search and scrolling never request outline files. The metadata catalog loads on first opening Font (or restoring an unfamiliar family); outline files load only after selection. Serve the checkout over HTTP so the relative JSON request works.

Each selected line saves `font` plus `fontSource: {family, weight, style, url}`. Versioned Google Fonts static TTF URLs preserve file identity across catalog updates. Older curated saves still use their original repository TTFs. Family-only catalog saves resolve to regular normal, or the first available variant. Failed selections retain the previous font; an unresolved saved family stays in the save and produces a warning rather than silently becoming Anton. Fonts already embedded as SVG paths in artwork exports need no font loader or catalog.

## Compatibility and scope

opentype.js 1.3.4 reads TrueType/OpenType and WOFF1, but has no WOFF2 decoding or working variation-axis application. The generator requests Google's legacy CSS API with a fixed nonbrowser user agent, which supplies static TrueType instances, including for variable source families. No API key is used. The loader rejects variable instances rather than displaying an incorrect weight. Roboto regular, bold and italic, DM Sans regular and Noto Sans Arabic regular were parsed with 1.3.4 and confirmed to have no `fvar` table; the Roboto weight outlines differ.

Catalog availability means Google supplied a static TTF URL, not that every glyph in every family has been tested with Atypix's renderer. Some repository entries are unreleased or aren't served by the API; those remain discoverable but disabled with an explanation. Color fonts may also fail outline parsing. Missing glyphs are reported for the actual selected text. The tool's individual-character layout does not support connected/complex-script shaping. Legacy CSS font files may have limited character coverage; the missing-character warning is authoritative for the actual file. Custom variable axes, user-uploaded fonts, and additional font sources are outside this implementation.

## Refreshing the generated index

Use a separate Google Fonts metadata checkout outside this repository:

```sh
git clone --depth=1 --filter=blob:none --no-checkout https://github.com/google/fonts.git /tmp/atypix-google-fonts
git -C /tmp/atypix-google-fonts sparse-checkout set --no-cone '/ofl/*/METADATA.pb' '/apache/*/METADATA.pb' '/ufl/*/METADATA.pb'
git -C /tmp/atypix-google-fonts checkout
python3 scripts/build-font-catalog.py /tmp/atypix-google-fonts
```

The JSON records the exact repository revision and generation date. For a specific revision, check it out before generation. The generator reads family/license/axis metadata, requests Google's versioned static TTF links in batches, and caches CSS responses under the system temporary directory. No font binaries are downloaded during generation. HTTP 400 isolates unpublished families; other request failures stop generation without replacing the output. Review the generated diff and test representative fonts before committing an update. Keep TLS verification enabled. Runtime font downloads require `fonts.gstatic.com`; catalog generation requires the GitHub proxy and `fonts.googleapis.com`.

## Overlapping outlines

Some fonts, including Eczar, construct glyphs from overlapping contour components. Filling those paths looks correct, but extruding or stroking each component creates internal walls and seams. Both tools now resolve intersections under the nonzero fill rule before generating letter geometry. A locally vendored Paper.js core preserves Bezier curves; ordinary nonoverlapping contours pass through unchanged. Counters retain their winding and glyph metrics are not altered. The work is cached by font object, character and size, avoiding cache collisions between fonts with identical name metadata. Generated artwork and animation snippets contain the resolved paths and need no Paper.js dependency.

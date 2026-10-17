# Atypix

Dimensional lettering, made to move. Create styled, textured lettering in the browser and export SVG artwork, raster images, or animated HTML.

- [Open Atypix](https://firefly-fireflai.github.io/atypix/Atypix.html)
- [Open the timeline editor](https://firefly-fireflai.github.io/atypix/Atypix-editor.html)
- **[Instruction manual and FAQ](docs/ATYPIX-MANUAL.md)** — workflows, every main tab, animation, saving, exports, and troubleshooting.
- **[Website embedding guide](docs/EMBEDDING.md)** — move the complete artwork, understand viewport playback, integrate with a website, and handle accessibility.
- [Font catalog maintenance](docs/font-catalog.md)

Both editions share lettering tools. The timeline editor adds the newer animation timeline and per-line animation editing; the original edition retains the older animation controls.

For local development, serve this directory with a static HTTP server, such as `python3 -m http.server 8000`, then open the desired HTML file through that server. There is no application build step. Font loading and CDN dependencies require network access. See the manual for export dependencies and font limitations.

// Run after editing either <script id="runtime">: node scripts/build-export-runtime.mjs
// --check verifies freshness without downloading or running the minifier.
import { readFileSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
const check = process.argv.includes('--check');
for (const name of ['Atypix.html', 'Atypix-editor.html']) {
  const path = new URL('../' + name, import.meta.url);
  let html = readFileSync(path, 'utf8');
  const source = html.match(/<script id="runtime">([\s\S]*?)<\/script>/)[1].trim();
  const hash = createHash('sha256').update(source).digest('hex');
  const pattern = /<script id="export-runtime" type="application\/json" data-source-sha256="([^"]+)">[\s\S]*?<\/script>\n?/;
  if (check) {
    if (html.match(pattern)?.[1] !== hash) throw new Error(name + ': run node scripts/build-export-runtime.mjs');
    console.log(name + ': export runtime is current');
    continue;
  }
  const compact = execFileSync('npx', ['--yes', '--package=terser@5.44.0', 'terser', '--compress', '--mangle', '--comments', 'false'], { input: source, encoding: 'utf8' }).trim();
  const payload = JSON.stringify(compact).replace(/</g, '\\u003c');
  const tag = `<script id="export-runtime" type="application/json" data-source-sha256="${hash}">${payload}</script>\n`;
  html = pattern.test(html) ? html.replace(pattern, () => tag) : html.replace(/(<script id="runtime">[\s\S]*?<\/script>\n)/, (_, runtime) => runtime + tag);
  writeFileSync(path, html);
  console.log(`${name}: runtime ${Buffer.byteLength(source)} → ${Buffer.byteLength(compact)} bytes`);
}

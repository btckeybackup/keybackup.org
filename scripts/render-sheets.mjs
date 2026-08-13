// Renders each sheet of the current document to a PNG for use on the site.
// The site shows the real document rather than a mock-up of it, so these need
// regenerating whenever DOC_VERSION changes: `npm run sheets`.
import { chromium } from 'playwright'
import { mkdirSync } from 'node:fs'
import { fileURLToPath, pathToFileURL, URL } from 'node:url'
import { DOC_FILE } from '../src/site.js'

const root = new URL('../', import.meta.url)
const source = new URL(`public/${DOC_FILE}`, root)
const outDir = fileURLToPath(new URL('public/sheets/', root))

mkdirSync(outDir, { recursive: true })

const browser = await chromium.launch()
const page = await browser.newPage({
  viewport: { width: 1000, height: 1400 },
  deviceScaleFactor: 2,
})
await page.goto(pathToFileURL(fileURLToPath(source)).href, {
  waitUntil: 'networkidle',
})

// The sheets are sized for print and carry no page margin on screen. Add the
// margin they would have on paper so each crop reads as a printed sheet.
await page.addStyleTag({
  content: `
    body { background: #ffffff !important; }
    .sheet {
      background: #ffffff;
      box-sizing: content-box !important;
      padding: 15mm !important;
      margin: 0 !important;
    }
  `,
})

const sheets = await page.locator('.sheet').all()
if (sheets.length !== 4) {
  throw new Error(`Expected 4 sheets in ${DOC_FILE}, found ${sheets.length}`)
}

for (const [i, sheet] of sheets.entries()) {
  const file = `sheet-${i + 1}.png`
  await sheet.screenshot({ path: `${outDir}${file}` })
  console.log(`rendered ${file}`)
}

await browser.close()

import './style.css'
import { DOC_VERSION, DOC_FILE, DOC_HREF, REPO_URL } from './site.js'
import { renderLayout } from './layout.js'
import { icon } from './icons.js'
import { trackContents } from './toc.js'

renderLayout()

if (document.body.dataset.page === 'guide') {
  trackContents()
}

// Any element marked with data-icon gets that Phosphor glyph inlined.
for (const el of document.querySelectorAll('[data-icon]')) {
  el.innerHTML = icon(el.dataset.icon, { size: Number(el.dataset.iconSize) || 20 })
}

// Fill in the version and download target wherever a page asks for them.
for (const el of document.querySelectorAll('[data-doc-version]')) {
  el.textContent = DOC_VERSION
}

for (const a of document.querySelectorAll('[data-doc-download]')) {
  a.href = DOC_HREF
  a.download = DOC_FILE
}

// Same file, opened rather than saved.
for (const a of document.querySelectorAll('[data-doc-view]')) {
  a.href = DOC_HREF
  a.target = '_blank'
  a.rel = 'noopener'
}

for (const a of document.querySelectorAll('[data-repo-link]')) {
  a.href = REPO_URL
}

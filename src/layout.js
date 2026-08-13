import { DOC_VERSION, REPO_URL } from './site.js'
import { icon } from './icons.js'

// Header and footer are rendered from here so both pages stay in sync.
export function renderLayout() {
  const page = document.body.dataset.page

  const header = document.querySelector('header')
  if (header) {
    header.innerHTML = `
      <nav
        id="site-header--nav"
        class="mx-auto flex h-16 max-w-6xl items-center justify-between px-5 sm:px-8"
        aria-label="Primary"
      >
        <a
          href="/"
          id="site-header--brand-link"
          class="flex items-baseline gap-2 transition-opacity hover:opacity-70"
        >
          <span class="text-[0.9375rem] font-semibold tracking-tight">keybackup</span>
          <span class="font-mono text-xs text-muted">v${DOC_VERSION}</span>
        </a>

        <div class="flex items-center gap-6">
          <a
            href="/guide/"
            id="site-header--guide-link"
            class="nav-link"${page === 'guide' ? ' aria-current="page"' : ''}
          >Guide</a>
          <a
            href="${REPO_URL}"
            rel="noopener"
            id="site-header--repo-link"
            class="nav-link flex items-center gap-1.5"
          >${icon('github-logo', { size: 17 })}<span>GitHub</span></a>
        </div>
      </nav>
    `
  }

  const footer = document.querySelector('footer')
  if (footer) {
    footer.innerHTML = `
      <div
        id="site-footer--inner"
        class="mx-auto flex max-w-6xl flex-col gap-3 px-5 py-9 text-sm text-muted sm:flex-row sm:items-center sm:justify-between sm:px-8"
      >
        <p id="site-footer--text">
          Open source. No trackers, no cookies, nothing phones home.
        </p>
        <a
          href="${REPO_URL}"
          rel="noopener"
          id="site-footer--repo-link"
          class="link flex items-center gap-1.5 no-underline hover:underline"
        >${icon('github-logo', { size: 16 })}<span>Source and issues</span></a>
      </div>
    `
  }
}

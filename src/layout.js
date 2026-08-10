import { DOC_VERSION, REPO_URL } from './site.js'

// Header and footer are rendered from here so both pages stay in sync.
export function renderLayout() {
  const page = document.body.dataset.page

  const header = document.querySelector('header')
  if (header) {
    header.innerHTML = `
      <nav id="site-header--nav">
        <ul><li><a href="/" id="site-header--brand-link"><strong>keybackup</strong></a> <small>v${DOC_VERSION}</small></li></ul>
        <ul>
          <li><a href="/guide/" id="site-header--guide-link"${page === 'guide' ? ' aria-current="page"' : ''}>Guide</a></li>
          <li><a href="${REPO_URL}" rel="noopener" id="site-header--repo-link">GitHub</a></li>
        </ul>
      </nav>
    `
  }

  const footer = document.querySelector('footer')
  if (footer) {
    footer.innerHTML = `
      <small id="site-footer--text">
        Open source. No trackers, no cookies, nothing phones home.
        <a href="${REPO_URL}" rel="noopener" id="site-footer--repo-link">Source and issues on GitHub</a>.
      </small>
    `
  }
}

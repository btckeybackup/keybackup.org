// Marks the contents entry for whichever section the reader is currently in.
// Uses IntersectionObserver rather than a scroll listener, so nothing runs on
// the scroll frame.
export function trackContents() {
  const links = [...document.querySelectorAll('#guide--contents--list a[href^="#"]')]
  if (links.length === 0) return

  const byId = new Map()
  for (const link of links) {
    const section = document.querySelector(link.getAttribute('href'))
    if (section) byId.set(section, link)
  }

  const setActive = (link) => {
    for (const other of links) other.removeAttribute('data-active')
    link.setAttribute('data-active', '')
  }

  // A thin band near the top of the viewport. Whichever section crosses it is
  // the one being read.
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) setActive(byId.get(entry.target))
      }
    },
    { rootMargin: '-12% 0px -78% 0px', threshold: 0 },
  )

  for (const section of byId.keys()) observer.observe(section)
}

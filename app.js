(function () {
  const root = document.getElementById("pubs");
  if (!root) return;
  const chipsEl = document.getElementById("chips");
  const tags = [...new Set(PUBLICATIONS.flatMap(p => p.tags))].sort();
  let active = decodeURIComponent(location.hash.replace("#tag=", "")) || "";
  if (!tags.includes(active)) active = "";

  const esc = s => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const mediaHtml = m => !m ? "figure"
    : /\.mp4$/i.test(m) ? `<video src="${m}" autoplay loop muted playsinline></video>`
    : `<img src="${m}" alt="">`;

  const svg = d => `<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${d}</svg>`;
  const ICONS = {
    Paper: svg('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>'),
    Talk: svg('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M12 16v4M8 20h8M10 8.5v3l3-1.5z"/>'),
    Code: svg('<path d="M8 8l-5 4 5 4M16 8l5 4-5 4M14 5l-4 14"/>'),
    Video: svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M10 9v6l5-3z"/>'),
    Poster: svg('<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M8 7h8M8 11h3v5H8zM13 11h3M13 14h3"/>'),
  };
  const linkHtml = (k, v) => `<a class="link" href="${v}">${ICONS[k] || ICONS.Paper}${k}</a>`;

  function render() {
    chipsEl.innerHTML = ["All", ...tags].map(t =>
      `<button class="chip${(t === "All" ? !active : t === active) ? " on" : ""}" data-tag="${t}">${t}</button>`).join("");
    const list = PUBLICATIONS.filter(p => !active || p.tags.includes(active)).sort((a, b) => b.year - a.year);
    let html = "", year = null;
    for (const p of list) {
      if (p.year !== year) { year = p.year; html += `<h3 class="year">${year}</h3>`; }
      const authors = p.authors.map(a => /Karabag/.test(a) ? `<b>${esc(a)}</b>` : esc(a)).join(", ");
      const links = Object.entries(p.links).map(([k, v]) => linkHtml(k, v)).join("");
      html += `<article class="paper"><div class="figure"><div class="media${p.media ? "" : " ph"}">${mediaHtml(p.media)}</div>${p.caption ? `<div class="caption">${esc(p.caption)}</div>` : ""}</div><div>
        <div class="title">${esc(p.title)}</div><div class="authors">${authors}</div><div class="venue">${esc(p.venue)}</div>
        ${links ? `<div class="meta">${links}</div>` : ""}
        <div class="tags">${p.tags.map(t => `<a class="tag" href="#tag=${encodeURIComponent(t)}" data-tag="${t}">#${t}</a>`).join("")}</div>
        ${p.abstract ? `<details><summary>Abstract</summary><p>${esc(p.abstract)}</p></details>` : ""}</div></article>`;
    }
    root.innerHTML = html || '<p class="empty">No papers with this tag.</p>';
  }
  document.addEventListener("click", e => {
    const t = e.target.closest("[data-tag]");
    if (!t) return;
    e.preventDefault();
    active = t.dataset.tag === "All" ? "" : t.dataset.tag;
    history.replaceState(null, "", active ? "#tag=" + encodeURIComponent(active) : location.pathname);
    render();
  });
  render();
})();

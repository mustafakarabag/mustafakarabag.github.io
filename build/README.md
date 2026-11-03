# Build
- `python3 build/build_publications.py` reads `build/publications.xlsx` and `build/papers/<Folder>/` (abstract.txt, media/figure + caption.txt), copies figures to `media/`, and writes `data/publications.js`. Standard library only.
- `python3 build/build_pages.py` rebuilds the three HTML pages.

To add a paper: add a row to `publications.xlsx`, add its folder under `build/papers/`, then run the first script.

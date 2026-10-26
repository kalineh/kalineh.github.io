# kalin.games

Landing page, lightweight game pages and short links for kalin.games, served by GitHub Pages.

- `index.html` is the English landing page; `ja/index.html` is the Japanese version and `zh/index.html` the Simplified Chinese one (keep all three in sync). Images live in `img/`.
- `ashigaru/`, `dragonwake/`, `solspire/` and `azemar/` are static overview pages, with matching pages under `ja/` and `zh/`. Keep those three language versions in sync. They share `brand.css` / `game.css` and reuse the existing small JPEGs; no JavaScript or external fonts are required.
- Game cards open these overview pages; their Steam / Play buttons remain direct links. `brand.css` defines the fixed publisher capsule and shared header alignment used on Azemar's web pages.
- Short links: edit `links.json` (e.g. `"mmo": "https://..."`), run `python3 build_links.py`, then commit and push. Each key becomes `kalin.games/<key>`.
- Any other public repo of kalineh with GitHub Pages enabled automatically appears at `kalin.games/<repo-name>/` (e.g. `kalin.games/dragonwake-pages/`), shown directly, not redirected.
- `CNAME` holds the custom domain. DNS lives at Squarespace: apex A records to GitHub Pages IPs, `www` CNAME to `kalineh.github.io`.
- `build_links.py` never touches `ja/`, `zh/`, `img/` or any folder it didn't generate.

# kalin.games

Landing page and short links for kalin.games, served by GitHub Pages.

- `index.html` is the landing page.
- Short links: edit `links.json` (e.g. `"mmo": "https://..."`), run `python3 build_links.py`, then commit and push. Each key becomes `kalin.games/<key>`.
- Any other public repo of kalineh with GitHub Pages enabled automatically appears at `kalin.games/<repo-name>/` (e.g. `kalin.games/dragonwake-pages/`), shown directly, not redirected.
- `CNAME` holds the custom domain. DNS lives at Squarespace: apex A records to GitHub Pages IPs, `www` CNAME to `kalineh.github.io`.

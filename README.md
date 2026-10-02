# spigot-javadoc

Static historical Javadoc served at [spigot-javadoc.s7a.dev](https://spigot-javadoc.s7a.dev/). Each Minecraft version lives under `docs/{source}/{version}/`.

## Updating mirrors

The [spigot-event-list downloader](https://github.com/sya-ri/spigot-event-list/tree/master/packages/downloader) resolves official Maven Javadoc archives and extracts the complete HTML, search indexes, styles, scripts, and license files. For example, to generate one historical version from a spigot-event-list checkout with this repository at its `spigot-javadoc` path:

```sh
mise exec node@24 -- npm --workspace packages/downloader run start -- --version 26.2
```

In this repository, prepare the selected generated directories before staging:

```sh
python scripts/prepare-mirror.py spigot/26.2 purpur/26.2
git diff --cached --check
```

This removes trailing whitespace from generated text without changing documentation or license wording, and excludes Maven's `META-INF/MANIFEST.MF` packaging metadata from the static site. HTML pages, indexes, scripts, styles and license files remain present.

Publish only the version directories needed for historical reference links. Prefer versioned official Javadoc when available. The public [Spigot](https://hub.spigotmc.org/javadocs/spigot/) and [Purpur](https://purpurmc.org/javadoc/) Javadoc follows their latest API; use mirrors when those pages no longer document the required version.

Review the generated directories and verify the corresponding event links before opening a PR against `master`. GitHub Pages publishes `/docs` after merge. Keep the existing version directories, `docs/CNAME`, and `docs/.nojekyll` in place.

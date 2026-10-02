# spigot-javadoc

Static historical Javadoc served at [spigot-javadoc.s7a.dev](https://spigot-javadoc.s7a.dev/). Each Minecraft version lives under `docs/{source}/{version}/`.

## Updating mirrors

The [spigot-event-list downloader](https://github.com/sya-ri/spigot-event-list/tree/master/packages/downloader) resolves official Maven Javadoc archives and extracts the complete HTML, search indexes, styles, scripts, and license files. From a spigot-event-list checkout with this repository at its `spigot-javadoc` path:

```sh
mise exec node@24 -- npm --workspace packages/downloader run start -- --version 26.2
```

In this repository, prepare the selected generated directories before staging:

```sh
python scripts/prepare-mirror.py spigot/26.2 purpur/26.2
git diff --cached --check
```

This removes trailing whitespace from generated text without changing documentation or license wording, and excludes Maven's `META-INF/MANIFEST.MF` packaging metadata from the static site. HTML pages, indexes, scripts, styles and license files remain present.

Publish only the version directories needed for historical reference links. Paper's official Javadoc has versioned URLs for [26.2](https://jd.papermc.io/paper/26.2/) and [26.3](https://jd.papermc.io/paper/26.3/). The public [Spigot](https://hub.spigotmc.org/javadocs/spigot/) and [Purpur](https://purpurmc.org/javadoc/) Javadoc currently documents 26.3 and follows their latest API; the mirrors below preserve 26.2.

Review the generated directories and verify the corresponding event links before opening a PR against `master`. GitHub Pages publishes `/docs` after merge. Keep the existing version directories, `docs/CNAME`, and `docs/.nojekyll` in place.

## 26.2 sources

These mirrors use the same builds as the corresponding spigot-event-list event snapshot.

| Source | Official Javadoc archive |
| --- | --- |
| Spigot | [26.2 #13 snapshot](https://hub.spigotmc.org/nexus/content/repositories/snapshots/org/spigotmc/spigot-api/26.2-R0.1-SNAPSHOT/spigot-api-26.2-R0.1-20260915.151451-13-javadoc.jar) |
| Purpur | [26.2 #2633 stable](https://repo.purpurmc.org/snapshots/org/purpurmc/purpur/purpur-api/26.2.build.2633-stable/purpur-api-26.2.build.2633-stable-javadoc.jar) |

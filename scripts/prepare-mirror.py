"""Prepare generated Javadoc directories for a static-site commit."""
import pathlib
import re
import sys

docs = pathlib.Path(__file__).resolve().parents[1] / "docs"
changed = 0
for argument in sys.argv[1:]:
    directory = (docs / argument).resolve()
    if not directory.is_relative_to(docs) or not directory.is_dir():
        raise SystemExit(f"Not a generated directory under docs: {argument}")
    # Maven's CRLF manifest is archive metadata, not a Javadoc page or resource.
    manifest = directory / "META-INF" / "MANIFEST.MF"
    if manifest.is_file():
        manifest.unlink()
    for path in directory.rglob("*"):
        if not path.is_file() or not (
            path.suffix in {".html", ".js", ".css", ".txt"}
            or "legal" in path.relative_to(directory).parts
        ):
            continue
        original = path.read_bytes()
        formatted = re.sub(rb"[ \t]+(?=\r?$)", b"", original, flags=re.MULTILINE)
        formatted = formatted.rstrip(b"\r\n") + b"\n"
        if formatted != original:
            path.write_bytes(formatted)
            changed += 1
print(f"Prepared {len(sys.argv) - 1} mirror directories; formatted {changed} files.")

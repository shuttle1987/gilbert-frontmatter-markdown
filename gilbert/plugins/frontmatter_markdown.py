from pathlib import Path

import markdown

from gilbert import Site
from gilbert.content import Page

print("Loaded the Gilbert markdown with frontmatter loader")

def load_frontmatter_md(path: Path):
    """Loader for markdown files that contain frontmatter"""
    data = path.read_text(encoding='utf-8')
    md = markdown.Markdown(extensions = ['meta'], output_format='html5')
    processed = md.convert(data)
    return processed, md.Meta

Site.register_loader('md', load_frontmatter_md)


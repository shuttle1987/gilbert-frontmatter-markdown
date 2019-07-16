from markdown import markdown

from gilbert import Site
from gilbert.content import Page


def load_frontmatter_md(path):
    """Loader for markdown files that contain frontmatter"""
    data = path.read_text(encoding='utf-8')
    processed = markdown(self.data, output_format='html5', extensions=['meta'])
    html = md.convert(data)

    return html, processed.Meta

Site.register_loader('md', load_frontmatter_md)


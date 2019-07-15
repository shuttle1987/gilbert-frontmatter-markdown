from markdown import markdown

from gilbert import Site
from gilbert.content import Page


class FrontmatterMarkdownPage(Page):
    def content(self):
        raise NotImplementedError

def load_frontmatter_md(path):
    """Loader for markdown files that contain frontmatter"""
    data = path.read_text(encoding='utf-8')

    return data, {'content_type': 'FrontmatterMarkdownPage'}


Site.register_loader('md', load_frontmatter_md)


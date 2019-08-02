from pathlib import Path

import markdown

from gilbert import Site
from gilbert.content import Page
from gilbert.utils import oneshot


print("Loaded the Gilbert markdown with frontmatter loader")

class FrontmatterMarkdownPage(Page):
    extras: list = ['meta']

    @oneshot
    def content(self):
        extras = self.extras
        if not extras:
            extras = self.site.config.get('content_type', {}).get('MarkdownPage', [])
        md = markdown.Markdown(extensions=extras, output_format='html5')
        processed = md.convert(self.data)
        return processed

def load_frontmatter_md(path):
    data = path.read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['meta'], output_format='html5')
    return data, {'content_type': 'FrontmatterMarkdownPage', **md.Meta}

Site.register_loader('md', load_frontmatter_md)


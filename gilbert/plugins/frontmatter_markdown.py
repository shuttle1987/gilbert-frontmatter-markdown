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
        #import pdb; pdb.set_trace()
        md = markdown.Markdown(extensions=extras, output_format='html5')
        processed = md.convert(self.data)
        return processed, md.Meta

def load_frontmatter_md(path):
    data = path.read_text(encoding='utf-8')

    return data, {'content_type': 'FrontmatterMarkdownPage'}

Site.register_loader('md', load_frontmatter_md)


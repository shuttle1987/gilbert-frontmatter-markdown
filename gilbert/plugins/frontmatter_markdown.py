"""A frontmatter aware markdown loader for Gilbert"""
from pathlib import Path

import markdown
import yaml

from gilbert import Site

print("Loaded the Gilbert markdown with frontmatter loader")

def load_frontmatter_md(path):
    data = path.read_text(encoding='utf-8')
    md = markdown.Markdown(output_format='html5')

    with path.open() as fin:
        loader = yaml.Loader(fin)
        meta = loader.get_data()
        # PyYAML Reader greedily consumes chunks from the stream.
        # We must recover any un-consumed data, as well as what's left in the stream.
        if loader.buffer:
            data = loader.buffer[loader.pointer:-1]
        else:
            data = ''
        data += fin.read()
        print('markdown frontmatter meta: ', meta)

    processed = md.convert(data)
    return processed, meta

Site.register_loader('md', load_frontmatter_md)


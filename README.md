# gilbert-frontmatter-markdown

This is a plugin for [Gilbert](https://github.com/funkybob/gilbert) that provides the ability to load markdown documents that contain embedded metadata in the frontmatter.

## Why this plugin exists

You may have noticed that Gilbert provides a default markdown loader, but the default markdown loader in Gilbert will not process the frontmatter in your documents.
This is a deliberate decision (and is not a bug) since Gilbert is a general purpose static site generation framework that caters to many users.
Users may want to have frontmatter like material in their markdown documents that is not
supposed to be processed as metadata, since Gilbert doesn't want to make assumptions about document contents you have to use a loader such as this to get the frontmatter extracted.

If however you are using frontmatter in your markdown documents you may wish to use this loader.

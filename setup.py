from setuptools import setup

setup(name='gilbert-frontmatter-markdown',
      version='0.0.1',
      description='Supports frontmatter metadata',
      url='https://github.com/oadams/persephone',
      author='Janis Lesinskis',
      packages=['gilbert.plugins.frontmatter_markdown'],
      classifiers = [
          'Development Status :: 4 - Beta',
      ],
      keywords='gilbert',
      install_requires=[
          'markdown'
      ],
      include_package_data = True,
)
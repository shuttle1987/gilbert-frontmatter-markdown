from setuptools import setup

setup(name='gilbert-frontmatter-markdown',
      version='0.1.0',
      description='Supports frontmatter metadata',
      url='https://github.com/shuttle1987/gilbert-frontmatter-markdown',
      author='Janis Lesinskis',
      packages=['gilbert.plugins'],
      classifiers = [
          'Development Status :: 4 - Beta',
      ],
      keywords='gilbert',
      install_requires=[
          'markdown'
      ],
      include_package_data = True,
)

from setuptools import setup

setup(name='gilbert-frontmatter-markdown',
      version='0.2.0',
      description='Supports frontmatter metadata',
      url='https://github.com/shuttle1987/gilbert-frontmatter-markdown',
      author='Janis Lesinskis',
      license='AGPL v3',
      packages=['gilbert.plugins'],
      classifiers = [
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Operating System :: OS Independent',
      ],
      keywords='gilbert',
      install_requires=[
          'markdown',
          'pyyaml',
      ],
      include_package_data = True,
)

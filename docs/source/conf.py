# Configuration file for the Sphinx documentation builder.

import sys
from pathlib import Path

from src import __cliname__
sys.path.insert(0, Path(__file__).parents[2].joinpath('src/app').as_posix())

project = __cliname__
copyright = '2020, author'
author = 'author'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_click.ext',
]

napoleon_include_private_with_doc = True

html_theme = 'sphinx_rtd_theme'
html_theme_path = ['sphinx_rtd_theme.get_html_theme_path()']

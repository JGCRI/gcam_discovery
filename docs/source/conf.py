# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('../../'))

# current datetime to use as the version
today = f"Last updated: {datetime.utcnow().strftime('%b %d, %Y')}"


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Scenario Discovery with GCAM'
copyright = '2023-current, Battelle Memorial Institute'

release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.bibtex',
    'sphinx.ext.githubpages',
    'sphinx.ext.viewcode',
    'nbsphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# bibliography files
bibtex_bibfiles = ['refs.bib']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**.ipynb_checkpoints']

# Figures and tables are automatically numbered if they have a caption.
# This also helps with referencing figures in the main text (otherwise
# the link text is the figure caption).
numfig = True

numfig_format = {
    'section': 'Chapter %s',
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# theme options
html_theme_options = {
    'path_to_docs': '/docs',
    'repository_url': 'https://github.com/IMMM-SFA/msd_uncertainty_ebook',
    'use_issues_button': True,
    'use_download_button': True,
    'use_repository_button': True,
    'extra_navbar': f'<span style="display:block;text-align:left">{today}</span>',
    'home_page_in_toc': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

# -- Options for Latex
master_doc = 'index'

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = None

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'German NLP Group'
copyright = 'Philip May & Philipp Reißel 2021 (CC0)'
author = 'Philip May & Philipp Reißel'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "myst_nb",
    "sphinx.ext.githubpages",
]

# add github link
html_context = {
  'display_github': True,
  'github_user': 'German-NLP-Group',
  'github_repo': 'German-NLP-Group.github.io',
  'github_version': 'main/source/',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# turn off notebook execution
# also see https://myst-nb.readthedocs.io/en/latest/use/execute.html
jupyter_execute_notebooks = "off"

html_theme_options = {
    "prev_next_buttons_location": None,
}

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Optional MyST Syntaxes
# also see https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html
myst_enable_extensions = [
#    "amsmath",
#    "colon_fence",
#    "deflist",
#    "dollarmath",
#    "html_admonition",
#    "html_image",
    "linkify",
    "replacements",
#    "smartquotes",
#    "substitution"
]

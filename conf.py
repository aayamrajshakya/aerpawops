import os
import sys
import sphinx_rtd_theme
from datetime import date
from docutils import nodes
from docutils.parsers.rst import roles

year = str(date.today().year)

project = 'AERPAW Ops'
copyright = '2025, AERPAW'
author = 'AERPAW'
release = '1.0'

sys.path.insert(0, os.path.abspath('.'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'hoverxref.extension',
    'sphinx_tabs.tabs',
    'myst_parser',
]

# Allow Markdown files as source
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


# Optional: enable MyST features
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
]

hoverxref_auto_ref = True

hoverxref_role_types = {
    'hoverxref' : 'tooltip',
    'ref' : 'tooltip',
}

if os.environ.get('READTHEDOCS') != 'True':
    hoverxref_api_host = 'https://readthedocs.org'

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "display_version": False,
    "show_sourcelink": False,
    "collapse_navigation" : False,
    "sticky_navigation": False,
}

pygments_style = 'sphinx'
html_show_sphinx = False
html_show_sourcelink = False
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
templates_path = ['_templates']

def bold_point_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.literal(text, text)
    node['classes'].append('bold-point')
    return [node], []

roles.register_local_role('bold-point', bold_point_role)

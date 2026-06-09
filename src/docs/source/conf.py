import os
import sys
import time
from docutils import nodes
from docutils.parsers.rst import roles
 
os.environ["TZ"] = "Asia/Kolkata"
time.tzset()

# Add your package root to PYTHONPATH
sys.path.insert(0, os.path.abspath('../..'))

def method_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    return [nodes.inline(text=text, classes=["method-name"])], []

html_logo = "_static/logo.png"
html_title = 'Shapley Regression'
project = 'Shapley Regression'
copyright = '2026, Sarbadal Pal'
author = 'Sarbadal Pal'
release = '0.0.1'
# html_theme_options = {
#     "sidebar_hide_name": False,  # hide "Sarbadal Pal" text in sidebar brand
# }
 
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',
    'sphinx_togglebutton',
    'sphinx_copybutton',
]
 
templates_path = ['_templates']
exclude_patterns = []

html_context = { 
    "READTHEDOCS": False,
    "display_lower_left": False,
}
 
# html_theme = 'furo'
html_theme = 'sphinx_rtd_theme'
html_last_updated_use_utc = False
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S IST"
 
html_static_path = ['_static']
html_css_files = [
    'custom.css',
    'font.css',
    'compact_table.css',
    'logo.css',
    'source_code.css',
]

html_allow_unsafe = True
html_show_sphinx = False
html_copy_source = False
html_show_sourcelink = False
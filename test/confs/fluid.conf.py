# -*- coding: utf-8 -*-
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'First Doc'
copyright = '2020, Adewale Azeez'
author = 'Adewale Azeez'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
import os
import themata

html_theme_path = [os.path.dirname(themata.__file__)]

html_theme_options = {
    'project_icon': "https://media2.giphy.com/media/2vnId4IaAjIGZd2EWC/giphy.gif",
    'has_left_sidebar': True,
    'has_right_sidebar': True,
    'navbar_links': [
        ("Docs", "./docs"),
        ("Download", "https://pypi.python.org/pypi/milkish"),
        ("Examples", "./examples"),
        ("FAQ", "./faq")
    ],
    'social_icons': [
        ("https://twitter.com/iamthecarisma"),
        ("https://www.twitch.tv/amsiraceht"),
        ("https://github.com/Thecarisma"),
        ("https://www.linkedin.com/in/azeez-adewale/"),
        ("https://stackoverflow.com/users/6626422/thecarisma")
    ],
    'footer_menus': [
        {
            'title': 'Contact',
            'menu_items': [
                {
                    'link': "#",
                    'title': 'azeezadewale98@gmail.com'
                },
                {
                    'link': "",
                    'title': '12345678998'
                }
            ]
        },
        {
            'title': 'Documentation',
            'menu_items': [
                {
                    'link': "#",
                    'title': 'Title One'
                },
                {
                    'link': "#",
                    'title': 'Two'
                },
                {
                    'link': "#",
                    'title': 'Three'
                },
                {
                    'link': "#",
                    'title': 'Title Four'
                },
                {
                    'link': "#",
                    'title': 'Item Five'
                },
            ]
        },
        {
            'title': 'Community',
            'menu_items': [
                {
                    'link': "#",
                    'title': 'Stackoverflow'
                },
                {
                    'link': "",
                    'title': 'Slack'
                },
                {
                    'link': "",
                    'title': 'Forum'
                },
                {
                    'link': "",
                    'title': 'IRC'
                }
            ]
        }
    ],
}

html_theme = 'milkish'
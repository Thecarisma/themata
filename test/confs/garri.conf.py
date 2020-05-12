import os
import themata

project = 'First Doc'
copyright = '2020, Adewale Azeez'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]

html_theme_options = {
    'sidebar_position': 'right',
    'has_sidebar': True,
    'no_sidebar': [
        "singlepage"
    ],
    'toc_title': 'Main Links',
    "source_root": "https://github.com/Thecarisma/themata/tree/test/test/test_rst",
}

html_theme = 'garri'
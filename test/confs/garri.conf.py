import os
import themata

project = 'First Doc'
copyright = '2020, Adewale Azeez'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]

extensions = ['recommonmark']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

html_theme_options = {
    'sidebar_position': 'right',
    'has_sidebar': True,
    'no_sidebar': [
        "singlepage"
    ],
    'toc_title': 'Main Links',
    "source_root": "https://github.com/Thecarisma/themata/tree/test/test/test_rst",
    "metadata": {
        "enable": True,
        "url": "https://thecarisma.github.io/themata",
        "type": "website",
        "title": "Set of Highly customizable sphinx themes.",
        "description": "Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.",
        "image": "https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png",
        "keywords": "python, sphinx, thecarisma, themata, documentation, markdown, rst, themes",
        "author": "Adewale Azeez"
    },
    "twitter_metadata": {
        "enable": True,
        "card": "summary",
        "site": "@iamthecarisma",
        "creator": "@iamthecarisma",
        "title": "Set of Highly customizable sphinx themes.",
        "description": "Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.",
        "image": "https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png",
    }
}

html_theme = 'garri'
import os
import themata

project = 'Garri'
copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]
html_theme = 'garri'
html_favicon = '../images/themata.png'
master_doc = 'index'

html_theme_options = {
    'index_is_single': False,
    'sidebar_position': 'right',
    'has_sidebar': True,
    'no_sidebar': [
        "singlepage"
    ],
    'toc_title': 'Other Topics',
    'source_root': 'https://github.com/Thecarisma/themata/edit/test/docs/garri/',
    'source_root_edit_text': 'Edit on Github',
    'metadata': {
        "enable": True,
        "url": "https://thecarisma.github.io/themata/garri/",
        "type": "website",
        "title": "Garri Theme - Set of Highly customizable sphinx themes.",
        "description": "Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.",
        "image": "https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png",
        "keywords": "python, sphinx, thecarisma, themata, documentation, markdown, rst, themes",
        "author": "Adewale Azeez"
    },
    'twitter_metadata': {
        "enable": True,
        "card": "summary",
        "site": "@iamthecarisma",
        "creator": "@iamthecarisma",
        "title": "Garri Theme - Set of Highly customizable sphinx themes.",
        "description": "Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.",
        "image": "https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png",
    }
}
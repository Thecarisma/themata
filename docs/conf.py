import os
import themata

project = 'themata'
copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]
html_theme = 'sugar'
html_favicon = 'images/themata.png'
exclude_patterns = [
    'hackish/*',
    'milkish/*',
    'fandango/*',
    'clear/*',
    'fluid/*',
    'garri/*',
    'water/*',
    'sugar/*'
]

html_theme_options = {
    'navbar_links': [
        ("Download", "https://pypi.org/project/themata/"),
        ("Github", "https://github.com/Thecarisma/themata"),
        ("Follow me on twitter", "https://twitter.com/iamthecarisma")
    ],
    'navbar_sec_links': [
        ("hackish", "https://thecarisma.github.io/themata/hackish"),
        ("milkish", "https://thecarisma.github.io/themata/milkish"),
        ("fandango", "https://thecarisma.github.io/themata/fandango"),
        ("clear", "https://thecarisma.github.io/themata/clear"),
        ("fluid", "https://thecarisma.github.io/themata/fluid"),
        ("garri", "https://thecarisma.github.io/themata/garri"),
        ("water", "https://thecarisma.github.io/themata/water"),
        ("sugar", "https://thecarisma.github.io/themata/sugar")
    ],
    'metadata': {
        "enable": True,
        "url": "https://thecarisma.github.io/themata",
        "type": "website",
        "title": "Set of Highly customizable sphinx themes.",
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
        "title": "Set of Highly customizable sphinx themes.",
        "description": "Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.",
        "image": "https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png",
    }
}
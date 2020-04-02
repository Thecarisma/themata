import os
import themata

project = 'themata'
copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]
html_theme = 'milkish'
html_favicon = 'images/themata.png'
exclude_patterns = [
    'hackish/*',
    'milkish/*',
    'fandango/*',
    'clear/*',
    'fluid/*'
]

html_theme_options = {
    'navbar_links': [
        ("Download", "https://pypi.org/project/themata/"),
        ("Github", "https://github.com/Thecarisma/themata"),
        ("Follow me on twitter", "https://twitter.com/iamthecarisma")
    ]
}
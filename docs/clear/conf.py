import os
import themata

project = 'Clear'
copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]
html_theme = 'clear'
html_favicon = '../images/themata.png'

html_theme_options = {
    'index_is_single': False,
    'left_sidebar_only': [
        'otherpages/leftpage'
    ],
    'no_sidebar': [
        'otherpages/singlepage'
    ],
    'right_sidebar_only': [
        'otherpages/rightpage'
    ]
}
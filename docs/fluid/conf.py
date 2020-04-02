import os
import themata

project = 'Fluid'
copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]
html_theme = 'fluid'
html_favicon = '../images/themata.png'

html_theme_options = {
    'index_is_single': False,
    'show_navigators_in_index': False,
    'navbar_links': [
        ('Twitter', 'https://twitter.com/iamthecarisma'),
        ('Github', 'https://github.com/Thecarisma/themata/')
    ],
    'has_left_sidebar': True,
    'has_right_sidebar': True,
    'show_navigators': True,
    'footer_menus': [
        {
            'title': 'Contact',
            'menu_items': [
                {
                    'link': 'azeezadewale98@gmail.com',
                    'title': 'azeezadewale98@gmail.com'
                },
                {
                    'link': 'tel:911',
                    'title': '12345678998'
                }
            ]
        },
        {
            'title': 'Custom Pages',
            'menu_items': [
                {
                    'link': 'leftpage.html',
                    'title': 'Left Page'
                },
                {
                    'link': 'singletpage.html',
                    'title': 'Single Page'
                }
            ]
        }
    ],
    'social_icons': [
        ('fab fa-twitter', 'https://twitter.com/iamthecarisma'),
        ('fab fa-github', 'https://github.com/Thecarisma/themata/')
    ],
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
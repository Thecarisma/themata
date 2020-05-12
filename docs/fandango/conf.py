import os
import themata

project = 'Fandango'
copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]
html_theme = 'fandango'
html_favicon = '../images/themata.png'

html_theme_options = {
    'index_is_single': False,
    'show_navigators_in_index': False,
    'has_secondary_header': True,
    'navbar_links': [
        ('Twitter', 'https://twitter.com/iamthecarisma'),
        ('Github', 'https://github.com/Thecarisma/themata/')
    ],
    'has_right_sidebar': True,
    'show_navigators': True,
    'footer_menus': [
        {
            'title': 'Contact',
            'menu_items': [
                {
                    'link': 'https://thecarisma.github.io/',
                    'title': 'https://thecarisma.github.io/'
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
    'no_sidebar': [
        'otherpages/singlepage'
    ],
    'right_sidebar_only': [
        'otherpages/rightpage'
    ],
    'secondary_header_link': ('Support Devcareer', 'https://www.patreon.com/devcareer'),
    'toc_title': 'Other Topics',
    'exclude_secondary_header_in': [
        'index',
        'singlepage'
    ],
    'source_root': 'https://github.com/Thecarisma/themata/edit/test/docs/fandango/',
    'source_root_edit_text': 'Edit on Github'
}
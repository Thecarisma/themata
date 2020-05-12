import os
import themata

project = 'First Doc'
copyright = '2020, Adewale Azeez'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]

html_theme_options = {
    'project_icon': "https://github.com/Thecarisma/themata/raw/master/docs/images/themata.png",
    'has_left_sidebar': True,
    'show_navigators': True,
    'show_navigators_in_index': False,
    'left_sidebar_only': [
        "leftpage"
    ],
    'no_sidebar': [
        "singlepage"
    ],
    'navbar_links': [
        ("Docs", "./docs"),
        ("Download", "https://pypi.python.org/pypi/milkish"),
        ("Examples", "./examples"),
        ("FAQ", "./faq")
    ],
    'social_icons': [
        ("fab fa-twitter", "https://twitter.com/iamthecarisma"),
        ("fab fa-twitch", "https://www.twitch.tv/amsiraceht"),
        ("fab fa-github", "https://github.com/Thecarisma"),
        ("fab fa-linkedin", "https://www.linkedin.com/in/azeez-adewale/"),
        ("fab fa-stackoverflow", "https://stackoverflow.com/users/6626422/thecarisma")
    ],
    'footer_menus': [
        {
            'icon': 'fa-phone',
            'title': 'Contact',
            'menu_items': [
                {
                    'link': "#",
                    'title': 'https://thecarisma.github.io/'
                },
                {
                    'link': "",
                    'title': '12345678998'
                }
            ]
        },
        {
            'icon': 'fa-book',
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
            'icon': 'fa-users',
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
    "source_root": "https://github.com/Thecarisma/themata/tree/test/test/test_rst",
}

html_theme = 'water'
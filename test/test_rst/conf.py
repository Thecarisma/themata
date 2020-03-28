import os
import themata

project = 'First Doc'
copyright = '2020, Adewale Azeez'
author = 'Adewale Azeez'

html_theme_path = [os.path.dirname(themata.__file__)]

html_theme_options = {
    'project_icon': "https://media2.giphy.com/media/2vnId4IaAjIGZd2EWC/giphy.gif",
    'has_left_sidebar': True,
    'has_right_sidebar': True,
    'show_navigators': True,
    'show_navigators_in_index': False,
    'left_sidebar_only': [
        "leftpage"
    ],
    'right_sidebar_only': [
        "sampleregex1"
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

html_theme = 'fluid'
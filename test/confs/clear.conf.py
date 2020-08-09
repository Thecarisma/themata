import os
import themata

project = 'First Doc'
copyright = '2020, Adewale Azeez'
author = 'Adewale Azeez'

html_theme_path = [themata.get_html_theme_path()]

html_theme_options = {
    'project_icon': "https://github.com/Thecarisma/themata/raw/main/docs/images/themata.png",
    'has_left_sidebar': True,
    'has_right_sidebar': True,
    'collapsible_sidebar': True,
    'collapsible_sidebar_display': 'block',
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
    'social_icons': [
        ("fab fa-twitter", "https://twitter.com/iamthecarisma"),
        ("fab fa-twitch", "https://www.twitch.tv/amsiraceht"),
        ("fab fa-github", "https://github.com/Thecarisma"),
        ("fab fa-linkedin", "https://www.linkedin.com/in/azeez-adewale/"),
        ("fab fa-stackoverflow", "https://stackoverflow.com/users/6626422/thecarisma")
    ],
    "source_root": "https://github.com/Thecarisma/themata/tree/test/test/test_rst",
}

html_theme = 'clear'
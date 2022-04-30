import os
import themata

project = 'Sugar'
copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
author = 'Adewale Azeez'

html_theme = 'sugar'
html_favicon = '../images/themata.png'
master_doc = 'index'

html_theme_options = {
    'index_is_single': False,
    'show_navigators_in_index': False,
    'collapsible_sidebar': True,
    'collapsible_sidebar_display': 'block',
    'navbar_links': [
        ('Twitter', 'https://twitter.com/iamthecarisma'),
        ('Github', 'https://github.com/Thecarisma/themata/')
    ],
    'navbar_sec_links': [
        ('Twitter', 'https://twitter.com/iamthecarisma'),
        ('Github', 'https://github.com/Thecarisma/themata/')
    ],
    'has_left_sidebar': True,
    'has_right_sidebar': True,
    'show_navigators': True,
    'syntax_highlighter': 'prism',
    'code_block_editable': False,
    'syntax_highlighter_theme': 'coy',
    'syntax_highlighter_iframe_embed': False,
    'github_repo': 'https://github.com/Thecarisma/themata',
    'social_share_label': "Throw this page at people faces",
    'github_page_feedback_title': "Throw tantrum about this page to the developers",
    'github_page_view_feedbacks_label': "Look at your like tantrums on github",
    'source_root': 'https://github.com/Thecarisma/themata/edit/test/docs/clear/',
    'source_root_edit_text': 'Edit on Github',
    'enable_page_social_share': True,
    'page_rating_options': {
        'title': 'Did you find this documentation helpful?',
        "positive_icon": '<img style="height: 100%; width: 100%; object-fit: contain" src="https://avatars.githubusercontent.com/u/14879387?v=4"/>',
        "negative_icon": '<img style="height: 100%; width: 100%; object-fit: contain" src="https://avatars.githubusercontent.com/u/14879387?v=4"/>',
        "positive_event": 'alert("Positive")',
        "negative_event": 'alert("Negative")',
    },
    "enable_github_page_feedback": True,
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
    'left_sidebar_only': [
        'otherpages/leftpage'
    ],
    'no_sidebar': [
        'otherpages/singlepage'
    ],
    'right_sidebar_only': [
        'otherpages/rightpage'
    ],
    'source_root': 'https://github.com/Thecarisma/themata/edit/test/docs/sugar/',
    'source_root_edit_text': 'Edit on Github',
    'metadata': {
        "dynamic": True,
        "url": "https://thecarisma.github.io/themata/sugar/",
        "type": "website",
        "title": "Sugar Theme - Set of Highly customizable sphinx themes.",
        "description": "Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.",
        "image": "https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png",
        "keywords": "python, sphinx, thecarisma, themata, documentation, markdown, rst, themes",
        "author": "Adewale Azeez"
    },
    'twitter_metadata': {
        "dynamic": True,
        "card": "summary",
        "site": "@iamthecarisma",
        "creator": "@iamthecarisma",
        "title": "Sugar Theme - Set of Highly customizable sphinx themes.",
        "description": "Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.",
        "image": "https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png",
    }
}
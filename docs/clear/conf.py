import os
import themata

project = 'Clear'
copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
author = 'Adewale Azeeze'

html_theme = 'clear'
html_favicon = '../images/themata.png'
master_doc = 'index'

html_theme_options = {
    'index_is_single': False,
    'show_navigators_in_index': False,
    'has_left_sidebar': True,
    'has_right_sidebar': True,
    'collapsible_sidebar': True,
    'collapsible_sidebar_display': 'block',
    'show_navigators': True,
    'syntax_highlighter': 'syntaxy',
    'code_block_editable': False,
    'syntax_highlighter_theme': 'light',
    'syntax_highlighter_iframe_embed': False,
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
    'google_analytics_tracking_id': "UA-0000000-00",
    'github_repo': 'https://github.com/Thecarisma/themata',
    'github_new_product_issue_template': "Yahoo",
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
    'metadata': {
        "dynamic": True,
        "url": "https://thecarisma.github.io/themata/clear/",
        "type": "website",
        "title": "Clear Theme - Set of Highly customizable sphinx themes.",
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
        "title": "Clear Theme - Set of Highly customizable sphinx themes.",
        "description": "Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.",
        "image": "https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png",
    }
}

Sample Configuration
=====================

The **conf.py** file that generates this documentation.

.. code:: python

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
        'show_navigators_in_index': False,
        'has_left_sidebar': True,
        'has_right_sidebar': True,
        'show_navigators': True,
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
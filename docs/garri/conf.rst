
Sample Configuration
=====================

The **conf.py** file that generates this documentation.

.. code:: python

    import os
    import themata

    project = 'Garri'
    copyright = '2020, Adewale Azeez, Creative Commons Zero v1.0 Universal License'
    author = 'Adewale Azeez'

    html_theme_path = [themata.get_html_theme_path()]
    html_theme = 'garri'
    html_favicon = '../images/themata.png'

    html_theme_options = {
        'index_is_single': False,
        'sidebar_position': 'right',
        'has_sidebar': True,
        'no_sidebar': [
            "singlepage"
        ],
        'toc_title': 'Other Topics'
    }
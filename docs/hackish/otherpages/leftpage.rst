Left Sidebar Only. Theme Option
================================

Set this page to have only the left side bar by adding the page name to the theme option 
**left_sidebar_only**. 

Example
''''''''

.. code:: python

    import os
    import themata

    project = 'Hackish Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'

    html_favicon = 'favicon.png'
    html_theme = 'hackish'

    html_theme_options = {
        'left_sidebar_only': [
            'otherpages/leftpage'
        ]
    }
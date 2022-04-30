Left Sidebar Only. Theme Option
================================

Set this page to have only the left side bar by adding the page name to the theme option 
**left_sidebar_only**. 

Example
''''''''

.. code:: python

    import os
    import themata

    project = 'Sugar Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'

    html_favicon = 'favicon.png'
    html_theme = 'sugar'

    html_theme_options = {
        'left_sidebar_only': [
            'otherpages/leftpage'
        ]
    }
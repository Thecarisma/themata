No Sidebar. Theme Option
================================

Set this page to have no side bar by adding the page name to the theme option 
**no_sidebar**. 

Example
''''''''

.. code:: python

    import os
    import themata

    project = 'Clear Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'

    html_favicon = 'favicon.png'
    html_theme_path = [themata.get_html_theme_path()]
    html_theme = 'clear'

    html_theme_options = {
        'no_sidebar': [
            'otherpages/singlepage'
        ]
    }
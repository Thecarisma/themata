Right Sidebar Only. Theme Option
================================

Set this page to have only the right side bar by adding the page name to the theme option 
**right_sidebar_only**. 

Example
''''''''

.. code:: python

    import os
    import themata

    project = 'Fluid Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'

    html_favicon = 'favicon.png'
    html_theme_path = [themata.get_html_theme_path()]
    html_theme = 'fluid'

    html_theme_options = {
        'right_sidebar_only': [
            'otherpages/rightpage'
        ]
    }
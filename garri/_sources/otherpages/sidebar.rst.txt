Show Sidebar. Theme Option
================================

Set the project to show the sidebar and position the sidebar to the right side of the page.
**has_sidebar** to show sidebar and **sidebar_position** to pisition the sidebar left or right. 

Example
''''''''

.. code:: python

    import os
    import themata

    project = 'Fandango Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'

    html_favicon = 'favicon.png'
    html_theme = 'fadango'

    html_theme_options = {
        'sidebar_position': 'right',
        'has_sidebar': True
    }
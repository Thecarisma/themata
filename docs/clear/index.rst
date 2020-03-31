
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Main
   :name: main-nav

   preview


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Custom Files
   :name: sec-files

   /otherpages/singlepage
   /otherpages/test1
   /otherpages/test1.single
   /otherpages/test1.left
   /otherpages/test1.right
   /otherpages/leftpage
   

Clear
========

Setting up and using the clear theme.

Install the themata package from python index.

.. code:: bash

    pip install themata

or equivalent (add `themata` to any appropriate requirements files).

Example
---------

Below is a minimal sample **conf.py** file to use the clear theme.

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
        'project_icon': 'favicon.png'
    }

Theme Options
--------------

The following theme option are accepted in the theme.

* project_icon <string>:
    The abolute or relative (to _static folder) path to the image to use as the theme icon. 
    This is not the same as favicon. If the favicon is set using the variable `html_favicon` 
    and the project_icon is not set. The project_icon value will be the value of the favicon.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Main
   :name: main-nav

   preview
   conf


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Custom Files
   :name: sec-files

   /otherpages/singlepage
   /otherpages/test.single
   /otherpages/test.left
   /otherpages/test.right
   /otherpages/leftpage
   /otherpages/rightpage
   

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

    html_theme_optionss = {
        'project_icon': 'favicon.png'
    }

Theme Options
--------------

The following theme option are accepted in the theme.

Variable Options
'''''''''''''''''

.. csv-table::
    :header: "Option <Datatype>", "Description"

    "project_icon <string>", "The abolute or relative (to _static folder) path to the image to use as the theme icon. This is not the same as favicon. If the favicon is set using the variable `html_favicon` and the project_icon is not set. The project_icon value will be the value of the favicon."
    "index_is_single <boolean>", "This option is to indicate if any **index** page does not have sidebars. It is True by default which means any index page will not have any sidebar. To add sidebars to index pages set the value to False in `html_theme_optionss`."
    "show_navigators_in_index <boolean>", "The theme option to decide whether to show the bottom navigation buttons (index, next, previous) in any **index** page. By default it is False. To show the navigation buttons in index pages set the value to True in the `html_theme_optionss`."
    "has_left_sidebar <boolean>", "By default this theme renders the left sidebar. The left sidebar shows the documentation toc tree. To not shouw the left sidebar in all the pages set the value to False in the `html_theme_options`."
    "has_right_sidebar <boolean>", "By default this theme renders the right sidebar. The left sidebar shows the table of content for the active page, the previous and next topic and the link to the page source. To not shouw the right sidebar in all the pages set the value to False in the `html_theme_options`."
    "social_icons <list of tupples>", "The social icons to show at the foot of the page, each of the social link should be a tupple of the favicon icon and the link e.g for a social icon of twitter and github. 
   
   .. code:: python 
      
        html_theme_options = [
            'social_icons': [
                ('fab fa-twitter', 'https://twitter.com/iamthecarisma'),
                ('fab fa-github', 'https://github.com/Thecarisma/themata/')
            ]
        ]
    
    "
    "show_navigators <boolean>", "Theme option to decide whether to show the bottom navigation buttons (index, previous and next) at the bottom of each of the generated pages. The default is True which means the navigators is shown. To hide the navigation set the value of show_navigators to False in `html_theme_options`."
    "right_sidebar_only", "An array list of pages name to have only the right sidebar. Any pagename added to this array will have ONLY the right sidebar regardless of other settings. E.g.
    
   .. code:: python 
      
        html_theme_options = [
            'right_sidebar_only': [
                'otherpages/rightpage'
            ]
        ]
    
   The name of the page must be relative to the index project root folder. Another way to make a page have only the right sidebar is to add the extension **.right** to it file name e.g. **test.right.rst**"



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
   /otherpages/leftpage
   

Hackish
========

.. note:: 

    This theme is part of the `themata <https://thecarisma.github.io/themata/>`_ collection.

Setting up and using the hackish theme.

Install the themata package from python index.

.. code:: bash

    pip install themata

or equivalent (add `themata` to any appropriate requirements files).

Example
---------

Below is a minimal sample **conf.py** file to use the hackish theme.

.. code:: python

    import os
    import themata

    project = 'Hackish Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'

    html_favicon = 'favicon.png'
    html_theme_path = [themata.get_html_theme_path()]
    html_theme = 'hackish'

    html_theme_optionss = {
        'project_icon': 'favicon.png'
    }

Theme Options
--------------

The following theme options are accepted in the theme.

Variable Options
'''''''''''''''''

.. csv-table::
   :header: "Option <Datatype>", "Description"

   "project_icon <string>", "The abolute or relative (to _static folder) path to the image to use as the theme icon. This is not the same as favicon. If the favicon is set using the variable `html_favicon` and the project_icon is not set. The project_icon value will be the value of the favicon."
   "index_is_single <boolean>", "This option is to indicate if any **index** page does not have sidebars. It is True by default which means any index page will not have any sidebar. To add sidebars to index pages set the value to False in `html_theme_optionss`."
   "show_navigators_in_index <boolean>", "The theme option to decide whether to show the bottom navigation buttons (index, next, previous) in any **index** page. By default it is False. To show the navigation buttons in index pages set the value to True in the `html_theme_optionss`."
   "navbar_links <list of tupples>", "The navbar menus to show at the header of the page, each of the entry should be a tupple of the name and the link e.g for a menu that link to twitter and github. 
   
   .. code:: python 
      
        html_theme_options = {
            'navbar_links': [
                ('Twitter', 'https://twitter.com/iamthecarisma'),
                ('Github', 'https://github.com/Thecarisma/themata/')
            ]
        }
    
    "
   "has_left_sidebar <boolean>", "By default this theme renders the left sidebar. The left sidebar shows the documentation toc tree. To not shouw the left sidebar in all the pages set the value to False in the `html_theme_options`."
   "footer_menus <list of objects>", "The footer menu to show at the bottom of the page, each of the footer should contain the 'title' and the array of the 'menu_items'. 
   
   .. code:: python 
      
        html_theme_options = {
            'footer_menus': [
                {
                    'title': 'Contact',
                    'menu_items': [
                        {
                            'link': 'https://thecarisma.github.io/',
                            'title': 'https://thecarisma.github.io/'
                        },
                        {
                            'link': 'tel:911',
                            'title': '12345678998'
                        }
                    ]
                },
                {
                    'title': 'Custom Pages',
                    'menu_items': [
                        {
                            'link': 'leftpage.html',
                            'title': 'Left Page'
                        },
                        {
                            'link': 'singletpage.html',
                            'title': 'Single Page'
                        }
                    ]
                }
            ]
        }
    
    "
   "social_icons <list of tupples>", "The social icons to show at the foot of the page, each of the social link should be a tupple of the favicon icon and the link e.g for a social icon of twitter and github. 
   
   .. code:: python 
      
        html_theme_options = {
            'social_icons': [
                ('fab fa-twitter', 'https://twitter.com/iamthecarisma'),
                ('fab fa-github', 'https://github.com/Thecarisma/themata/')
            ]
        }
    
    "
   "show_navigators <boolean>", "Theme option to decide whether to show the bottom navigation buttons (index, previous and next) at the bottom of each of the generated pages. The default is True which means the navigators is shown. To hide the navigation set the value of show_navigators to False in `html_theme_options`."
   "left_sidebar_only <list>", "An array list of pages name to have only the left sidebar. Any pagename added to this array will have ONLY the left sidebar regardless of other sidebar options. E.g.
    
   .. code:: python 
      
        html_theme_options = {
            'left_sidebar_only': [
                'otherpages/leftpage'
            ]
        }
    
   The name of the page must be relative to the index project root folder. Another way to make a page have only the left sidebar is to add the extension **.left** to it file name e.g. **test.left.rst**"
   "no_sidebar <list>", "An array list of pages name to have no sidebar. Any pagename added to this array will have no sidebar regardless of other sidebar options. E.g.
    
   .. code:: python 
      
        html_theme_options = {
            'no_sidebar': [
                'otherpages/singlepage'
            ]
        }
    
   The name of the page must be relative to the index project root folder. Another way to make a page have no sidebar is to add the extension **.single** to it file name e.g. **test.single.rst**"
   "toc_title <string>", "The title of the main toc of the documentation the default is 'Browse'"
   "source_root <string>", "The full link to the web root folder where the source of the documentation source is e.g. the documentation github repo"
   "source_root_edit_text <string>", "The text to show on the button that link to the page source in a repository. The default is '**Edit this page**'"
   "metadata <object>", "Set the metadata values of the generated website. The object should contain any, more or all of the keys, enable, url, type, title, description, image, keywords, author. E.g. 
   
   .. code:: python 
      
        html_theme_options = {
            'metadata': {
                'enable': True,
                'url': 'https://thecarisma.github.io/themata',
                'type': 'website',
                'title': 'Set of Highly customizable sphinx themes.',
                'description': 'Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.',
                'image': 'https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png',
                'keywords': 'python, sphinx, thecarisma, themata, documentation, markdown, rst, themes',
                'author': 'Adewale Azeez'
            }
        }
        
   The result of the theme option above is 

   .. code:: text

      <meta name='description' content='Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.'>
      <meta name='keywords' content='python, sphinx, thecarisma, themata, documentation, markdown, rst, themes'>
      <meta name='author' content='Adewale Azeez'>
      <meta property='og:url' content='https://thecarisma.github.io/themata/' />
      <meta property='og:type' content='website' />
      <meta property='og:title' content='Set of Highly customizable sphinx themes.' />
      <meta property='og:description' content='Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.' />
      <meta property='og:image' content='https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png' />

   If the value of enable is False or not specified the metadata will not be generated."
   "twitter_metadata <object>", "Set the twitter metadata values of the generated website. The object should contain any, more or all of the keys, enable, card, site, creator, title, description, image. E.g. 
   
   .. code:: python 
      
        html_theme_options = {
            'twitter_metadata': {
                'enable': True,
                'card': 'summary',
                'site': '@iamthecarisma',
                'creator': '@iamthecarisma',
                'title': 'Set of Highly customizable sphinx themes.',
                'description': 'Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.',
                'image': 'https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png',
            }
        }
        
   The result of the theme option above is 

   .. code:: text

      <meta name='twitter:card' content='summary' />
      <meta name='twitter:site' content='@iamthecarisma' />
      <meta name='twitter:creator' content='@iamthecarisma' />
      <meta name='twitter:title' content='Set of Highly customizable sphinx themes.' />
      <meta name='twitter:description' content='Themata package contains different sphinx theme that can be easily customized to look like a complete website or just a documentation webpage.' />
      <meta name='twitter:image' content='https://raw.githubusercontent.com/Thecarisma/themata/main/docs/images/themata.small.png' />

   If the value of enable is False or not specified the metadata will not be generated."


CSS Options
'''''''''''''''''

The following theme options are used to style the look of the theme. For example to change the 
background color to gray:
    
.. code:: python

    html_theme_options = {
        'background_color': 'gray'
    }

.. csv-table::
   :header: "Option", "Default", "Description"

   "document_font_size", "16px", "the document font size"
   "text_color", "rgb(36,233,10)", "text color"
   "link_color", "rgb(146,250,131)", "link color"
   "highlight_color", "rgb(36,233,10)", "link hover color"
   "header_background_color", "black", "header background color"
   "background_color", "black", "theme background color"
   "code_background_color", "rgba(255, 255, 255, 0.1)", "pre block background color"
   "search_input_background", "#f7f7f7", "the search box background color"
   "header_sec_background_color", "rgb(0,63,0)", "sec header background color"



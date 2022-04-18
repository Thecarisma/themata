
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
   /otherpages/sidebar
   

Garri
=========

.. note:: 

    This theme is part of the `themata <https://thecarisma.github.io/themata/>`_ collection.

Setting up and using the garri theme.

Install the themata package from python index.

.. code:: bash

    pip install themata

or equivalent (add `themata` to any appropriate requirements files).

Example
---------

Below is a minimal sample **conf.py** file to use the garri theme.

.. code:: python

    import os
    import themata

    project = 'Garri Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'

    html_favicon = 'favicon.png'
    html_theme = 'garri'

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
   "toc_title <string>", "The title of the main toc of the documentation the default is 'Browse'"
   "index_is_single <boolean>", "This option is to indicate if any **index** page does not have sidebars. It is True by default which means any index page will not have any sidebar. To add sidebars to index pages set the value to False in `html_theme_optionss`."
   "sidebar_position <string>", "The position to render the sidebar either left or right. It is left by default. If the value of has_sidebar is set to False no sidebar is rendered."
   "has_sidebar <boolean>", "This option is used to determine whether to show the sidebar or not, the default is True."
   "no_sidebar <list>", "An array list of pages name to have no sidebar. Any pagename added to this array will have no sidebar regardless of other sidebar options. E.g.
    
   .. code:: python 
      
        html_theme_options = {
            'no_sidebar': [
                'otherpages/singlepage'
            ]
        }
    
   The name of the page must be relative to the index project root folder. Another way to make a page have no sidebar is to add the extension **.single** to it file name e.g. **test.single.rst**"
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
   "syntax_highlighter <string>", "The syntax higlighting provider to use for the generated documentation, the following syntax highlighters are supported `ace <https://thecarisma.github.io/themata/syntax_highlighter/ace.html>`_
   `highlightjs <https://thecarisma.github.io/themata/syntax_highlighter/highlightjs.html>`_ `rainbow <https://thecarisma.github.io/themata/syntax_highlighter/rainbow.html>`_
   `prism <https://thecarisma.github.io/themata/syntax_highlighter/prism.html>`_ `Google Prettify <https://thecarisma.github.io/themata/syntax_highlighter/google_prettify.html>`_
   `syntaxhighlighterjs <https://thecarisma.github.io/themata/syntax_highlighter/syntaxhighlighterjs.html>`_ `microlight <https://thecarisma.github.io/themata/syntax_highlighter/microlight.html>`_
   `syntaxyjs <https://thecarisma.github.io/themata/syntax_highlighter/syntaxyjs.html>`_. If syntax_highlighter is not specified the default sphinx highlighter is used."
   "code_block_editable <boolean>", "Specify whether the code block is editable. This only apply to syntax highlighter that support editing the source code e.g. ace. Default is false."
   "syntax_highlighter_theme <string>", "Set the theme your selected syntax highlighter should use. Default value depends on the specified value of syntax_highlighter. 
   The value can be absolute http url to the highlighter theme css e.g. **syntax_highlighter_theme: 'https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-3024.dark.css'**. 
   Visit each of the `syntax highlighter <https://thecarisma.github.io/themata/syntax_highlighter/index.html>`_ page to see their themes"
   "syntax_highlighter_iframe_embed <boolean>", "Specify whether the code block should be render in an iframe element. This is most useful to enforce cutom theme for highlighers that use the last loaded stylesheet e.g. highligherjs. Default is false."
   

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
   "text_color", "#000000", "text color"
   "link_color", "#33658E", "link color"
   "highlight_color", "#33658E", "link hover color"
   "background_color", "white", "theme background color"
   "navbar_color", "#70705C", "navbar background color. Not sure this is used."
   "header_link_color", "#AFAF92", "navbar text color. Not sure this is used."
   "code_background_color", "#EFEFE1", "source code background color"



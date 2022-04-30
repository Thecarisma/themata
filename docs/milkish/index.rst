
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
   

Milkish
========

.. note:: 

    This theme is part of the `themata <https://thecarisma.github.io/themata/>`_ collection.

Setting up and using the milkish theme.

Install the themata package from python index.

.. code:: bash

    pip install themata

or equivalent (add `themata` to any appropriate requirements files).

Example
---------

Below is a minimal sample **conf.py** file to use the milkish theme.

.. code:: python

    import os
    import themata

    project = 'Milkish Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'

    html_favicon = 'favicon.png'
    html_theme = 'milkish'

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
   "has_right_sidebar <boolean>", "By default this theme renders the right sidebar. The left sidebar shows the table of content for the active page, the previous and next topic and the link to the page source. To not shouw the right sidebar in all the pages set the value to False in the `html_theme_options`."
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
   "right_sidebar_only <list>", "An array list of pages name to have only the right sidebar. Any pagename added to this array will have ONLY the right sidebar regardless of other sidebar options. E.g.
    
   .. code:: python 
      
        html_theme_options = {
            'right_sidebar_only': [
                'otherpages/rightpage'
            ]
        }
    
   The name of the page must be relative to the index project root folder. Another way to make a page have only the right sidebar is to add the extension **.right** to it file name e.g. **test.right.rst**"
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
   "collapsible_sidebar <boolean>", "A boolean value to determine whether the left sidebar should be collapsible or not."
   "collapsible_sidebar_display <string>", "The left sidebar unordered list display css value. Set to 'none' if the list should be hidden by default when collapsible_sidebar is set to True, if collapsible_sidebar is set to False rember to remove this option or set it to 'block'."
   "source_root <string>", "The full link to the web root folder where the source of the documentation source is e.g. the documentation github repo"
   "source_root_edit_text <string>", "The text to show on the button that link to the page source in a repository. The default is '**Edit this page**'"
   "metadata <object>", "Set the metadata values of the generated website. The object should contain any, more or all of the keys, enable, url, type, title, description, image, keywords, author. E.g. 
   
   .. code:: python 
      
        html_theme_options = {
            'metadata': {
                'dynamic': True,
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

   If the value of **dynamic** is True the page content will be used to generate some of the metadata, but it still better to add the meta data in the conf.py file for fallback values 
   example for author, and keywords meta values."
   "twitter_metadata <object>", "Set the twitter metadata values of the generated website. The object should contain any, more or all of the keys, enable, card, site, creator, title, description, image. E.g. 
   
   .. code:: python 
      
        html_theme_options = {
            'twitter_metadata': {
                'dynamic': True,
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

   If the value of **dynamic** is True the page content will be used to generate some of the metadata, but it still better to add the meta data in the conf.py file for fallback values 
   example for twitter:site, and twitter:creator meta values."
   "syntax_highlighter <string>", "The syntax higlighting provider to use for the generated documentation, the following syntax highlighters are supported `ace <https://thecarisma.github.io/themata/syntax_highlighter/ace.html>`_
   `highlightjs <https://thecarisma.github.io/themata/syntax_highlighter/highlightjs.html>`_ `rainbow <https://thecarisma.github.io/themata/syntax_highlighter/rainbow.html>`_
   `prism <https://thecarisma.github.io/themata/syntax_highlighter/prism.html>`_ `Google Prettify <https://thecarisma.github.io/themata/syntax_highlighter/google_prettify.html>`_
   `syntaxhighlighterjs <https://thecarisma.github.io/themata/syntax_highlighter/syntaxhighlighterjs.html>`_ `microlight <https://thecarisma.github.io/themata/syntax_highlighter/microlight.html>`_
   `syntaxyjs <https://thecarisma.github.io/themata/syntax_highlighter/syntaxyjs.html>`_. If syntax_highlighter is not specified the default sphinx highlighter is used."
   "code_block_editable <boolean>", "Specify whether the code block is editable. This only apply to syntax highlighter that support editing the source code e.g. ace. Default is false."
   "syntax_highlighter_theme <string>", "Set the theme your selected syntax highlighter should use. Default value depends on the specified value of syntax_highlighter. 
   The value can be absolute http url to the highlighter theme css e.g. **syntax_highlighter_theme: 'https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-3024.dark.css'**. 
   Visit each of the `syntax highlighter <https://thecarisma.github.io/themata/syntax_highlighter/index.html>`_ page to see their themes"
   "syntax_highlighter_iframe_embed <boolean>", "Specify whether the code block should be render in an iframe element. This is most useful to enforce custom theme for highlighers that use the last loaded stylesheet e.g. highligherjs. Default is false."
   "google_analytics_tracking_id <string>", "Google analytics tracking id. If set in the config the tracking script will be added to the webpage."
   "github_repo <string>", "The project github repository if it hosted on github, used for feedback and like."
   "social_share_label <string>", "Title for the social icon share button section. Default is 'Share on'"
   "github_page_feedback_title <string>", "Title for github project and page feedback submission section. Default is 'Submit and view feedback for'"
   "github_page_view_feedbacks_label <string>", "Link text to view all issues related to a webpage on github. Default is 'View all page feedback'"
   "source_root <string>", "Github link to the source folder of the documentation, used to build page source preview and edit links."
   "source_root_edit_text <string>", "Label for the button that link to the page to edit the page source on Github. Default is 'Edit this page'"
   "enable_page_social_share <boolean>", "If set to true the social network share buttons will be added to the webpage. Default is False."
   "enable_github_page_feedback <boolean>", "If set to true the github page and project issue feedback will be generated for the webpages. Default is False."
   "github_feedback_project_template <string>", "The template footer for Github feedback issue creation for project. See `site variables <../site_variables.html>`_ for supported variables."
   "github_feedback_page_template <string>", "The template footer for Github feedback issue creation for a webpage. See `site variables <../site_variables.html>`_ for supported variables."
   "page_rating_options <object>", "This object can be used to create a custom feedback element on a webpage. The following feeds are required for this options 
   
   .. code:: text 
      
        title: The title for the page rating section
        positive_icon: The icon to use for the upvote button, value should be html element. Smiley smile is the deault.
        negative_icon: The icon to use for the downvote button, value should be html element. Smiley sad is the deault.
        positive_event: The raw javasccript code to execute when the upvote icon is clicked, you can use this to call a dynamic aapi to addredd the event.
        negative_event: The raw javasccript code to execute when the downvote icon is clicked, you can use this to call a dynamic aapi to addredd the event.
   
   Sample value in the conf.py file:
   
   .. code:: python
      
        html_theme_options = {
            'page_rating_options': {
                'title': 'Did you find this documentation helpful?',
                'positive_event': 'alert(`Positive`)',
                'negative_event': 'alert(`Negative`)'
            }
        }
        
   In the example above, the upvote button will have the image value, and when click it will alert 'Positive', and for the downvote button when clicked the page will alert 'Negative'."


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
   "text_color", "#727273", "text color"
   "link_color", "#727273", "link color"
   "highlight_color", "#34aeeb", "link hover color"
   "body_link_color", "#34aeeb", "link color in the article body"
   "body_link_highlight_color", "#147eb3", "link hover color in the article body"
   "header_background_color", "#333", "header background color"
   "menu_item_color", "white", "header link text color"
   "background_color", "white", "theme background color"
   "code_background_color", "white", "pre block background color"
   "pre_border_color", "black", "pre block border color"
   "navigator_border_color", "#e6e6e6", "navigation buttons border color"
   "table_background_color", "rgb(223, 226, 229)", "table background color"
   "table_tr_odd_background_color", "black", "odd row background color"
   "table_tr_even_background_color", "rgb(236, 240, 244)", "even row background color"
   "note_background_color", "#eee", "the note div background color"
   "note_border_color", "#ccc", "the note div border color"
   "seealso_background_color", "#ffc", "the seealso div background color"
   "seealso_border_color", "#ff6", "the seealso div border colorr"
   "topic_background_color", "rgb(187, 221, 255)", "the topic div background color"
   "warning_background_color", "#ffe4e4", "the warning div background color"
   "warning_border_color", "#f66", "the warning div border color"
   "footer_link_color", "default", "the footer link color"
   "footer_highlight_color", "default", "the footer link highlight color"



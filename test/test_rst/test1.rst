Basic Specification
=================================

Paragraphs contain text and may contain inline markup: *emphasis*, **strong emphasis**, `interpreted text`, ``inline literals``, standalone hyperlinks (http://www.python.org), external hyperlinks (Python_), internal cross-references (example_), footnote references ([1]_), citation references ([CIT2002]_), substitution references (|example|), and _`inline internal targets`.

``https://verylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtext.com``

Code blocks
=============

Hello world thgis ``is also inline code``

.. code:: c

    #define CESTER_NO_MAIN
    #include <exotic/cester.h>

    CESTER_TEST(test1, test_instance,
        cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);
    )

    CESTER_BODY(
    int main(int argc, char** argv) {
        CESTER_REGISTER_TEST(test1);
        return CESTER_RUN_ALL_TESTS(argc, argv);
    }
    )


List
-------

Bullet lists:
```````````````

- This is a bullet list.

- Bullets can be "*", "+", or "-".


Enumerated lists:
``````````````````

1. This is an enumerated list.

2. Enumerators may be arabic numbers, letters, or roman
   numerals.

Definition lists:
``````````````````

what
    Definition lists associate a term with a definition.

how
    The term is a one-line phrase, and the definition is one
    or more paragraphs or body elements, indented relative to
    the term.

Theme Options
--------------

The following theme options are accepted in the theme.

Variable Options
-----------------

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

Field lists:
``````````````````

:what: Field lists map field names to field bodies, like
       database records.  They are often part of an extension
       syntax.

:how: The field marker is a colon, the field name, and a
      colon.

      The field body may contain one or more body elements,
      indented relative to the field marker.

Option lists, for listing command-line options:
``````````````````````````````````````````````````````````

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too


Literal blocks:
-------------------

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None


Block quotes:
----------------

    This theory, that is mine, is mine.

    -- Anne Elk (Miss)


Simple Table
-----------------
    
.. code:: python

    html_theme_options = {
        'background_color': 'gray'
    }

====================  ==========  ==========
Header row, column 1  Header 2    Header 3
====================  ==========  ==========
body row 1, column 1  column 2    column 3
body row 2            Cells may span columns
====================  ======================

Citation
------------

.. [1] A footnote contains body elements, consistently
   indented by at least 3 spaces.

.. [CIT2002] Just like a footnote, except the label is
   textual.

.. _Python: http://www.python.org

.. |example| function:: module=xml.xslt class=Processor

.. _example:

The "_example" target above points to this paragraph.

.. warning::

	If the output of the tests is directed to a file on a unix, linux variant OS the color 
	bytes will be written into the file along with the test outputs. Use the flag 
	**--cester-nocolor** to disable colored output. Colored output can also be disabled from 
	within the source using the macro **CESTER_NOCOLOR()**.

.. note::

	If the output of the tests is directed to a file on a unix, linux variant OS the color 
	bytes will be written into the file along with the test outputs. Use the flag 
	**--cester-nocolor** to disable colored output. Colored output can also be disabled from 
	within the source using the macro **CESTER_NOCOLOR()**.

.. seealso::

	If the output of the tests is directed to a file on a unix, linux variant OS the color 
	bytes will be written into the file along with the test outputs. Use the flag 
	**--cester-nocolor** to disable colored output. Colored output can also be disabled from 
	within the source using the macro **CESTER_NOCOLOR()**.

.. topic:: themata

	If the output of the tests is directed to a file on a unix, linux variant OS the color 
	bytes will be written into the file along with the test outputs. Use the flag 
	**--cester-nocolor** to disable colored output. Colored output can also be disabled from 
	within the source using the macro **CESTER_NOCOLOR()**.




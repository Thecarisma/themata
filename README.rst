
.. image:: https://github.com/Thecarisma/themata/raw/main/docs/images/themata.small.png
    :alt: Thecarisma.themata
    :width: 90
    :height: 140

themata
########

.. image:: https://img.shields.io/pypi/dw/themata?style=for-the-badge   :alt: PyPI - Downloads   :target: https://pypi.org/project/themata/
.. image:: https://img.shields.io/travis/thecarisma/themata?style=for-the-badge   :alt: Travis (.org) branch   :target: https://travis-ci.org/github/Thecarisma/themata

.. class:: center

    Set of Highly customizable sphinx themes.

Overview
========

This package contains different sphinx theme that can be easily customized to look like 
a complete website or just a documentation webpage.


To use one of the theme install the themata package from python index.

.. code:: bash

    pip install themata

or equivalent (add `themata` to any appropriate requirements files).

The following themes are implemented in the project. Follow the link for detail documentation for
each of the themes.

- `hackish <https://thecarisma.github.io/themata/hackish>`_
- `milkish <https://thecarisma.github.io/themata/milkish>`_
- `fandango <https://thecarisma.github.io/themata/fandango>`_
- `clear <https://thecarisma.github.io/themata/clear>`_
- `fluid <https://thecarisma.github.io/themata/fluid>`_
- `garri <https://thecarisma.github.io/themata/garri>`_
- `water <https://thecarisma.github.io/themata/water>`_
- `sugar <https://thecarisma.github.io/themata/sugar>`_

To use one of the them install the themata package, and specify the theme to use in the **conf.py** 
file. 

Example
---------

To use the milkish theme, set the following option in your **conf.py** file.

.. code:: python

    import os
    import themata

    project = 'First Doc'
    copyright = '2020, Adewale Azeez'
    author = 'Adewale Azeez'
    html_favicon = 'favicon.png'

    html_theme_path = [themata.get_html_theme_path()]
    html_theme = 'milkish'

Each of the themes has theme options to customize the look of the generated pages. The options for 
each of the themes can be view on their documentation page (links above). 

Documentation
-------------

The full documentation is at `https://thecarisma.github.io/themata <https://thecarisma.github.io/themata>`_.
To read the documentation offline run the `gendoc.bat` command in the docs/ folder to generate a 
**dist** folder.

How it works
-------------

In each of the theme folder, the `theme.conf` is used to declare the the defult theme options, the 
`layout.html` file is the template for all the generated pages in the theme. The `__init__.py` 
file is where the theme and it version is added to sphinx. `static\*.css_t` is the cascaded style 
sheet template for the theme.

Contributing
-------------

Fork the project clone the `test <https://github.com/Thecarisma/themata/tree/test>`_ branch 
to view the static test folder which is used as template for the main theme module in 
themata. Copy one of the static folder change the css to suite your need, then make a copy of one 
of the theme in *themata* folder then add your static css file ending with .css_t. Write a 
documentation for the new theme in the *doc* folder. Send in a PR if it OK it will be merged 
into the main project. 

If you have any feature request or issue, open a new issue `here <https://github.com/Thecarisma/themata/issues/new/choose>`_.

Useful Links
-------------

* `Python <https://www.python.org/>`_
* `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_
* `Sphinx Templating <https://www.sphinx-doc.org/en/master/templating.html>`_

License
--------

Creative Commons Zero v1.0 Universal License. Copyright (c) 2020 Adewale Azeez

Change Log 
-----------

1.1
'''''''''

- Remove <no title> from pages with no title. If no title set title to page or project name `731e51d <https://github.com/Thecarisma/themata/commit/731e51dc3999f3fd00594837268e9e98aae27924>`_
- Add theme option to set the document font-size `aefa7ac <https://github.com/Thecarisma/themata/commit/aefa7acbe45d7269773e6bc6c2145a44808a25b2>`_
- Add theme option document font-size to each theme documentation `a474591 <https://github.com/Thecarisma/themata/commit/a4745913506918aaf2eb4bda4ffa7ed12cd62f44>`_
- Put note on top of each theme page that link back to themata `8b3bc8d <https://github.com/Thecarisma/themata/commit/8b3bc8d4ab5f95a05e7566463da6ef4c1d13852d>`_
- Make the document occupy 100% in sugar theme if left and right sidebar is disabled `439fd97 <https://github.com/Thecarisma/themata/commit/439fd9702058d0633114d613079effcdd1376227>`_
- Add optional 'edit this page' button to webpages e.g. edit on github `df0987c <https://github.com/Thecarisma/themata/commit/df0987cbbd355c179df3d886a037f567edaf3d6b>`_
- Add source_root option for the edit on link and source_root_edit_text for the text to display to theme option `df0987c <https://github.com/Thecarisma/themata/commit/df0987cbbd355c179df3d886a037f567edaf3d6b>`_
- Document the source_root and source_root_edit_text theme options `e9ea268 <https://github.com/Thecarisma/themata/commit/e9ea268929293f4eb2b620f0d2e9cd25c4c28476>`_

1.11
'''''''''

- reduce margin and spacing the code block `d942fdb <https://github.com/Thecarisma/themata/commit/d942fdb>`_
- add theme options to customize note, warning, seealso and topic background and border https://github.com/Thecarisma/themata/issues/6 `befd80a <https://github.com/Thecarisma/themata/commit/befd80a>`_
- add the documentation for theme option cutomize the table row background `ba46635 <https://github.com/Thecarisma/themata/commit/ba46635>`_
- fix table overflow, table customization should be done by user with custom css https://github.com/Thecarisma/themata/issues/8 `a02e558 <https://github.com/Thecarisma/themata/commit/a02e558>`_
- add support for metadata and twitter_metadata https://github.com/Thecarisma/themata/issues/9 `79d50a9 <https://github.com/Thecarisma/themata/commit/79d50a9>`_
- add support for metadata and twitter_metadata https://github.com/Thecarisma/themata/issues/9 `21393b4 <https://github.com/Thecarisma/themata/commit/21393b4>`_
- add support for metadata and twitter_metadata https://github.com/Thecarisma/themata/issues/9 `b59ae69 <https://github.com/Thecarisma/themata/commit/b59ae69>`_
- make the title bold and reduce the monstrous padding in code block. https://github.com/Thecarisma/themata/issues/12 `23e5336 <https://github.com/Thecarisma/themata/commit/23e5336>`_
- make the title bold and reduce the monstrous padding in code block `ac160e9 <https://github.com/Thecarisma/themata/commit/ac160e9>`_
- modify the table css to make it look more clean and stylish `36a71d4 <https://github.com/Thecarisma/themata/commit/36a71d4>`_
- change the style of the code rendering `e78e1c7 <https://github.com/Thecarisma/themata/commit/e78e1c7>`_


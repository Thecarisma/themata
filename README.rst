
.. image:: https://github.com/Thecarisma/themata/raw/master/docs/images/themata.small.png
    :alt: Thecarisma.themata
    :width: 90
    :height: 140

themata
########

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
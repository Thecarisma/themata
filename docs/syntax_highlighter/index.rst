

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Syntax Higlighters
   :name: syntax-higlighters-nav

   ace
   highlightjs
   rainbow
   prism
   google_prettify
   syntaxhighlighterjs
   microlight
   syntaxy


Syntax Higlighters 
===================

themata support various syntax highlighter libraries that can be used apart from the default sphinx syntax highligher. The following options are 
accepted by the theme for custom syntax highlighting

.. code:: python
    
    html_theme_options = {
        #...
        'syntax_highlighter': 'syntaxy',
        'code_block_editable': False,
        'syntax_highlighter_theme': 'light',
        #...
    }


- syntax_highlighter: Set the value of the syntax highligher to use, see the :ref:`supported-syntax-higlighters` section for list of supported syntax highligher.
- code_block_editable: If set to True any syntax highligher that support editing the source code will make the code block editable.
- syntax_highlighter_theme: Specify the syntax highligher theme to use, default is github. E.g. if your syntax_highlighter value is 'ace' you can use this field to set the theme to 'monokai'.

In a documentation where the syntax highlighting for the code blocks are different or when you want to make your code blocks 
use different syntax highligher or theme you can specify the syntax_highlighter, code_block_editable and syntax_highlighter_theme in the parameter for your code block e.g.

In the example below the syntax highlighter and theme **(syntaxy with purple theme)** to use for the specific code block is specified in the code tag.

In reStructuredText

.. code:: rst
    
    .. code:: python,syntax_highlighter=syntaxy,code_block_editable=False,syntax_highlighter_theme=purple

        print("Hello World")

In Markdown

.. code:: markdown
    
    ```python,syntax_highlighter=syntaxy,code_block_editable=False,syntax_highlighter_theme=purple
        print("Hello World")
    ```

.. _supported-syntax-higlighters:

Supported Syntax Higlighters
------------------------------

The following syntax highlighers are currently supported in themata. Most of the supported syntax highligher allows to 
specify which theme to use for the code highlight. Click on each syntax highligher below to see their themes.

- `ace <./ace.html>`_
- `highlightjs <./highlightjs.html>`_
- `rainbow <./rainbow.html>`_
- `prism <./prism.html>`_
- `Google Prettify <./google_prettify.html>`_
- `syntaxhighlighterjs <./syntaxhighlighterjs.html>`_
- `microlight <./microlight.html>`_
- `syntaxyjs <./syntaxy.html>`_


Javascript APIs
=================

themata also provide JS functions that can be called in your documentation Javascript file. The following function are available:

- **resolveCodeBlockSyntaxHighlighter(id, language, sh, sht, cbe, embed)**: set/change the syntaxh highlight property of a code block. The parameters are:

    - id: The id of the html code block element
    - language: The code block programming language
    - sh: One of the :ref:`supported-syntax-higlighters`
    - sht: The specific syntax highligher theme. Check the syntax highlighers for their themes
    - cbe: Set whether the code block is editable
    - embed: if set to true the code block will be rendered in it own iframe to force syntaxh highlighting with it theme

- **getThemataCodeEditors()**: get all the ace editor (code blocks) on the page.
- **setThemataCodeEditorMode(mode)**: call this function with the ace mode to set for all the ace editor (code blocks) on the page.
- **setThemataCodeEditorTheme(theme)**: call this function to change all the ace editor (code blocks) theme on a page.
- **setThemataCodeEditorOptions(options)**: change or set the option for all the ace editor (code blocks) theme on a page.
- **themataRegisterJsLoadedCallback(options)**: register a callback function that will be invoke once the themata.js file is loaded.
- **themataRegisterOnloadCallback(cb)**: register a callback function that will be invoke once the page completely loads.


Manual Code Block Integration
------------------------------

Adding the highlight syntax variables to the markdown or rst code block cause sphinx to report *Pygments lexer name* error. To get around this 
the raw html tag can be used to embed a code block and the Javascript APIs above can be used to hightlight the code block with any highlighter and 
theme. Example below

.. code:: rst
    
    .. raw:: html

        <div id="custom-editor" style="min-height: 200px">
            <pre><code>print("Hello World")</pre></code>
        </div>
        <script>
            themataRegisterJsLoadedCallback(() => {
                resolveCodeBlockSyntaxHighlighter(`custom-editor`, "python", "ace", "monokai", true, true);
            });
        </script>


In the example above, the rst raw html tag was used to create a code block for an editable ace editor with monokai theme. In the script 
tag a function is registered which will be called when **themata.js** file is loaded. And finally the function `resolveCodeBlockSyntaxHighlighter` 
is used to highlight the code block by specifying the code block id, programming langauge, the syntax highlight (ace in this example), the syntax 
highligher theme (monokai) and also specify if the code block is editable whihc is true in the example above.

.. note::

    The **code_background_color** theme option is completely ignored if **syntax_highlighter** option is not default 



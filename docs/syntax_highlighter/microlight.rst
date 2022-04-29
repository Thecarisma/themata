
Syntax Higlighter - microlight
=================================

The ace syntax highlighter uses the `microlight <https://asvd.github.io/microlight/>`_ library to render the source code block.


Themes
--------

The following are the supported themes:

.. raw:: html

    <div id="themes-panel" style="display: flex; flex-wrap: wrap;">
        <div style="min-width: 300px; flex: 1; margin: 10px;"><span style="font-weight: bold;"></span>
            <div id="editorx-microlight"><pre><code>html_theme_options = {
        'syntax_highlighter': 'microlight',
        'code_block_editable': False,
    }
    </pre></code>
            </div>
        <div>
    </div>
    <script>
        themataRegisterJsLoadedCallback(() => {
            resolveCodeBlockSyntaxHighlighter(`editorx-microlight`, "python", "microlight", "", false, false);
        });
    </script>




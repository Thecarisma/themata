
Syntax Higlighter - syntaxhighlighterjs
==========================================

The ace syntax highlighter uses the `syntaxhighlighterjs <https://o7planning.org/10375/highlighting-code-with-syntaxhighlighter-javascript-library>`_ library to render the source code block.

.. warning::

    syntaxhighlighterjs does not render the code block in embeded iframe mode, reason unknown.
    This is likely due to how or when syntaxhighlighterjs renderes the code block.

Themes
--------

The following are the supported themes:

.. raw:: html

    <div id="themes-panel" style="display: flex; flex-wrap: wrap;"></div>
    <script>
        themataRegisterJsLoadedCallback(() => {
            let themes = [ 
                "Default", "Django", "Eclipse", "Emacs", "FadeToGrey", "MDUltra", "Midnight", "RDark"
            ];
            let themesPanel = get("themes-panel");
            for (let index = 0; index < themes.length; index++) {
                let theme = themes[index];
                themesPanel.innerHTML += `<div style="min-width: 300px; flex: 1; margin: 10px;"><span style="font-weight: bold;">${theme}</span>
                <div id="editorx-${theme}"><pre><code>html_theme_options = {
        'syntax_highlighter': 'syntaxhighlighterjs',
        'code_block_editable': False,
        'syntax_highlighter_theme': '${theme}',
    }
    </pre></code>
                </div><div>`;
            }
            for (let theme of themes) {
                resolveCodeBlockSyntaxHighlighter(`editorx-${theme}`, "python", "syntaxhighlighterjs", theme, false, true);
            }
        });
    </script>




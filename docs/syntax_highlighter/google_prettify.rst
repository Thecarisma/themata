
Syntax Higlighter - Google Prettify
====================================

The ace syntax highlighter uses the `google_prettify <https://github.com/googlearchive/code-prettify>`_ library to render the source code block.


Themes
--------

The following are the supported themes:

.. raw:: html

    <div id="themes-panel" style="display: flex; flex-wrap: wrap;"></div>
    <script>
        themataRegisterJsLoadedCallback(() => {
            let themes = [ 
                "default", "desert", "sunburst", "sons-of-obsidian", "doxy"
            ];
            let themesPanel = get("themes-panel");
            for (let index = 0; index < themes.length; index++) {
                let theme = themes[index];
                themesPanel.innerHTML += `<div style="min-width: 300px; flex: 1; margin: 10px;"><span style="font-weight: bold;">${theme}</span>
                <div id="editorx-${theme}"><pre><code>html_theme_options = {
        'syntax_highlighter': 'google_prettify',
        'code_block_editable': False,
        'syntax_highlighter_theme': '${theme}',
    }
    </pre></code>
                </div><div>`;
            }
            for (let theme of themes) {
                resolveCodeBlockSyntaxHighlighter(`editorx-${theme}`, "python", "google_prettify", theme, false, true);
            }
        });
    </script>




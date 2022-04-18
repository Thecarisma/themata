
Syntax Higlighter - rainbow
=================================

The ace syntax highlighter uses the `rainbow <https://craig.is/making/rainbows>`_ library to render the source code block.


Themes
--------

The following are the supported themes:

.. raw:: html

    <div id="themes-panel" style="display: flex; flex-wrap: wrap;"></div>
    <script>
        themataRegisterJsLoadedCallback(() => {
            let themes = [ 
                "all-hallows-eve", "blackboard", "dreamweaver", "espresso-libre", "github", "kimbie-dark",
                "kimbie-light", "monokai", "obsidian", "paraiso-dark", "paraiso-light", "pastie",/* "rainbow",*/ "solarized-dark",
                "solarized-light", "sunburst", "tomorrow-night", "tricolore", "twilight", "zenburnesque"
            ];
            let themesPanel = get("themes-panel");
            for (let index = 0; index < themes.length; index++) {
                let theme = themes[index];
                themesPanel.innerHTML += `<div style="min-width: 300px; flex: 1; margin: 10px;"><span style="font-weight: bold;">${theme}</span>
                <div id="editorx-${theme}"><pre><code>html_theme_options = {
        'syntax_highlighter': 'rainbow',
        'code_block_editable': False,
        'syntax_highlighter_theme': '${theme}',
    }
    </pre></code>
                </div><div>`;
            }
            for (let theme of themes) {
                resolveCodeBlockSyntaxHighlighter(`editorx-${theme}`, "python", "rainbow", theme, false, true);
            }
        });
    </script>




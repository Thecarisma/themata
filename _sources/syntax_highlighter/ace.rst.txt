
Syntax Higlighter - ace
=========================

The ace syntax highlighter uses the `ace <https://ace.c9.io/>`_ editor library to render the source code block.


Themes
--------

The following are the supported themes:

.. raw:: html

    <div id="themes-panel" style="display: flex; flex-wrap: wrap;"></div>
    <script>
        themataRegisterJsLoadedCallback(() => {
            let themes = [ 
                "chrome", "clouds", "crimson_editor", "dawn", "dreamweaver", "eclipse", "github", "iplastic", 
                "solarized_light", "textmate", "tomorrow", "xcode", "kuroir", "katzenmilch", "sqlserver", "ambiance",
                "chaos", "clouds_midnight", "dracula", "cobalt", "gruvbox", "gob", "idle_fingers", "kr_theme", "merbivore",
                "merbivore_soft", "mono_industrial", "monokai", "nord_dark", "one_dark", "pastel_on_dark", "terminal", "tomorrow_night",
                "tomorrow_night_blue", "tomorrow_night_bright", "tomorrow_night_eighties", "twilight", "vibrant_ink"
            ];
            let themesPanel = get("themes-panel");
            for (let index = 0; index < themes.length; index++) {
                let theme = themes[index];
                themesPanel.innerHTML += `<div style="min-width: 300px; flex: 1; margin: 10px;"><span style="font-weight: bold;">${theme}</span>
                <div id="editorx-${theme}"><pre><code>html_theme_options = {
        'syntax_highlighter': 'highlightjs',
        'code_block_editable': False,
        'syntax_highlighter_theme': '${theme}',
    }
    </pre></code>
                </div><div>`;
            }
            for (let theme of themes) {
                resolveCodeBlockSyntaxHighlighter(`editorx-${theme}`, "python", "ace", theme, false, true);
            }
        });
    </script>


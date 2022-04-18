
Syntax Higlighter - prism
=================================

The ace syntax highlighter uses the `prism <https://prismjs.com/>`_ library to render the source code block.


Themes
--------

The following are the supported themes:

.. raw:: html

    <div id="themes-panel" style="display: flex; flex-wrap: wrap;"></div>
    <script>
        themataRegisterJsLoadedCallback(() => {
            let themes = [ 
                "default", "coy", "dark", "funky", "okaidia", "solarizedlight", "tomorrow", "twilight", 
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-3024.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-apathy.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-ashes.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-bespin.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-brewer.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-bright.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-chalk.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-colors.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-default.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-eighties.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-embers.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-flat.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-google.light.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-grayscale.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-greenscreen.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-harmonic16.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-hopscotch.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-isotope.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-marrakesh.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-mocha.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-monokai.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-ocean.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-paraiso.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-pop.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-railscasts.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-shapeshifter.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-shapeshifter.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-solarized.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-solarized.light.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-summerfruit.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-tomorrow.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-londontube.dark.css",
                "https://atelierbram.github.io/syntax-highlighting/prism/demo/assets/css/prism-base16-twilight.dark.css",
            ];
            let themesPanel = get("themes-panel");
            for (let index = 0; index < themes.length; index++) {
                let theme = themes[index];
                themesPanel.innerHTML += `<div style="min-width: 300px; flex: 1; margin: 10px;"><span style="font-weight: bold;">${theme}</span>
                <div id="editorx-${theme}"><pre><code>html_theme_options = {
        'syntax_highlighter': 'prism',
        'code_block_editable': False,
        'syntax_highlighter_theme': '${theme}',
    }
    </pre></code>
                </div><div>`;
            }
            for (let theme of themes) {
                resolveCodeBlockSyntaxHighlighter(`editorx-${theme}`, "python", "prism", theme, false, true);
            }
        });
    </script>




import os

__version_trait = (1, 0, 0)
__version = ".".join(map(str, __version_trait))

def get_path():
    """
    Return the path to the sugar theme
    """
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context["sugar_version"] = __version


def setup(app):
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("sugar", theme_path)
    app.connect("html-page-context", update_context)
    return {"version": __version}
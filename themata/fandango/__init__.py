import os
import themata

def get_path():
    """
    Return the path to the fandango theme
    """
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def setup(app):
    if hasattr(app, "add_html_theme"):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme("fandango", theme_path)
    app.connect("html-page-context", themata.update_context)
    app.connect('build-finished', themata.copy_custom_files)
    return {"version": themata.__version}
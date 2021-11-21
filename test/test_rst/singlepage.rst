Hello
-----

Sphinx will look for templates in the folders of templates_path first, and if it can’t find the template it’s looking for there, it falls back to the selected theme’s templates.

A template contains variables, which are replaced with values when the template is evaluated, tags, which control the logic of the template and blocks which are used for template inheritance.

Sphinx’s basic theme provides base templates with a couple of blocks it will fill with data. These are located in the themes/basic subdirectory of the Sphinx installation directory, and used by all builtin Sphinx themes. Templates with the same name in the templates_path override templates supplied by the selected theme.

For example, to add a new link to the template area containing related links all you have to do is to add a new template called layout.html with the following contents:


=============
final stdout
=============
**Source**: final stdout Source.
    
    The standard output stream is the default destination of output for console programs. It is usually directed 
    by default to the text console (generally, on the screen) which can be the terminal. 
    
    Although it is commonly  assumed that the default destination for stdout is going to be the screen, this may 
    not be the case even in regular console systems, since stdout can generally be redirected on most operating 
    systems at the time of invoking the application. For example, many systems, among them DOS/Windows and most 
    UNIX shells, support the following command syntax :
    
    ::
    
      theprogram > output.txt
    
    to redirect the output of **theprogram** to the file **output.txt** instead of the console.
    
    .. note::
      The stdout stream cannot be closed in order to prevent error while trying to write to it later, instead 
      of closing the stream the stdout stream will be flushed instead

    
    .. warning::
      The stdout stream cannot be closed in order to prevent error while trying to write to it later, instead 
      of closing the stream the stdout stream will be flushed instead

    
    .. seealso::
      The stdout stream cannot be closed in order to prevent error while trying to write to it later, instead 
      of closing the stream the stdout stream will be flushed instead


.. image:: https://github.com/Thecarisma/themata/raw/master/docs/images/themata.png
    :alt: About to make the tackle, Yale Alumni Game 2017
    :align: center

Templating
----------

Sphinx uses the Jinja templating engine for its HTML templates. Jinja is a text-based engine, and inspired by Django templates, so anyone having used Django will already be familiar with it. It also has excellent documentation for those who need to make themselves familiar with it.

Do I need to use Sphinx’s templates to produce HTML?
No. You have several other options:

You can write a TemplateBridge subclass that calls your template engine of choice, and set the template_bridge configuration value accordingly.

You can write a custom builder that derives from StandaloneHTMLBuilder and calls your template engine of choice.

You can use the PickleHTMLBuilder that produces pickle files with the page contents, and postprocess them using a custom tool, or use them in your Web application.

Jinja/Sphinx Templating Primer
The default templating language in Sphinx is Jinja. It’s Django/Smarty inspired and easy to understand. The most important concept in Jinja is template inheritance, which means that you can overwrite only specific blocks within a template, customizing it while also keeping the changes at a minimum.

To customize the output of your documentation you can override all the templates (both the layout templates and the child templates) by adding files with the same name as the original filename into the template directory of the structure the Sphinx quickstart generated for you.


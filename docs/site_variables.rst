
Site Variables
=========================

themata support varaibles expansion on a webpage. In the documentation some webpage or website specific information such as 
the webpage title, project url origin, the webpage source code location, the webpage absolute url are not available. themata allows 
that such variables can be added to the webpage and the value will be set/expanded during the documentation build phase. 

The following self explanatory variables are supported:

- **__themata_base_url__E**: The base url of the project, e.g. __themata_base_url__
- **__themata_page_url__E**: The the active page fabsolute url e.g. __themata_page_url__
- **__themata_project__E**: The project name e.g. __themata_project__
- **__themata_project_github_location__E**: The project github location e.g. __themata_project_github_location__
- **__themata_current_page_path__E**: The path of the page in the folder plus the prefix, e.g. *__themata_current_page_path__*
- **__themata_current_page_location__E**: The active page github blob location e.g. e.g. __themata_current_page_location__
- **__themata_current_page_title__E**: The title of the page e.g. *__themata_current_page_title__*

If any of the variables above is find in the following location on a wwebsite it ll be expanded.

- em - `<em>__themata_page_url__E</em>`
- strong - `<strong>__themata_page_url__E</strong>`
- span value - `<span>This project <__themata_project__E> is part of exotic libraries</span>`
- paragraph - `<p>The page title is '__themata_current_page_title__E' </p>`
- div - `<div>The page title is '__themata_current_page_title__E' </div>`
- link text and href - `<a href="__themata_current_page_location__E">view source</a>`
- github page and project feedback templates options - `github_feedback_project_template`, `github_feedback_page_template`


Ignoring Expansion
--------------------

If you do not want the variable to be expanded append **E** at the end of the variable. e.g. **__themata_base_url__EE** will not be expanded it'll be 
expanded to **__themata_base_url__** instead removing the **E** prefix.

.. warning::

    Having so much site variables on a webpage can cause noticeable lag on the page load, as the expansion occur in a loop.
    No how many site variables is too much, like 800 and above. So 


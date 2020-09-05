Basic Specification
=================================

Paragraphs contain text and may contain inline markup: *emphasis*, **strong emphasis**, `interpreted text`, ``inline literals``, standalone hyperlinks (http://www.python.org), external hyperlinks (Python_), internal cross-references (example_), footnote references ([1]_), citation references ([CIT2002]_), substitution references (|example|), and _`inline internal targets`.

``https://verylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtextverylongtext.com``

Code blocks
=============

Hello world thgis ``is also inline code``

.. code:: c

    #define CESTER_NO_MAIN
    #include <exotic/cester.h>

    CESTER_TEST(test1, test_instance,
        cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);cester_assert_equal(NULL, NULL);
    )

    CESTER_BODY(
    int main(int argc, char** argv) {
        CESTER_REGISTER_TEST(test1);
        return CESTER_RUN_ALL_TESTS(argc, argv);
    }
    )


List
-------

Bullet lists:
```````````````

- This is a bullet list.

- Bullets can be "*", "+", or "-".


Enumerated lists:
``````````````````

1. This is an enumerated list.

2. Enumerators may be arabic numbers, letters, or roman
   numerals.

Definition lists:
``````````````````

what
    Definition lists associate a term with a definition.

how
    The term is a one-line phrase, and the definition is one
    or more paragraphs or body elements, indented relative to
    the term.

Field lists:
``````````````````

:what: Field lists map field names to field bodies, like
       database records.  They are often part of an extension
       syntax.

:how: The field marker is a colon, the field name, and a
      colon.

      The field body may contain one or more body elements,
      indented relative to the field marker.

Option lists, for listing command-line options:
``````````````````````````````````````````````````````````

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too


Literal blocks:
-------------------

    if literal_block:
        text = 'is left as-is'
        spaces_and_linebreaks = 'are preserved'
        markup_processing = None


Block quotes:
----------------

    This theory, that is mine, is mine.

    -- Anne Elk (Miss)


Simple Table
-----------------

====================  ==========  ==========
Header row, column 1  Header 2    Header 3
====================  ==========  ==========
body row 1, column 1  column 2    column 3
body row 2            Cells may span columns
====================  ======================

Citation
------------

.. [1] A footnote contains body elements, consistently
   indented by at least 3 spaces.

.. [CIT2002] Just like a footnote, except the label is
   textual.

.. _Python: http://www.python.org

.. |example| function:: module=xml.xslt class=Processor

.. _example:

The "_example" target above points to this paragraph.

.. warning::

	If the output of the tests is directed to a file on a unix, linux variant OS the color 
	bytes will be written into the file along with the test outputs. Use the flag 
	**--cester-nocolor** to disable colored output. Colored output can also be disabled from 
	within the source using the macro **CESTER_NOCOLOR()**.

.. note::

	If the output of the tests is directed to a file on a unix, linux variant OS the color 
	bytes will be written into the file along with the test outputs. Use the flag 
	**--cester-nocolor** to disable colored output. Colored output can also be disabled from 
	within the source using the macro **CESTER_NOCOLOR()**.




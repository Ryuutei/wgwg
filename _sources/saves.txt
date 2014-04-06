.. template for ReST
    toctree:
    Entries (titles directly)
    :maxdepth: 2
    :numbered:
    :titlesonly:
    :glob:  (files and folders)
    :hidden:

    .. math:: (a + b)^2 = a^2 + 2ab + b^2
        :label: truc \n
    some other paragraph with :eq:`truc` which ref. or :math:`inline maths`

    `hyperlink <http://stuff.com>`_
    hyperlink_
    .. _hyperlink: http://stuff.com

    footnote ref[n]_.
        .. [n] footnote stuff with no : after "[n]"

    :download:`title <file>`
    :ref:`text : to be linked` # will link to :
    .. _text \: to be linked:

    Word
        to define.
    r"""raw python like line"""
    #. auto enumerated stuff.
    #. auto enumerated stuff.
    .. image:: path/image.png
    .. NAME image:: path/image.png   // then after refered as |NAME|
    Titles, chapter and paragraphs :
    # with overline, for parts
    * with overline, for chapters
    =, for sections
    _, for subsections
    -, for sub-subsections
    ^, for sub-sub-subsections
    ", for paragraphs

.. index::
.. |date| date:: %Y/%m/%d
.. |time| date:: %H:%M

:Author:
:Site: `x `_
:Date:
:Source:
:Edition: |date| à |time|
:Version: 1.0


::

    ~/Library/Application Support/Google Earth /Applications/Games/Google\ Earth.app


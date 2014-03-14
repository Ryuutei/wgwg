.. -*- coding: utf-8 -*-
    template for ReST

.. index:: RPG, Aventure

Bastion
=======

.. |lin| image:: ../img/linux.svg
.. |osx| image:: ../img/osx.svg
.. |win| image:: ../img/windows.svg
.. |and| image:: ../img/android.svg

:Plateforme: |win| |osx| |lin|


Sauvegardes Mac OSX
-------------------

::

    Library/Application Support/com.wb.Bastion/






.. aide memoire for ReST
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



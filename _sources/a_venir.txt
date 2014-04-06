.. -*- coding: utf-8 -*-
    template for ReStructured Text
    by Ryuutei 〔ryuutei@gmail.com〕〔http://ryuutei.wordpress.com/〕

.. |date| date:: %Y/%m/%d
.. |time| date:: %H:%M

.. index::

Liste des jeux a venir
======================

:Author: Julien B.
:Edition: |date| à |time|
:Version: α 1.2
:Status: Brouillon

.. toctree::
    :maxdepth: 3

    videogames.rst




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



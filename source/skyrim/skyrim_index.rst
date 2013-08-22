.. template for ReST
    *emphasise* 
    **Bold**
    ``inline literal``
    `hyperlink <http://stuff.com>`_
    footnote ref[n]_.
        .. [n] footnote stuff with no : after "[n]"
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
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

.. index:: The Elder Scrolls, FPS, Solo

The Elder Scrolls V: Skyrim
===========================

:Author: Julien B.
:Date: 2013/08/15 19:50:44 +0200
:Version: 1.0

La section Alchimie a été créée car les autres sources internet sont erronées, et la version française inclue beaucoup d'erreurs diverses, de duplicata et de classement (ℯℊ. les 'é' sont rangés à la fin de la liste dans le jeu.)


.. toctree::
    alchimie.rst


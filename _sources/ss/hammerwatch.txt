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

.. index:: network

Hammerwatch
===========

**Server & Multiplayer**

* **UDP** [*]_ 9995

.. [*] 2013/08/27: il est etrange que malgres que le port externe dans un reseau local le jeu arrive a publier les parties sur l'internet. Plus encore forwarding un tunnel ne permet pas de joindre une partie. A parement `Hammerwatch utilise une connection uPnP <http://steamcommunity.com/workshop/filedetails/discussion/122788084/846962439206314705/>`_ et necessite l'ouverture des ports 9995 sur les deux machines. Du coup je ne sais pas pour le moment interfacer ce truc.

* -2013/08/25 Etant donne tous les problemes de syncronisation que le je possede, il est probable que le protocol soit TCP. Ouvrez les deux protocol au cas ou.-

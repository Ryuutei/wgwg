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

.. index:: strategie, mods, install notes

Command & Conquer 3
===================

Raccouci pour un MOD
--------------------


Comment Créer un raccourci pour un MOD Command and Conquer 3 Les Guerres du Tiberium :

Pour éviter d’avoir a passer par le menu de gestion des mods de Command and Conquer 3 pour lancer un MOD, il faut faire un raccourcis de ce genre :

**Cible** :

::

     C:\C&C3\cnc3.exe -modConfig "C:\Documents and Settings\<NOM D’UTILISATEUR>
        \My Documents\Command & Conquer 3 Tiberium Wars\mods\<NOM DU MOD>\<NOM DU MOD>.skudef"

**Demarre dans** :

::

    C:\Documents and Settings\<NOM D’UTILISATEUR>\My Documents
        \Command & Conquer 3 Tiberium Wars\mods\<NOM DU MOD>\"


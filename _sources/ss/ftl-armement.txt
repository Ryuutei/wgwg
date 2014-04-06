.. -*- coding: utf-8 -*-
    template for ReStructured Text
    by Ryuutei 〔ryuutei@gmail.com〕〔http://ryuutei.wordpress.com/〕

.. |date| date:: %Y/%m/%d
.. |time| date:: %H:%M

Armement
========

:Author: Sebastien Blanc 龍帝〔ryuutei.at.work@gmail.com〕
:Site: `Ryuutei's Blog <http://ryuutei.wordpress.com/>`_
:Date: 2014-04-06 03:13:16 PM +0200
:Edition: |date| à |time|
:Version: 1.1


**Legende:**

- € : Cout de pièces détachées a l'achat.
- ⚡︎ : Consommation d'énergie du système.
- ⌛︎ : Chargement de l'arme en secondes.
- ☠ : Dégâts que l'arme de....
- × : Nombre de tirs de de l'arme.
- ␣ : Longueur du rayon. (Beams seulement)
- 🔓 : Chances de créer une brèche.
- 🔥 : Chances de créer un incendie.
- ☆ : Étourdis l'équipage.
- Notes Spéciales : détails, autres bonus.

**Brèches, Incendies, Etourdissements:**

    0. NA
    1. Faible
    2. Moyen
    3. Élevé

Lasers
------

.. OLD : Lasers                  Cout    Energie Charge      Tirs Dommages   Brèche  Incendies Notes Speciales

======================= === === === === === === === === =======================================================================
Nom                     €   ⚛   ⌛︎   ×   ☠   🔓   🔥   ☆   Notes Spéciales
======================= === === === === === === === === =======================================================================
Basic Laser Mk1         0   1   10  1   1   0   1   ?   ␀
Dual Lasers             25  1   10  2   1   0   1   ?   ␀
Burst Laser Mk1         50  2   11  2   1   0   1   ?   ␀
Burst Laser Mk2         80  2   12  3   1   0   1   ?   ␀
Burst Laser Mk3         110 4   19  5   1   0   0   ?   ␀
Heavy Laser Mk1         55  1   9   1   2   1   1   ?   ␀
Heavy Laser Mk2         75  3   13  2   2   1   1   ?   ␀
Hull Smasher Laser      65  2   14  2   1   1   0   ?   ×2 Salles normales
Hull Smasher Laser Mk2  100 3   15  3   1   1   1   ?   ×2 Salles normales

Laser Charger (S) [AE]_ 55  2   6   1   1   0   0   ?   Peu contenir 2 charges (tire des que possible en mode tire auto.)
Laser Charger (L) [AE]_ ?   3   5   1   1   0   1   ?   Peu contenir 4 charges (tire des que possible en mode tire auto.)
Chain Burst Laser [AE]_ 65  2   16  2   1   0   1   ?   Diminue le temps de charge apres chaque tir jusqu'a 7 secondes.

======================= === === === === === === === === =======================================================================


Rayons（Beams）
---------------

======================= === === === === === === === === =======================================================================
Nom                     €   ⚛   ⌛︎   ␣   ☠   🔓   🔥   ☆   Notes Spéciales
======================= === === === === === === === === =======================================================================
Mini Beam               50  1   12  3   1   0   1   ?   Seulement pour le Nessasio
Pike Beam               60  2   16  6   1   0   0   ?   ␀
Halberd Beam            70  3   17  4   2   1   0   ?   ␀
Fire Beam               70  2   20  5   0   0   3   ?   ␀
Hull Beam               70  2   14  3-4 1-2 1   0   ?   ×2 Salles normales
Glaive Beam             120 4   25  4-5 3   0   0   ?   Passe Boucliers [S]_
Anti-Bio Beam           50  2   16  5   0   0   0   ?   - 60 dommages/equipage
                                                        - 30 dommages/drones
Artillery Beam          0   1-4 50  5   ?   0   2   ?   Arme speciale de la classe Osprey. Perce bouclier.
======================= === === === === === === === === =======================================================================

.. [S] Perds 1 de dommage a chaque couche de bouclier passé.

Missiles
--------

======================= === === === === === === === === =======================================================================
Nom                     €   ⚛   ⌛︎   ×   ☠   🔓   🔥   ☆   Notes Spéciales
======================= === === === === === === === === =======================================================================
Leto Missiles           0   1   9   1   1   1   1   ?
Artemis Missiles        38  2   10  1   2   1   1   ?   - ×5 Perce Bouclier
Artemis Missiles [α]_   0   1   11  1   2   1   1   ?   - ×5 Perce Bouclier
Hermes Missiles         50  3   14  1   3   1   1   ?   - ×5 Perce Bouclier
                                                        - ×2 Systemes ⁇
Breach Missiles         70  3   22  1   4   3   1   ?   - ×5 Perce Bouclier
Hull Missiles           75  2   17  1   2   1   1   ?   - ×5 Perce Bouclier
                                                        - ×2 Salles normales.
                                                        - Equipé sur le Bulwark
Pegasus Missile         80  3   20  2   2   1   1   ?   - Tire deux missiles pour le prix d'un.
Swarm                   85  2   7   1   1   1   1   0   Peu contenir 3 charges (tire des que possible en mode tire auto.)
======================= === === === === === === === === =======================================================================

.. [α] Missile Artemis special du Kestrel et du Bulvark.

Bombes
------

======================= === === === === === === === === =======================================================================
Nom                     €   ⚛   ⌛︎   ×   ☠   🔓   🔥   ☆   Notes Spéciales
======================= === === === === === === === === =======================================================================
Healing Burst           40  1   18  1   0   0   0   ?   ⚠ Soigne l'equipage de 150
Small Bomb              55  1   13  1   2   0   1   ?   - 2 dommages sur les systèmes.
                                                        - 2 dommages sur l'equipage.
Fire bomb               55  2   15  1   2   0   3   ?
Ion Bomb                65  1   18  1   0   0   0   ?   4 Dommages Ion.
Breach Bomb 1           70  1   9   1   1   3   0   ?   2 de dommages sur le personel.
Breach Bomb 2           70  2   17  1   3   3   1   ?   - 0 dommage sur salles normales
                                                        - 3 dommages sur le personnel.
                                                        - 3 dommages sur les systèmes.
Crystal lockdown Bomb   60  1   15  1   0   0   0   ?   Bloque la salle.
======================= === === === === === === === === =======================================================================

Ions
----

======================= === === === ======= === === === === =======================================================================
Nom                     €   ⚛   ⌛︎   ×       ☠   🔓   🔥   ☆   Notes Spéciales
======================= === === === ======= === === === === =======================================================================
Ion Blast               30  1   8   1       1   0   0   ?   ␀
Ion Blast 2             30  3   4   1       3   0   0   ?   ␀
Heavy Ion               40  2   13  1       2   0   0   ?   ␀
Ion Stunner [AE]_       35  1   10  1       1   0   0   1   ␀
Ion Charger [AE]_       50  2   6   [*]_    1   0   0   0   ␀
Chain Ion   [AE]_       55  3   14  1       1-4 0   0   0   +1 de dommages a chaque tirs. (4 max)
======================= === === === ======= === === === === =======================================================================

.. [*] Ion Charger: peu contenir 3 charges (tire des que possible en mode tire auto.)

Flak
----

Tous les Flak guns ne sont accessibles que sur la Advanced Edition de FTL, avec l'option de jeu activée.

======================= === === === === === === === === =======================================================================
Nom                     €   ⚛   ⌛︎   ×   ☠   🔓   🔥   ☆   Notes Spéciales
======================= === === === === === === === === =======================================================================
Flak Gun 1              65  2   10  3   1   0   1   0   ␀
Flak Gun 2              85  3   21  7   1   0   1   0   ␀
Advanced Flak Gun       ?   1   8   3   1   0   1   0   Plus petite surface d'impact
======================= === === === === === === === === =======================================================================

****

.. [AE] Advanced Edition


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

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

.. index:: JSON,

Command Block
-------------

**Basics**

    * ``@a`` : all players on the server.
    * ``@p`` : nearest player
    * ``@r`` : random player

``give <player> <object> <amount> <datavalue>``

``clear <player> <object> <datavalue>``

*difficulty*

    * ``0`` : peaceful
    * ``1`` : easy
    * ``2`` : nornal
    * ``3`` : hard

``gademode <mode> <player>``

``say <msg>``
``tell <player> <msg>``

``spawnpoint <player> <X> <Y> <Z>``

``time set <value>``
``time add <value>``

*weather*

    * clear
    * rain
    * thunder

``xp <+/-value> <player>``

*filtering*

[r=<value>]

    * ``r`` :  radius
    * ``rm`` :  radius min

    * ``l`` :  level
    * ``lm`` :  level min

    * ``m`` : game mode
    * ``c`` : count

    * ``x``
    * ``y``
    * ``z``
    * ``r``

``testfor``

**Advanced**

cf. `sethbling <http://youtu.be/Ujls92b-hUw>`_

``/setblock <x> <y> <z> <TileName> [dataValue] [oldBlockHandling] [dataTag]``

``/testforblock <x> <y> <z> <TileName> [dataValue] [dataTag]``

::

    /tellraw @a {"text":"Do you want an apple? ", "extra": [{"text":"[OK]","color":"red","clickEvent": {"action":"run_command","value":"/give @p 260"}, "hoverEvent":{"action":"show_text","value":"I really do"}}]}


::

    /tellraw @a {"text": "Click on the item to buy it: ", "extra": [{"text": "Dinner's Bone", "clickEvent": {"action": "run_command", "value": "/give @p bone 1 0 {display:{Name:\"Dinners Bone\"}}"}, "hoverEvent": {"action": "show_item", "value": "{id:352s,Damage:0s,Count:1b,tag:{display:{Name:\"Dinner's Bone\"}}}"}}]}

Score Board
:::::::::::

`video explicative <https://www.youtube.com/watch?v=NTrViboaGgE>`_

`Plus d'infos <http://www.minecraftwiki.net/wiki/Scoreboard>`_

/scoreboard objectives add [name for objective] [objective] [display name]
/scoreboard objectives setdisplay [display location] [name for objective]
/scoreboard players add / remove @p [name for objective] [amount]
/scoreboard players set @p [name for objective] [amount]
/scoreboard players reset @a
/testfor @p[score_GameVar_min=2,score_GameVar=2,s­core_Lives_min=0,score_Lives=0]
/scoreboard teams join team player
/scoreboard teams leave team player
/scoreboard teams empty team
/scoreboard teams option [team] [friendlyfire|color] [value]


`Changelog 13w37a <http://www.reddit.com/r/Minecraft/comments/1m8xcj/minecraft_snapshot_13w37a/>`_

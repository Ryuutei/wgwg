.. index:: Stratégie, Simulation, Roguelike-like, FTL：Faster Than Light, 

.. |lin| image:: ../img/linux.svg
.. |osx| image:: ../img/osx.svg
.. |win| image:: ../img/windows.svg
.. |and| image:: ../img/android.svg

FTL：Faster Than Light（Advanced Edition）
==========================================

:Plateforme: |win| |osx| |lin|

.. image:: ../img/The_Kestrel_Logo_FINAL.svg
    :align: center
    :width: 256 px

Fichiers de sauvegardes
-----------------------

Les fichiers ``continue.sav`` et ``prof.sav`` contiennent respectivement la sauvegarde de sortie de jeu et les achievements, unlocks & hi-score

* Windows: ``%USERPROFILE%/My Documents/My Games/FasterThanLight``
* Mac: ``~/Library/Application Support/FasterThanLight/``
* Linux: ``~/.local/share/FasterThanLight/`` or ``$XDG_DATA_HOME/FasterThanLight`` (The latter being for non-default XDG_DATA_HOME settings.)

.. toctree::
    ftl-armement.rst
    ftl-vaisseaux.rst

.. image:: ../img/ftl-ks-engi.gif
    :align: center

Hacking
-------

::

    # Header
     4 bytes (32bit int)        Version

     # Achievements
     4 bytes (32bit int)        Number of achievements

      # Begin achievement unlock (repeated for each achievement unlocked -- 'Number of achievements')
      4 bytes (32bit int)        String Length (Achievement name)
      n bytes (char *)           Achievement name
      4 bytes (32bit int)        Achievement unlocked on easy or normal (Easy: 00, Normal: 01)
      # End achievement unlock

     # Repeated 12 times at present, indicating ship unlocks (Type A). Only the first 9 ships are actually unlockable
     4 bytes (32bit int)        Ship unlock (0 = locked; 1 = unlocked)


     # Begin ship high scores (repeated twice, representing "Top Scores" and "Ships Best" sets)

     4 bytes (32bit int)        Number of high scores in this set

       # Begin individual 'top score' (repeated once for each high score in this set)
       4 bytes (32bit int)    String Length (Ship name)
       n bytes (string)       Ship name
       4 bytes (32bit int)    String Length (Ship Type)
       n bytes (string)       Ship Type
       4 bytes (32bit int)    Score
       4 bytes (32bit int)    Sector (e.g. 8 = Sector 8)
       4 bytes (32bit int)    Victory (1 = true; 0 = false)
       4 bytes (32bit int)    Difficulty (1 = easy; 0 = normal)
       # End individual top score

     # End high score repeats

     # General/running scores
     4 bytes (32bit int)        Best ships defeated in a session
     4 bytes (32bit int)        Total ships defeated (all sessions)
     4 bytes (32bit int)        Best beacons explored in a session
     4 bytes (32bit int)        Total beacons explored (all sessions)
     4 bytes (32bit int)        Best scrap collected in a session
     4 bytes (32bit int)        Total scrap collected (all sessions)
     4 bytes (32bit int)        Most number of crew hired in a session
     4 bytes (32bit int)        Total number of crew hired (all sessions)
     4 bytes (32bit int)        Total games played
     4 bytes (32bit int)        Total number of victories

     # Repeated five times for Repair, Combat Kills, Pilot Evasions, Jumps Survived, Skill Masteries
     4 bytes (32bit int)        Skill Score (e.g. repairs, kills, etc.)
     4 bytes (32bit int)        String Length (Crew member name)
     n bytes (string)           Crew member name
     4 bytes (32bit int)        String Length (Crew member race)
     n bytes (string)           Crew member race (short version, e.g. "engi")
     4 bytes (32bit int)        Gender (1 = Male)

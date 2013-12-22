#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#===============================================================================
#          FILE:
#
#         USAGE:
#
#   DESCRIPTION:
#
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#       CREATED:
#      REVISION:  ---
#===============================================================================
__author__  = "Ryuutei, (ryuutei.at.work@gmail.com)"
__doc__     = ""
__version__ = "0.1"
#===============================================================================

#constants:
coffre = 64 * 6 * 9


#nombres:
hopper = 5*64
other_hoppers = (6 + 5 + 20 + 15 + 4) * hopper

desengorgeages = (64*4+55)*2 # calcule directement en units.

silos = [

    660410,
    (coffre *16*4) + (hopper *16*4) + other_hoppers + desengorgeages, # super_silo
    (coffre *32*4) + (hopper *32*4) + other_hoppers + desengorgeages, # mega_silo
    (coffre *64*4) + (hopper *64*4) + other_hoppers + desengorgeages, # hyper_silo

]


def silop(chiffre):
    "print a silo infos"
    units = chiffre
    stacks = chiffre / 64

    print()
    print("{:7} Units".format(units))
    print("{:7} Stacks".format(int(stacks)))
    print("{:7} Coffres".format(int(units/coffre)))



if __name__  == "__main__":
    print("==============================================================================")
    print("== Silos Max Capacities ======================================================")
    print("==============================================================================")
    for ii in silos:
        silop(ii)
    loot = {
        "fleches" : 31+(5*64),
        "gunpowder" : (64*6)+5,
        "bones" : (64*5) +41,
        "string" : 2,
        "flesh": (6*64)+6,

    }

    total = 0
    for ii in loot.keys():
        total += loot[ii]

    print()
    print("resume loot:")
    for ii in loot.keys():

        print("    {} = {} ({})".format(ii, loot[ii], (loot[ii]/total)*100 ) )





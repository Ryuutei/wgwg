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

def pl():
    print(".. ==============================================================================")
bullets = {
    "Musket": (1, 0.07, 0),
    # Musket balls : (bullet needed, bullet price, materiel price),
    "Meteor" :      (70, 0.07, 0),
    "Silver" :      (70, 0.07, 0),
    "Crystal" :     (50, 0.07, 0),
    "Cursed" :      (50, 0.07, 0),
    "Ichor" :       (50, 0.07, 0),
    "Chlorophyte":  (70, 0.07, 0),

    #Bmpty Bullets
    "High Velocity" :   (50, 0.03, 7),
    "Party" :           (50, 0.03, 1),
    "Nano" :            (50, 0.03, 10),
    "Exploding" :       (50, 0.03, 12),
    "Golden" :          (50, 0.03, 17),
    "Venom" :           (50, 0.03, 10),
}


prixunitaire = {
    "Musket": 0,
    # Musket balls : (bullet needed, bullet price, materiel price),
    "Meteor" :      0,
    "Silver" :      0,
    "Crystal" :     0,
    "Cursed" :      0,
    "Ichor" :       0,
    "Chlorophyte":  0,

    #Bmpty Bullets
    "High Velocity" :   0,
    "Party" :           0,
    "Nano" :            0,
    "Exploding" :       0,
    "Golden" :          0,
    "Venom" :           0,
}

OUT = [
    "Musket",
    "Meteor" ,
    "Silver" ,
    "Crystal" ,

    "High Velocity" ,
    "Party" ,
    "Nano" ,
    "Exploding" ,
    "Golden" ,

    "Cursed" ,
    "Ichor" ,

    "Venom" ,

    "Chlorophyte",

]
dommages = {
    "Musket":       7,
    "Meteor" :      9,
    "Silver" :      9,
    "Crystal" :     8,
    "Cursed" :      12,
    "Ichor" :       13,
    "Chlorophyte":  15,

    "High Velocity" :   10,
    "Party" :           10,
    "Nano" :            10,
    "Exploding" :       10,
    "Golden" :          10,
    "Venom" :           14,
}

def material(bar):
    """ retournes le prix du materiel et le nombre qu'il en faut.

    bar : nombre de cartouches cree avec 1 bar de materiel"""


    mini = 999//bar
    minbullets = mini * bar

    maxi = (999//bar) + 1
    maxbullets = maxi * bar
    extra = maxbullets - 999

    return ((mini, minbullets), (maxi, maxbullets))


def price(material, mat_price, bulletprice):
    """ returns the min and max price of bullet stacks
    material: nombre de cartouches cree avec une barre de materiel.
    bulletprice: prix des balles ou douilles vides. (en piece d'argent)

    retournes le prix d'une balle."""


    # Materiel
    mini = 999//material
    minbullets = mini * material

    mib = minbullets * bulletprice
    mim = mini * mat_price
    minprice = mib+mim

    maxi = (999//material) + 1
    maxbullets = maxi * material
    extra = maxbullets - 999

    mab = maxbullets * bulletprice
    mam = maxi * mat_price
    maxprice = mab + mam

    print("- Materiel")
    print()
    print("    Minumum：{} materiel + {} bullets".format( mini, minbullets ))
    print("    Maximum：{} materiel + {} bullets 〔extra bullets created: {}〕".format(maxi , maxbullets , extra  ))
    print()

    # Prix
    print("- Prix")
    print()
    print("    prix des balles min : {:n}".format(mib))
    print("    Prix min : {:n}".format(minprice))
    print()
    print("    prix des balles max : {:n}".format(mab))
    print("    Prix max : {:n}".format(maxprice))
    print()

    return maxprice / maxbullets





def main():
    for ii in OUT:

        pl()
        print()
        print("{} bullet".format(ii))
        print("________")
        print()

        bulletneeded, bulletprice, materialprice = bullets[ii]
        #mini, minbullets, maxi, maxbullets =
        prixunitaire[ii] = price(bulletneeded, materialprice, bulletprice)

    pl()
    print("prix Unitaire:")

    bestQP = 0
    best = None

    for ii, ij in bullets.items():
        qualiteprix = dommages[ii] / prixunitaire[ii]

        if qualiteprix > bestQP:
            bestQP = qualiteprix
            best = ii

        print("{} bullet：{} {:>30} ".format(ii, prixunitaire[ii], "〘ratio：{:0.1f}〙".format(qualiteprix)))



    print("Meilleure cartouches qualite/prix: {} 〔avec un ratio prix/dommages de {:n}〕".format(best, bestQP))




if __name__  == "__main__":
    version = __version__
    main()
    #price(50, 1, 0.03)


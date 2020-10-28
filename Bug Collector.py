# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:18:07 2019

@author: timil
"""

totalDays = 5
totalNumberOfBugs = 0

for currentDay in range( 1, totalDays + 1 ):
    bugsCollected = int( input( "How many bugs were collected on day " + \
                               str( currentDay ) + ": ") )
    totalNumberOfBugs += bugsCollected
print()
print( "The total number of bugs collected for all", totalDays, "days is", \
      totalNumberOfBugs )


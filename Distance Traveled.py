# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:31:38 2019

@author: timil
"""

vehicleSpeed = float( input( "What is the speed of the vehicle: " ) )
timeTraveled = int( input( "How many hours has it traveled?: " ) )

print()

print( "Hour","\tDistance Traveled" )
for currentHour in range( 1, timeTraveled + 1 ):
    distanceTraveled = vehicleSpeed * currentHour
    print( currentHour,"\t",distancedTraveled)

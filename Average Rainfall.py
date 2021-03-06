# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:42:50 2019

@author: timil
"""

totalNumberOfMonths = 0
totalInchesOfRainfall = 0
userNumberOfYears = int( input( "Please enter the number of years: ") )

for currentYear in range( 1, userNumberOfYears + 1 ):
    for currentMonth in range( 1, 13 ):
        monthlyRainfallInches = float( input( "Please type the inches of" + \
                    " rainfall for month " + format( currentMonth, "d" ) + \
                    ", year " + format( currentYear, "d" ) + ": ") )
        totalInchesOfRainfall += monthlyRainfallInches
        totalNumberOfMonths += 1
     
averageRainfall = totalInchesOfRainfall / totalNumberOfMonths

print()

print( "Number of months: " + format( totalNumberOfMonths, "d"), "Total" + \
      " inches of rainfall: " + format( totalInchesOfRainfall, ".2f" ), \
      " Average rainfall: " + format( averageRainfall, ".2f" ), sep="\n" )
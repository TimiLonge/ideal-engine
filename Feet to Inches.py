# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:13:11 2019

@author: timil
"""

def feetToInches(userFeet):
    inches = (userFeet / 1) * 12
    return inches

def main():
    userFeet = float( input( "Please enter the number of feet: ") )
    inches = feetToInches( userFeet )
    print(userFeet, "feet converted to inches is", format( inches, ".2f"), "inches" )
    
main()
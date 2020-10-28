# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:14:46 2019

@author: timil
"""

def max( firstNumber, secondNumber ):
    if firstNumber > secondNumber:
        return firstNumber
    else:
        return secondNumber
    
def getNumbersFromUser():
    userFirstNumber = int( input( "Please enter the first number: ") )
    userSecondNumber = int( input( "Please enter the second number: ") )
    return userFirstNumber, userSecondNumber

def main():
    userFirstNumber, userSecondNumber = getNumbersFromUser()
    print( "The maximum number between", userFirstNumber, "and", \
          userSecondNumber, "is", max( userFirstNumber, userSecondNumber) )
    
main()
def askUserForKilometers():
    userKilometers = float( input( "Please enter the distnace" + \
                                   "in kilometers: ") )
    return userKilometers

def convertKilometersToMiles( userKilometers ):
    miles = userKilometers * 0.6214
    return miles

def main():
    userKilometersTyped = askUserForKilometers()
    convertedMiles = convertKilometersToMiles( userKilometersTyped )
    
    print( userKilometersTyped, "kilometers converted to miles is", \
          format( convertedMiles, ".2f"), "miles")
    
main()
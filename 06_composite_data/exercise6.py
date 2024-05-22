#import the modules that will use
import csv
import copy

#create the dictionary to use as composite type for reading the data
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#with for loop print the key and value in terminal of the dictionary. the {} are the item in the dictionary and .format contains what is the value insert in the {} and printing
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
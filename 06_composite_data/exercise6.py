#import the modules that will use
import csv
import copy

#create the dictionary to use as composite type for reading the data
myCar = {
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
for key, value in myCar.items():
    print("{} : {}".format(key,value))

#defnie a empty list to read car inventory
myCarList = []

with open('06_composite_data/car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'column names are: {",".join(row)}')
            lineCount += 1
        else:
            print(f'vin: {row[0]} make {row[1]}, model: {row[2]},year: {row[3]}, range: {row[4]}, topSpeed {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentCar = copy.deepcopy(myCar)
            currentCar["vin"] = row[0]
            currentCar["make"] = row[1]
            currentCar["model"] = row[2]
            currentCar["year"] = row[3]
            currentCar["range"] = row[4]
            currentCar["topSpeed"] = row[5]
            currentCar["zeroSixty"] = row[6]
            currentCar["mileage"] = row[7]
            myCarList.append(currentCar)
            lineCount += 1
    print(f'Processed {lineCount} lines.')

    currentCar = copy.deepcopy(myCar)

    for myCarProperties in myCarList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-------")

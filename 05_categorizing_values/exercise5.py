#Create a list with different types of data
myMixedTypeList = [45, 290578, 1.02, True, "my dog is on the bed.", "45"]

#usinf for loop statement to print data type for each item
for item in myMixedTypeList:
    print("{} is of data type {}".format(item,type(item)))
#1. Create a variable with string value and print in console
myString = "This is a string."
print(myString)

#Print witch type of string there is
print(type(myString))

#Convert the value of type into string with srt()
print(myString + " is of the data type " + str(type(myString)))

#2. Create two string to concatenated with + in a third string and print in console.
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#3. Create a variable with function input and then print in console
name = input("What is your name? ")
print(name)

#4. Create two variable with inputs 
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

#Create a string with print() and two variables
print("{}, you like a {} {}!".format(name,color,animal))
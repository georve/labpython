

myValue="This is a String"
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
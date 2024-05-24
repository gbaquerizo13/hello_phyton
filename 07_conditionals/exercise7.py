# use if and else conditions
userReply  = input("Do you need to ship a package? (enter yes or not) ")
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

# elif statement
userReplies = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

if userReplies == "stamps":
    print("we have many stamp designs to choose from.")
elif userReplies == "envelope":
    print("we have many envelope sizes to choose from.")
elif userReplies == "copy":
    copies = input("how many copies would you like? (enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("thank you, please come again.")
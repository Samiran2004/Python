import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Creating instance")
elif type == "t2.medium":
    print("Creating instance but take sometime..")
    print("This will charge you $4 per day")
else:
    print("Your input is t2.micro or t2.medium")

# Ask user for name

name = input("What is your Name?: ")

# Ask user for Age

age = input("What is your Age?; ")

# Ask user for City

city = input("What City do you live in?: ")

# Ask user what the Like

like = input("What do you like to do?: ")

#Create Ouput text

string = "Your name is {} and you are {} years old. You live in {} and you like {}"
output = string.format(name,age,city,like)

# Print out to screen

print(output)


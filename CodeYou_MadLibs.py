# Take in a name from the user and store it in the variable name using the title method to coerce it to title case

name =  input('Please enter your name: ').title()

# Print a string inserting the user's name using the variable created above

print("Hello, " + name + ". I hear you are interested in learning Python! Great choice!")

# Take input from the user to find out more about their interest in Python and store in the variable ambition

ambition = input("I'm curious what sparked your interest? What do you aspire to achieve?")

# Print a string inserting the user's ambition from the above variable

print("So your ambition is " + ambition + ". I think Python will be very helpful for that.")

# Take input from the user on one of their hobbies and store it in the variable hobby using the lower method to coerce it to all lowercase

hobby = input("So what are your interests outside of programming?").lower()

# Print a string inserting the user's hobby from the above variable

print("So you're also interested in " + hobby + "? That is a great way to spend some free time!")

# Capture a y/n 'boolean' from the user and storing it in the variable bool

bool = input("Do you think that learning Python could supplement your " + hobby + " experience? (y/n)")

# Validate the user input coercing y to yes or n to no and storing that string in the bool variable. If the user input does not match one of the options
# then a new input announces the error and asks the user to try again. A true boolean stored in the variable valid is created that is coerced to True
# from False if the user input is valid, otherwise remaining false and causing the while loop to continue

valid = False

while valid == False:
    if bool.lower() == 'y':
        bool = 'yes'
        valid = True
    elif bool.upper() == 'N':
        bool = 'no'
        valid = True
    else:
        bool = input("I'm sorry but that is invalid input. Please enter either 'y' or 'n'")

# Provide the user some feedback based upon what they have stored in the bool variable including their hobby variable in the output using if/else logic
# to customize the response 

if bool == 'yes':
    print("I agree that Python can likely enhance your " + hobby + " experience. I look forward to helping you reach that point.")
elif bool == 'no':
    print("Perhaps you will find something while learning Python to better your enjoyment of " + hobby)

# Create a final string using all the individual output from the previous statements. Introduces += for appending to a string. Uses some if/else logic 
# to customize from teh boolean variable.

final = name + " is a Code You student that is on a good path to picking up a new programming langauge. " + name
final += " would like to learn Python for " + ambition + ". In their free time " + name + " likes to do " + hobby + " for fun. "

if bool == 'yes':
    final += name + " believes Python can enhance their experience with " + hobby + "."
else:        
    final = final + name + " does not believe Python can enhance their experience with " + hobby + ". Maybe we can find a way to make that happen."

print(final)


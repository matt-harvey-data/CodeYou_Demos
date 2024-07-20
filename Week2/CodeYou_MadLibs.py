# Initialize an empty list stored in the variable 'responses' to store input taken from the user

responses = []

# Take in a name from the user and store it in the list using the title method to coerce it to title case

responses.append(input('Please enter your name: ').title())

# Print a string inserting the user's name using the list at index 0 created above

print("Hello, " + responses[0] + ". I hear you are interested in learning Python! Great choice!")

# Take input from the user to find out more about their interest in Python and store in index 1 of our responses list

responses.append(input("I'm curious what sparked your interest? What do you aspire to achieve? "))

# Print a string inserting the user's ambition from index 1 of our responses list

print("So your ambition is " + responses[1] + ". I think Python will be very helpful for that.")

# Take input from the user on one of their hobbies and store it in index 2 of the responses list using the lower method to coerce it to all lowercase

responses.append(input("So what are your interests outside of programming? ").lower())

# Print a string inserting the user's hobby from index 2 of our list

print("So you're also interested in " + responses[2] + "? That is a great way to spend some free time!")

# Capture a y/n 'boolean' from the user and storing it in index 3 of our list

responses.append(input("Do you think that learning Python could supplement your " + responses[2] + " experience? (y/n) "))

# Validate the user input coercing y to yes or n to no and storing that string in index 3 of the list. If the user input does not match one of the options
# then a new input announces the error and asks the user to try again. A true boolean stored in index 3 of the list is created that is coerced to True
# from False if the user input is valid, otherwise remaining false and causing the while loop to continue

valid = False

while valid == False:
    if responses[3].lower() == 'y':
        responses[3] = True
        valid = True
    elif responses[3].upper() == 'N':
        responses[3] = False
        valid = True
    else:
        responses[3] = input("I'm sorry but that is invalid input. Please enter either 'y' or 'n' ")

# Provide the user some feedback based upon what they have stored at index 3 including their index 2 in the output using if/else logic
# to customize the response 

if responses[3] == True:
    print("I agree that Python can likely enhance your " + responses[2] + " experience. I look forward to helping you reach that point.")
elif responses[3] == False:
    print("Perhaps you will find something while learning Python to better your enjoyment of " + responses[2] + ".")

# Create a final string using all the individual output from the previous statements. Introduces += for appending to a string. Uses some if/else logic 
# to customize from index 3.

final = responses[0] + " is a Code You student that is on a good path to picking up a new programming langauge. " + responses[0]
final += " would like to learn Python for " + responses[1] + ". In their free time " + responses[0] + " likes " + responses[2] + ". "

if responses[3] == 'yes':
    final += responses[0] + " believes Python can enhance their experience with " + responses[2] + "."
else:        
    final = final + responses[0] + " does not believe Python can enhance their experience with " + responses[2] + ". Maybe we can find a way to make that happen."

print(final)


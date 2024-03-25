# Initiates Empty Python dictionary in the variable weekly_tasks

weekly_tasks = {}

# Initiates a list with the weekdays as strings in the variable weekdays

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Initiates a list with the days of the weekend as string in the variable weekends

weekend_days = ['Saturday', 'Sunday']

# Greets the user and announces the purpose of the program

print("Hello, I'm here to help you track your weekly tasks! We'll create a worklist day by day to help you stay on track with your weekly goals! ")

# Creates two lists to store our weekday and weekend goals, note we are creating these outside of our for loop, if blank lists were created inside the
# loop then we would be renewed as blank every time through. Two variables as blank strings are also created to control the loops flow. A while loop 
# is then created that prompts the user for input, initially tasks that are to be completed every day. If logic checks if the task is 'done.' If this is
# not the case the item is added to the weekday_goals list. Once we reach a 'done' input from the user for weekdays we initiate a second while loop to 
# take user input about repeating weekend tasks. When the weekend input is 'done' then a break statement ends the loop and we move on in the program.

weekday_goals = []
weekend_goals = []
weekday_task = ''
weekend_task = ''

while weekday_task != "done":
    weekday_task = (input("To start let's make a list of tasks that we aim to accomplish every weekday. We will add these one at a time. To add a task to be accomplished every weekday type it here, otherwise type 'done' "))
    if weekday_task != "done":
        weekday_goals.append(weekday_task)
    if weekday_task == 'done':
        while weekend_task != 'done':
            weekend_task = (input("Now let's make a list of tasks that we aim to accomplish every weekend day. Similarly, to add a task to be accomplished every weekday type it here, otherwise type 'done' "))
            if weekend_task != "done":
                weekend_goals.append(weekend_task)
            if weekend_task == 'done':
                break

# Initially a for loop is created to iterate through the items of the list 'weekdays' namely the name of the weekdays. This list then updates our blank
# dictionary from the first cell with each day of the week as the key and the list created in the above cell as the value. Similarly we iterate through]
# the days of the weekend adding those days and their list as dictionary items as well.

for i in weekdays:
    weekday_tasks = list.copy(weekday_goals)
    weekly_tasks.update({i:weekday_tasks})
for i in weekend_days:
    weekend_day_tasks = list.copy(weekend_goals)
    weekly_tasks.update({i: weekend_day_tasks})

# Now we announce to the user that we are going to add tasks specific to certain days. We iterate through the days which we now have stored as the keys
# in our weely_tasks dictionary. A variable 'unique_task' is initiated as an empty string, and then we check if it stores the value 'done.' If that is 
# not the case we ask the user if there are any tasks to add for the day corresponding to this time through the loop. If the user entered a task then it
# is appended to the list stored as the value for the corresponding day as the key. When the user types 'done' we move on to the next iteration
# representing the next day until we've iterated through all seven days.

print("Now we'll add tasks that are specific to certain days. ")

for i in weekly_tasks.keys():
    unique_task = ''
    while unique_task != 'done':
        unique_task = input("Are there any tasks to add to " + i + "? If not type 'done' ")
        if unique_task != 'done':
            weekly_tasks[i].append(unique_task)

# We now announce to the user that we have established a schedule for the week and print it to the console.

print("Great! Now we have a schedule for the week! Here is your week's schedule: ")

for i,j in weekly_tasks.items():
    print(i,j)

# Implement new empty dictionary to store completed tasks. Populate dictionary with days of the week as the keys from the list of tasks, and an empty 
# list for the values

achieved_tasks = {}

for i in weekly_tasks.keys():
    achieved_tasks.setdefault(i, [])

# Print to the console to announce to the user that we will be able to cross items off of our list. Implement the variable finished and store the value
# false in it. This is done to control the loop. Begin with a while loop that will terminate if finished != False. Take an input from the user to
# determine what day we'd like to move a task for. The next if statement validates that the day is in the keys of the weekly_tasks dictionary. If so
# we accept a task from the user as an input. If not we check if the user input = 'done.' If so we change finished to True to terminate the initial while
# loop. If neither is true we announce the invalid input and that we will try again. Presuming day is valid and we have accepted a task from the user we
# validate that task is in the values corresponding to the previously indicated day. If so pop the value from the weekly_tasks list and store the value
# in a variable 'achieved_value.' We then use that variable to append the item to the list corresponding to that day in achieved_value. We then announce to
# the user that it worked and we'll return to the beginning. If the user input for their task is not in the value corresponding to their day in 
# weekly_tasks we announce the input as invalid and let the user know we'll start again from the beginning.

print("Time to cross some items off of our list! ")

finished = False

while finished == False:
    day = input("Please type the day you have completed an item for! or 'done' if complete ")
    if day in weekly_tasks.keys():
        achieved = input("Please type the task that you have completed! ")
        if achieved in weekly_tasks[day]:
            achieved_value = weekly_tasks[day].pop(weekly_tasks[day].index(achieved))
            achieved_tasks[day].append(achieved_value)
            print("Perfect. Let's go back to the top! ")
        else:
            print("That's not a valid task, let's start from the beginning. ")
    elif day == 'done':
        finished = True
    else:
        print("I'm sorry but that's not a valid day. Try again! ")

# We now print to the console a message to let the user know that we'll be reading out the achieved tasks from the achieved_tasks dictionary.

print("Here's what you've achieved so far.")

for i,j in achieved_tasks.items():
    print(i,j)

# We now print to the console a message to let the user know that we'll be reading out the remaining tasks from the weekly_tasks dictionary.

print("Here's what we have left to do.")

for i,j in weekly_tasks.items():
    print(i,j)




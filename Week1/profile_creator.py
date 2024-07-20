ask_name = "What is your name? "

name = input(ask_name)

print(name)

ask_purpose = "Why did you decide to join Code Louisville? "

purpose = input(ask_purpose)

print(purpose)

ask_hobbies = "What are you interested in outside of programming? "

hobbies = input(ask_hobbies)

print(hobbies)

ask_goals = "What do you aspire to achieve with your new programming skills? "

goals = input(ask_goals)

print(goals)

ask_motivator = "What prompted you to set this goal? "

motivator = input(ask_motivator)

print(motivator)

f = open("profile.txt", "r+")

f.write(ask_name + "\n\n" + name + "\n\n" + ask_purpose + "\n\n" + purpose + "\n\n" + ask_hobbies + "\n\n" + hobbies + "\n\n" +
       ask_goals + "\n\n" + goals + "\n\n" + ask_motivator + "\n\n" + motivator)

f.close()


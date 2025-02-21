import time
print("Hello and welcome to the playtime leaderboard. Command is leaderboard!")
attempts = 0
command = input("Enter command: ")
while command != "leaderboard":
    attempts += 1
    if attempts == 3:
        print("Command wrong try again in 30 seconds")
        time.sleep(30)
        attempts = 0
    else:
        print("Wrong command try again")
    command = input("Enter command: ")
print("Jake 90 hrs; Michael 200 hrs; David 60 hrs; Chris 140 hrs; Ryan 220 hrs; Alex 75 hrs; Kevin 180 hrs; Brandon 120 hrs; Nick 50 hrs; Tyler 200 hrs; Daniel 95 hrs; Andrew 80 hrs; Justin 110 hrs; Ethan 70 hrs; Matt 160 hrs; Sean 40 hrs; Kyle 140 hrs; Eric 150 hrs; Zach 110 hrs; Jason 180 hrs")

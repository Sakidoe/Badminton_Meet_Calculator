#import string
#PARA
def addEvent(Meet): 
    for i in Meet:
        Meet[i]["MD"] = dict()
        Meet[i]["MS"] = dict()
        Meet[i]["XD"] = dict()
        Meet[i]["WS"] = dict()
        Meet[i]["WD"] = dict()
def addPlayer(Meet):
    print("ADDING PLAYER")
    name = input("What is the player's first and last name?")
    event_number_text = "how many events is "+ name + " playing?"
    event_number = input(event_number_text)
    for i in range(1, int(event_number)+1):
        event_text = "for the "+ str(i) + "th event, what is "+ name + " playing?"
        event = input(event_text)
        rank_text = "what rank is " + name + " playing for " +event+"?"
        rank = input(rank_text)
        if event.upper() == "MD":
            if Meet["MD"] ==
            print(Meet["MD"])

        elif event.upper() == "MS":
            pass
        elif event.upper() == "MD":
            pass
        elif event.upper() == "MD":
            pass
        elif event.upper() == "MD":
            pass
        else:
            pass
def deleteEvent():
    pass
def search():
    pass
def run():# may not need
    pass
def menu():
    print("----------------------Menu----------------------\n" + "[Add Player -> [A]] || [Remove Player -> [R]] || [View Roster -> [V]] || [Make Meet -> [M]]")
    return input()
def save():
    pass
#---
teams = []
teamNumber = input("//PROGRAM START\\\ \nHow many teams are there in this meet?")

#---
Meet = dict()
for i in range(1, int(teamNumber) + 1):
    print("--------------------------")
    temp = input("What is the team name of team " +  str(i) + "?")
    Meet[temp] = dict()
    teams.append(temp)
#---- add the events within the team
addEvent(Meet)
#----
if int(teamNumber) == 2:
    print("--------------------------")
    print("Welcome to the meet between", list(Meet.keys())[0],"and", list(Meet.keys())[1] + "!")
else:
    print("--------------------------")
    print("Welcome to the Trimeet between", list(Meet.keys())[0]+",", list(Meet.keys())[1],"and", list(Meet.keys())[2] + "!")
#----gonna have to loop the process below----
menu_query = menu()
if menu_query.upper() == "A":
    temp = input("Selection : Add Player : Which team is this player on?")
    if temp == list(Meet.keys())[0]:
        addPlayer(Meet[teams[0]])
    elif temp == list(Meet.keys())[1]:
        addPlayer(Meet[teams[1]])
    elif len(teams) > 2:
        if temp == list(Meet.keys())[2]:
            addPlayer(Meet[teams[2]])
    else:
        print("Not a team!")



#while True:
    
print(Meet)

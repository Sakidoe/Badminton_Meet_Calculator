import json
import openpyxl
from datetime import datetime, timedelta
from pandas import DataFrame
import random

# -> addEvent(Meet) :: add md, ms, xd, ws, and wd events to the algorithm.
def addEvent(Meet): 
    for i in Meet:
        Meet[i]["MD"] = dict()
        Meet[i]["MS"] = dict()
        Meet[i]["XD"] = dict()
        Meet[i]["WS"] = dict()
        Meet[i]["WD"] = dict()

# -> addPlayer() :: by inputting the player's name, event number, event title, and ranks of those events, input them into the json file.
def addPlayer(Meet, team_name, players):
    file_name = input("What is the file name called?")
    excel_sheet = openpyxl.load_workbook(file_name)

    sh = excel_sheet.active
    temp = []
    for i in range(1, sh.max_row+1): 
        for j in range(1, 4): 
            cell_obj = sh.cell(row=i, column=j)
            if cell_obj.value == None:
                pass
            else:
                temp.append(cell_obj.value)
    i = 0
    while True:
        if i >= len(temp):
            break
        if temp[i] == "MD" or temp[i] == "MS" or temp[i] == "XD" or temp[i] == "WS" or temp[i] == "WD":
            curr_event = temp[i]
        elif temp[i] != str(temp[i]):
            json_rank_text = "Rank " + str(int(temp[i]))
        else:
            name = temp[i]
            if json_rank_text not in Meet[curr_event].keys(): # if empty
                 Meet[curr_event][json_rank_text] = {"Player Name" : [name]}
            else:
                 Meet[curr_event][json_rank_text]["Player Name"].append(name)
        i+=1

def menu():
    print("----------------------Menu----------------------\n" + " [Add Roster -> [A]] \n [View Roster -> [V]] \n [Save Changes -> [S]] \n [Make Meet -> [M]] \n [Terminate -> [X]]")
    return input("\n<Your Choice>")
#may not need:
def saveSchedule(Meet):
    json_format = json.dumps(Meet, indent=3)

    file_to_delete = open("schedule.txt",'w')
    file_to_delete.close()

    with open('schedule.txt', 'w') as convert_file: 
        convert_file.write(json_format)
    print("saved!")

def save(Meet):
    json_format = json.dumps(Meet, indent=3)

    file_to_delete = open("save.txt",'w')
    file_to_delete.close()

    with open('save.txt', 'w') as convert_file: 
        convert_file.write(json_format)
    print("saved!")
#---
teams = [] # a list of teams.
teamNumber = input("//PROGRAM START\\\ \nHow many teams are there in this meet?")
players = dict() # a dictionary of players relevant to each team.
#---
Meet = dict()
for i in range(1, int(teamNumber) + 1):
    print("--------------------------")
    temp = input("What is the team name of team " +  str(i) + "?")
    temp = temp.upper()
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
while True:
    menu_query = menu()
    #try:
    if menu_query.upper() == "A":
        temp = input("Selection : Add Player : Which team is this player on?")
        if temp.upper() == list(Meet.keys())[0]:
            addPlayer(Meet[teams[0]], teams[0], players)
        elif temp.upper() == list(Meet.keys())[1]:
            addPlayer(Meet[teams[1]], teams[1], players)
        elif len(teams) > 2:
            if temp.upper() == list(Meet.keys())[2]:
                addPlayer(Meet[teams[2]], teams[2], players)
        else:
            print("Not a team!")
    if menu_query.upper() == "S":
        save(Meet)
    if menu_query.upper() == "V":
        print("this function has not been implemented yet")
        break
    if menu_query.upper() == "M":
        pass
        #makeMeet(Meet)
    if menu_query.upper() == "X":
         break



#while True:
    
print(Meet)
import json
import openpyxl
from datetime import datetime, timedelta
from pandas import DataFrame
import random
import sys
import tty
import termios


BOLD = '\033[1m'
END = '\033[0m'

def get_key():
    """Get a single keypress from the user."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        # Handle arrow keys (they send 3 characters)
        if ch == '\x1b':
            ch = sys.stdin.read(2)
            if ch == '[A':
                return 'UP'
            elif ch == '[B':
                return 'DOWN'
        elif ch == '\r' or ch == '\n':
            return 'ENTER'
        elif ch == '\x03':  # Ctrl+C
            return 'QUIT'
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# -> addEvent(Meet), add md, ms, xd, ws, and wd events to the algorithm.
def addEvent(Meet): 
    for i in Meet:
        Meet[i]["MD"] = dict()
        Meet[i]["MS"] = dict()
        Meet[i]["XD"] = dict()
        Meet[i]["WS"] = dict()
        Meet[i]["WD"] = dict()

# -> addPlayer(), by inputting the player's name, event number, event title, and ranks of those events, input them into the json file.
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
    options = [
        ("Add Roster", "A"),
        ("View Roster", "V"),
        ("Save Changes", "S"),
        ("Make Meet", "M"),
        ("Terminate", "X")
    ]
    
    selected = 0
    num_options = len(options)
    
    # Print static header once
    print("\n" + "="*50)
    print(f"{BOLD}{'BADMINTON MEET MAKER - MAIN MENU':^50}{END}")
    print("="*50)
    print(f"\n  Use ↑/↓ arrows to navigate, Enter to select\n")
    print("  " + "-"*46)
    
    # Save cursor position (after the separator line)
    print("\033[s", end='')  # Save cursor position
    
    def draw_menu():
        """Redraw the menu options."""
        print("\033[u", end='')  # Restore cursor position
        for i, (option, command) in enumerate(options):
            if i == selected:
                print(f"\r  {BOLD}→ {option:<28}{END} {BOLD}[{command}]{END}\033[K")  # \033[K clears to end of line
            else:
                print(f"\r    {option:<28} [{command}]\033[K")
        print(f"  {'-'*46}\033[K")
        sys.stdout.flush()
    
    # Draw initial menu
    draw_menu()
    
    while True:
        key = get_key()
        
        if key == 'UP':
            selected = (selected - 1) % num_options
            draw_menu()
            
        elif key == 'DOWN':
            selected = (selected + 1) % num_options
            draw_menu()
            
        elif key == 'ENTER':
            print()  # New line before returning
            return options[selected][1]  # Return the command letter
            
        elif key == 'QUIT':
            print()
            return 'X'

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
# ----------------------------------
# **********************************
# *********START OF PROGRAM*********
# **********************************
# ----------------------------------

teams = [] # Array of Teams
players = dict() # a dictionary of players relevant to each team.
Meet = dict()
#/----------
#Initial Print Statement
print("\n\n_______________________________________________________________\n\n" +
      f"{BOLD}Welcome to the Badminton Meet Maker, by Richard Huang and BUCD!{END}\n" +
          "_______________________________________________________________\n")
print("This program is designed to help create a 1v1 school badminton meet, \n" \
"generating a conflict-free .xslx file for users. Just answer the prompts, \n" \
"then follow the instructions.")
#\----------
for i in range(1,3):
    print("_______________________________________________________________")
    temp = input(f"{BOLD}What is the team name of team {i}?{END}>> ")
    temp = temp.upper()
    Meet[temp] = dict()
    teams.append(temp)
#---- add the events within the team
addEvent(Meet)
#----
print("--------------------------")
print("Welcome to the meet between", list(Meet.keys())[0],"and", list(Meet.keys())[1] + "!")

#----gonna have to loop the process below----
while True:
    menu_query = menu()
    #try:
    if menu_query.upper() == "A":
        temp = input("Selection == ")
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
    
print(Meet)
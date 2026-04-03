import json
import openpyxl
from datetime import datetime, timedelta
from pandas import DataFrame
import random
Meet = {
   "10:30": {
      "1": [
         "WD3",
         [
            "Aditi Kavipurapu",
            "Muyen Liang"
         ],
         [
            "Daphne Huang",
            "Rhea Zou"
         ]
      ],
      "2": [
         "XD2",
         [
            "Richard huang",
            "Kristine Ngo"
         ],
         [
            "Ashton Lee",
            "Amanda Ng"
         ]
      ],
      "3": [
         "XD1",
         [
            "Leyang Ding",
            "Xin Huang"
         ],
         [
            "Adam Tay",
            "Tara Chou"
         ]
      ],
      "4": [
         "XD3",
         [
            "Robert Chang ",
            "Erika Lai"
         ],
         [
            "Vivan Sinha",
            "Kristin Song"
         ]
      ],
      "5": [
         "MD5",
         [
            "Justin Larson",
            "Samarth Sridhara"
         ],
         [
            "Howard Huang",
            "Ray Sun"
         ]
      ],
      "6": [
         "XD8",
         [
            "Adrian Luo",
            "Julie Ma"
         ],
         [
            "Rehadyan Utomo",
            "Nadia Kho"
         ]
      ]
   },
   "11:15": {
      "1": [
         "WS1",
         [
            "Erika Lai"
         ],
         [
            "Tara Chou"
         ]
      ],
      "2": [
         "MD1",
         [
            "Richard Huang",
            "Jun Jie Lai"
         ],
         [
            "Adam Tay",
            "Kevin Lan"
         ]
      ],
      "3": [
         "XD7",
         [
            "Adrian Luo",
            "Julie Ma"
         ],
         [
            "Kyle Huang",
            "Yvonne Wang"
         ]
      ],
      "4": [
         "MS7",
         [
            "Jon Moser"
         ],
         [
            "Thet Paing (David) Da Na"
         ]
      ],
      "5": [
         "WD6",
         [
            "Aditi Kavipurapu",
            "Muyen Liang"
         ],
         [
            "Anni Zhang",
            "Elaine Jiang"
         ]
      ],
      "6": [
         "WS4",
         [
            "Elaine Tsou"
         ],
         [
            "Anjuli Oey"
         ]
      ]
   },
   "12:00": {
      "1": [
         "MS2",
         [
            "Leyang Ding"
         ],
         [
            "Brad Chiu"
         ]
      ],
      "2": [
         "MD3",
         [
            "Jon Moser",
            "Kyle Fang"
         ],
         [
            "Patrick Chi",
            "Ryan Zhu"
         ]
      ],
      "3": [
         "XD6",
         [
            "Andy Li",
            "Muyen"
         ],
         [
            "Warren Chang",
            "Ashley Zheng"
         ]
      ],
      "4": [
         "XD4",
         [
            "Claudia Xu",
            "Andrew Yeow "
         ],
         [
            "Kevin Lan",
            "Eileen Pan"
         ]
      ],
      "5": [
         "MD9",
         [
            "Junru Su",
            "Aaron Lim"
         ],
         [
            "Leo Chen",
            "Jackie Dai "
         ]
      ],
      "6": [
         "MS4",
         [
            "Neil Patel"
         ],
         [
            "Ray Sun"
         ]
      ]
   },
   "12:45": {
      "1": [
         "WD1",
         [
            "Joy Yang",
            "Xin Huang"
         ],
         [
            "Amanda Ng",
            "Tara Chou"
         ]
      ],
      "2": [
         "MS3",
         [
            "Robert Chang"
         ],
         [
            "Ryan Zhu"
         ]
      ],
      "3": [
         "MS1",
         [
            "Jun Jie Lai"
         ],
         [
            "Patrick Chi"
         ]
      ],
      "4": [
         "MD11",
         [
            "Junru Su",
            "Aaron Lim"
         ],
         [
            "Rehadyan Utomo",
            "Warren Chang"
         ]
      ],
      "5": [
         "WD5",
         [
            "Claudia Xu",
            "Erika Lai"
         ],
         [
            "Sarah Gao",
            "Fiona Chen"
         ]
      ],
      "6": [
         "MD4",
         [
            "Vo Ly",
            "Brandon Leung"
         ],
         [
            "Cameron Kato",
            "Harsh Srivastav"
         ]
      ]
   },
   "01:30": {
      "1": [
         "WS2",
         [
            "Joy Yang"
         ],
         [
            "Ashley Huang"
         ]
      ],
      "2": [
         "WS3",
         [
            "Kristine Ngo"
         ],
         [
            "Rosamund Li"
         ]
      ],
      "3": [
         "MS6",
         [
            "Kyle Fang"
         ],
         [
            "Brandon Wu"
         ]
      ],
      "4": [
         "MD10",
         [
            "Neil Patel",
            "Andrew Yeow"
         ],
         [
            "Arav Sachdeva",
            "Aarav Singh"
         ]
      ],
      "5": [
         "MD6",
         [
            "Jonathan Li",
            "Sean Tan"
         ],
         [
            "Edwin Tang",
            "Jonathon Cheng"
         ]
      ],
      "6": [
         "MD2",
         [
            "Leyang Ding",
            "Robert Chang"
         ],
         [
            "Ashton Lee",
            "Vivan Sinha"
         ]
      ]
   },
   "02:15": {
      "1": [
         "MS5",
         [
            "Andrew Yeow"
         ],
         [
            "Jackie Dai "
         ]
      ],
      "2": [
         "WD2",
         [
            "Claudia Xu",
            "Erika Lai"
         ],
         [
            "Ashley Huang",
            "Kristin Song"
         ]
      ],
      "3": [
         "WD4",
         [
            "Julie La",
            "Khanh Tran"
         ],
         [
            "Eileen Pan",
            "Alicia Wang"
         ]
      ],
      "4": [
         "MD8",
         [
            "Andy Li",
            "Jason Wu"
         ],
         [
            "Anton Luu",
            "Justin Wang "
         ]
      ],
      "5": [
         "XD5",
         [
            "Aditi Kavipurapu",
            "Ken Sibal"
         ],
         [
            "Randy Huang",
            "Rhea Zou"
         ]
      ],
      "6": [
         "MD7",
         [
            "Bill Wong",
            "Donald Ly"
         ],
         [
            "Evan Wang",
            "Brandon Wu"
         ]
      ]
   },
   "03:00": {}
}
def conflictSwap(final_schedule, conflicts):
   print(conflicts)
def selectMatch(match_number, Meet, players, timeslot, prio_flag, priority_courts, the_court_number, priority_dict, conflicts_dict):
   prev_player = ""
   flag = False
   conflict = False

   while True: #to make sure same matches are no longer called
      if match_number == {}:
         return True
      
      if prio_flag == True and the_court_number <= int(priority_courts):
         prio_list = []
         for i in Meet:
            if Meet[i] == False:
               prio_list.append(i)
         if len(prio_list) == 0:
            match = random.choice(list(match_number.keys()))
         else:
            match = random.choice(prio_list)
      else:
         match = random.choice(list(match_number.keys()))

      if prio_flag == True:
         if match_number[match][1] == True and match_number[match][2] == True and match_number[match][3] == True:
            priority_dict[match] = True
      
      if False not in match_number[match].values():
         del match_number[match]
         continue

      if prio_flag == True and the_court_number <= int(priority_courts):
         if priority_dict[match] == False:
            rank_choice = random.choice([1, 2, 3])
         elif len(prio_list) != 0:
            temp_list = []
            for i in range(4, len(match_number[match].keys())+1):
               temp_list.append(i)
            rank_choice = random.choice(temp_list)
         else:
            rank_choice = random.choice(list(match_number[match].keys()))
      else:
         rank_choice = random.choice(list(match_number[match].keys()))

      if match_number[match][rank_choice] == True:
         continue
      else:
         #conflict check
         for i in Meet:
            rank_number = "Rank " + str(rank_choice)

            try:
               for j in range(0, len(Meet[i][match][rank_number]["Player Name"])):
                  temp_player = Meet[i][match][rank_number]["Player Name"][j]
                  if temp_player in players:
                     conflict = True
                     break
            except:
               temp_num = rank_choice

               while temp_num > len(Meet[i][match].values()):   
                  temp_num = abs(len(Meet[i][match].values()) - temp_num)

               rank_number = "Rank " + str(temp_num)
               for j in range(0, len(Meet[i][match][rank_number]["Player Name"])):
                  temp_player = Meet[i][match][rank_number]["Player Name"][j]

                  if temp_player in players:
                     conflict = True
                     break

         if conflict == True and prev_player != temp_player:
            prev_player = temp_player
            conflict = False
            continue
         else:
            if prev_player == temp_player:
               print("there will be an unavoidable conflict in time", timeslot, prev_player)
               if timeslot not in conflicts_dict:
                  conflicts_dict[timeslot] = [prev_player]
               else:
                  conflicts_dict[timeslot].append(prev_player)
            match_number[match][rank_choice] = True
            break
   return [match,rank_choice]
         
   
def save(Meet):
    json_format = json.dumps(Meet, indent=3)

    file_to_delete = open("schedule.txt",'w')
    file_to_delete.close()

    with open('schedule.txt', 'w') as convert_file: 
        convert_file.write(json_format)
    print("saved!")
def makeMeet(Meet):# for a MEET, not trimeet
   #first make structure: how long each game will take, how many courts, how much time
   #priority courts named courts 1, 2 and 3. <- these hold the best courts.
   print("//MAKE PROGRAM START\\\ ")
   prio_flag = False
   #-- a series of inputs to begin the program

   tpm = input("what is the time given for each game cycle? write in terms of minutes(30 = 30 minutes)") #tpm = time per match
   meet_time_start = input("when does the meet start? Write in the 24:00 clock format(16:00 = 4pm)")
   meet_time_end = input("When does the meet end? Write in the 24:00 clock format(16:00 = 4pm)")
   courts_number = input("How many courts are used in this meet?")
   priority_query = input("Do you want to have priority courts?\nPriority courts are for the top seeds[1 - 3] to play on certain courts.\n[Y/N]")
   if priority_query.upper() == "Y":
      priority_courts = input("How many priority courts would you like?")
      if priority_courts >= courts_number:

         print("You cannot have equal or more priority courts than normal courts")
         return
      print("//PRIORITY COURTS = COURTS 1 -", priority_courts)
      prio_flag = True
   else:
      print("Running program without priority courts.")
   #-- using the datetime package to be ale to transfer str to time, and do math with time.

   time_begin = datetime.strptime(meet_time_start, "%H:%M")#check times
   time_end = datetime.strptime(meet_time_end, "%H:%M")
   difference = time_end - time_begin
   plausible_minutes = difference.total_seconds() / 60 #calculates minutes alloted to the meet
   plausible_total_matches = (plausible_minutes / int(tpm)) * int(courts_number) #minutes over time per match to get amount of matches for 1 court, * court no.
   match_number = { #will be changed later
      "MD" : 0,
      "MS" : 0,
      "XD" : 0,
      "WD" : 0,
      "WS" : 0
   }
   for i in Meet: #searches and finds the number of matches that will occur, from the highest number of spots from each event of each time.
      for j in Meet[i]:
         if len(Meet[i][j].values()) > match_number[j]:
               match_number[j] = len(Meet[i][j].values()) #places the values into match_number for calculation later.
   total_matches = sum(match_number.values()) # number of matches that have to be played

   #-- a check with time. If plausible with the time given and matches that have to be played, will allow, if not, display why not and break.
   
   print("PLAUSible matches", plausible_total_matches, "||TOTAL matches" , total_matches)
   if(plausible_total_matches < total_matches): #if amount of matches > matches can be played, impossible to create schedule
      print("NO TIME FOR THE MEET\nPlausible matches based on tpm and meet time:",plausible_total_matches, "\nTotal matches required for meet:", total_matches)
      return
   
   #--begin final part
   final_schedule = dict()#final schedule to be given out.
   priority_dict = { "MD" : False,
                     "MS" : False,
                     "XD" : False,
                     "WD" : False,
                     "WS" : False
                   }
   conflicts = dict()
   time_change = timedelta(minutes = int(tpm))
   new_time = time_begin
   while new_time < time_end:
       final_schedule[new_time.strftime('%I:%M')] = dict()
       new_time = new_time + time_change

   for c in match_number: #repurpose match_number
      temp = int(match_number[c])
      match_number[c] = dict()
      for d in range(1, temp + 1):
            match_number[c][d] = False

   for timeslot in final_schedule.keys():
      courts = dict()
      players = []
      for i in range(1, int(courts_number)+1):
         if match_number == {}:
            break
         SM_Results = selectMatch(match_number, Meet, players, timeslot, prio_flag, priority_courts, i, priority_dict, conflicts)
         if SM_Results == True:
            break
         match = SM_Results[0]
         rank_choice = SM_Results[1]
                                                                                                                                                
         courts[i] = []
         event_temp = match + str(rank_choice)
         courts[i].append(event_temp)

         for a in Meet:
            rank_number = "Rank " + str(rank_choice)
            try:
               courts[i].append(Meet[a][match][rank_number]["Player Name"])
            except:
               temp_num = rank_choice
               while temp_num > len(Meet[a][match].values()):   
                  temp_num = abs(len(Meet[a][match].values()) - temp_num)
               rank_number = "Rank " + str(temp_num)
               courts[i].append(Meet[a][match][rank_number]["Player Name"])

            x = 0
            while x < len(Meet[a][match][rank_number]["Player Name"]):
               players.append(Meet[a][match][rank_number]["Player Name"][x])
               x+=1
      final_schedule[timeslot] = courts
   save(final_schedule)
   conflictSwap(final_schedule, conflicts)

makeMeet(Meet)
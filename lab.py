import json
import openpyxl
from datetime import datetime, timedelta
from pandas import DataFrame
import random
Meet = {
   "UCD": {
      "MD": {
         "Rank 1": {
            "Player Name": [
               "Richard Huang",
               "Robert Chang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Kevin Cuan",
               "Jeremy Leung"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Sidney Wang",
               "Bo Yan"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Ethan Chan",
               "Anthony Ngo"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Adrian Lam",
               "Jon Moser"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Geoffrey Ku",
               "Vo Ly"
            ]
         }
      },
      "MS": {
         "Rank 1": {
            "Player Name": [
               "Kevin Cuan"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Robert Chang"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Justin Liu"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Neil Patel"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Jon Moser"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Sidney Wang"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Ethan Chan"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Jeff Cheung"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Ethan Chen"
            ]
         }
      },
      "XD": {
         "Rank 1": {
            "Player Name": [
               "Robert Chang",
               "Xin Huang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Steffi Ling",
               "Kevin Cuan"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Claudia Xu",
               "Jeremy Leung"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Joy Yang",
               "Justin Liu"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Stephanie Lau",
               "Anthony Ngo"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Collette Shu",
               "Ethan Chen"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Joey Mai",
               "Geoffrey Ku"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Richard Huang",
               "Amber Zhang"
            ]
         }
      },
      "WS": {
         "Rank 1": {
            "Player Name": [
               "Xin Huang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Joy Yang"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Cindy Shing"
            ]
         }
      },
      "WD": {
         "Rank 1": {
            "Player Name": [
               "Xin Huang",
               "Steffi Ling"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Iris Lee",
               "Claudia Xu"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Aysia Saeturn",
               "Diana Del Rosario"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Joey Mai",
               "Amie Zheng"
            ]
         }
      }
   },
   "UCSC": {
      "MD": {
         "Rank 1": {
            "Player Name": [
               "Brian Huang",
               "Sam Lai"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Eric Wang",
               "Brandon Wang"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Allan Sun",
               "Suneet Katrekar"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Curtis Luu",
               "Akhilesh Nidamanuri"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Yash Malegaonkar",
               "Nathan Nguyen"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Andrew Ryu",
               "Nathan Mei"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Shak Guruswami",
               "Dustin Wang"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Adam Vu ",
               "Justin Yi"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Bruce Bai",
               "Van Ly"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Curtis Luu",
               "Akhilesh Nidamanuri"
            ]
         }
      },
      "MS": {
         "Rank 1": {
            "Player Name": [
               "Sam Lai"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Allan Sun"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Evan Chen"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Eric Wang"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Anish Bansel"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Suneet Katrekar"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Aidan Au Yeung"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Andrew Ryu"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Nathan Mei"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Nathan Yu"
            ]
         },
         "Rank 11": {
            "Player Name": [
               "Yash Malegaonkar"
            ]
         },
         "Rank 12": {
            "Player Name": [
               "Nathan Nguyen"
            ]
         }
      },
      "XD": {
         "Rank 1": {
            "Player Name": [
               "Evan Chen",
               "Sarah Chun"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Sam Lai",
               "Hannah Wang"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Brian Huang",
               "Amy Sha"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Curtis Luu ",
               "Emily Lam"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Brandon Wang",
               "Natasha Kulkarni"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Shak Guruswami",
               "Vara Madem"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Akhilesh Nidamanuri",
               "Jennifer Kim"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "William Wu",
               "Jenny Lei"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Julius Chang",
               "Dorothy Li"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Brandon Wang",
               "Natasha Kulkarni"
            ]
         }
      },
      "WS": {
         "Rank 1": {
            "Player Name": [
               "Amy Sha"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Sarah Chun"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Natasha Kulkarni"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Jenny Lei"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Dorothy Li"
            ]
         }
      },
      "WD": {
         "Rank 1": {
            "Player Name": [
               "Sarah Chun",
               "Hannah Wang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Natasha Kulkarni",
               "Vara Madem"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Emily Lam",
               "Jennifer Kim"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Dorothy Li",
               "Hazel Chen"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Jenny Lei",
               "Iris Chan"
            ]
         }
      }
   }
}
def selectMatch(match_number, Meet, players, timeslot, prio_flag, priority_courts, the_court_number, priority_dict):
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
            print("conflict player:", temp_player)
            conflict = False
            continue
         else:
            if prev_player == temp_player:
               print("there will be an unavoidable conflict in time", timeslot, prev_player)
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
def conflictCheck(Meet, match, rank_choice):
   return 0
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
         SM_Results = selectMatch(match_number, Meet, players, timeslot, prio_flag, priority_courts, i, priority_dict)
         if SM_Results == True:
            break
         match = SM_Results[0]
         rank_choice = SM_Results[1]
         #conflict check must happen here in sm                                                                                                                                                    
         courts[i] = []

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


makeMeet(Meet)

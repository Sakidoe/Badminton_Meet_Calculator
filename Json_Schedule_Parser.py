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
               "Leyang Ding",
               "Richard Huang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Benson Ngai",
               "Geoffray Lee"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Jon Moser",
               "Jonathan Li"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Sidney Wang",
               "Adrian Luo"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Mariano Elizondo",
               "Jerry Qiu"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Sean Tan",
               "Kevin Cuan"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Aaron Lim",
               "Bill Wong"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Daniel Lin",
               "Yawei He"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Jordon Kwong",
               "Chimnay"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Michael Salim",
               "Kyle Kimura"
            ]
         },
         "Rank 11": {
            "Player Name": [
               "Ryan Lei",
               "Adrian Luu"
            ]
         },
         "Rank 12": {
            "Player Name": [
               "Josh Luo",
               "Karthik Villavan"
            ]
         },
         "Rank 13": {
            "Player Name": [
               "Marc Ethan Saguiped",
               "Donnovan Saelee"
            ]
         }
      },
      "MS": {
         "Rank 1": {
            "Player Name": [
               "Leyang Ding"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Kevin Cuan"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Mariano Elizondo"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Geoffray Lee"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Jon Moser"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Adrian Luo"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Sidney Wang"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Jonathan Li"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Sean Tan"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Aaron Lim"
            ]
         },
         "Rank 11": {
            "Player Name": [
               "Adrian Li"
            ]
         },
         "Rank 12": {
            "Player Name": [
               "Kyle Kimura"
            ]
         },
         "Rank 13": {
            "Player Name": [
               "Michael Salim"
            ]
         },
         "Rank 14": {
            "Player Name": [
               "Bill Wong"
            ]
         },
         "Rank 15": {
            "Player Name": [
               "Finn"
            ]
         },
         "Rank 16": {
            "Player Name": [
               "Booker Brown"
            ]
         }
      },
      "XD": {
         "Rank 1": {
            "Player Name": [
               "Leyang Ding",
               "Xin Huang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Benson Ngai",
               "Kristine Ngo"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Kevin Cuan",
               "Iris Lee"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Richard Huang",
               "Erika Lai"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Sidney Wang",
               "Betty Yang"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Adam Dinh",
               "Minh Nguyen"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Jonathan Li",
               "Ehong Ng"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Ryan Lei",
               "Jamie Yip"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Adrian Li",
               "Isabella Li"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Richard Huang",
               "Livia Rice"
            ]
         },
         "Rank 11": {
            "Player Name": [
               "Aaron Lim",
               "Gaby Solei"
            ]
         },
         "Rank 12": {
            "Player Name": [
               "Daniel Lin",
               "Carolyn Surypermana"
            ]
         },
         "Rank 13": {
            "Player Name": [
               "Booker Brown",
               "Chonticha Phanphanit"
            ]
         },
         "Rank 14": {
            "Player Name": [
               "Jerry Qiu",
               "Suhani Shokeen"
            ]
         }
      },
      "WS": {
         "Rank 1": {
            "Player Name": [
               "Jamie Yip"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Carolyn Suryapermana"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Chonticha Phanphanit"
            ]
         }
      },
      "WD": {
         "Rank 1": {
            "Player Name": [
               "Xin Huang",
               "Betty Yang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Kristine Ngo",
               "Erika Lai"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Muyen Liang",
               "Jamie Yip"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Livia Rice",
               "Isabella Li"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Winnie Wu",
               "Mallika Chou"
            ]
         }
      }
   },
   "UCB": {
      "MD": {
         "Rank 1": {
            "Player Name": [
               "Patrick Chi",
               "Jason Arya"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Ashley Huang",
               "Natalie Chi"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Aarav Rathi",
               "Shengkai Jiang"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Reanne Chan",
               "Ariel Shan"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Jonathan Pan",
               "Harry Zhang"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Kelsey Lin",
               "Jansen Mok"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Jonathan Pan",
               "Jeff Chen"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Arav Sachdeva",
               "Arun Yadavalli"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Kyle Huang",
               "Khai Ho"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Howard Huang",
               "Cameron Kato"
            ]
         },
         "Rank 11": {
            "Player Name": [
               "Zevin Bansal",
               "Vinayak Prathikanti"
            ]
         },
         "Rank 12": {
            "Player Name": [
               "Justin Wang",
               "Anton Luu"
            ]
         },
         "Rank 13": {
            "Player Name": [
               "Wesley Tan",
               "Jansen Mok"
            ]
         }
      },
      "MS": {
         "Rank 1": {
            "Player Name": [
               "Adam Tay"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Brad Chiu"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Brad Chiu"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Zheng Zhou"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Zheng Zhou"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Jason Arya"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Ryan Zhu"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Ryan Zhu"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Arun Yadavalli"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Jake Kim"
            ]
         },
         "Rank 11": {
            "Player Name": [
               "Arav Sachdeva"
            ]
         },
         "Rank 12": {
            "Player Name": [
               "Khai Ho"
            ]
         },
         "Rank 13": {
            "Player Name": [
               "Joon Choi"
            ]
         },
         "Rank 14": {
            "Player Name": [
               "Jack Chu"
            ]
         },
         "Rank 15": {
            "Player Name": [
               "Arion Togelang"
            ]
         },
         "Rank 16": {
            "Player Name": [
               "Kwanghyun Kim"
            ]
         }
      },
      "XD": {
         "Rank 1": {
            "Player Name": [
               "Adam Tay",
               "Angie Huang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Patrick Chi",
               "Natalie Chi"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Ashton Lee",
               "Ashley Huang"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Patrick Chi",
               "Kaylee Wang"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Ashton Lee",
               "Angie Huang"
            ]
         },
         "Rank 6": {
            "Player Name": [
               "Shengkai Jiang",
               "Kristin Song"
            ]
         },
         "Rank 7": {
            "Player Name": [
               "Aarav Rathi",
               "Jane Dong"
            ]
         },
         "Rank 8": {
            "Player Name": [
               "Kelsey Lin",
               "Trinity Nguyen"
            ]
         },
         "Rank 9": {
            "Player Name": [
               "Howard Huang",
               "Rosamund Li"
            ]
         },
         "Rank 10": {
            "Player Name": [
               "Jeff Chen",
               "Stephanie Kuang"
            ]
         },
         "Rank 11": {
            "Player Name": [
               "Howie Liang",
               "Angel Yeung"
            ]
         },
         "Rank 12": {
            "Player Name": [
               "Vinayak Prathikanti",
               "Caitlin Tong"
            ]
         },
         "Rank 13": {
            "Player Name": [
               "Ajay Sharma",
               "Zinong Wang"
            ]
         },
         "Rank 14": {
            "Player Name": [
               "Haoran Qu",
               "Janina Schieneman"
            ]
         }
      },
      "WS": {
         "Rank 1": {
            "Player Name": [
               "Ziyi Huang"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Emily Qian"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Chaemin Lee"
            ]
         }
      },
      "WD": {
         "Rank 1": {
            "Player Name": [
               "Reanne Chan",
               "Ariel Shan"
            ]
         },
         "Rank 2": {
            "Player Name": [
               "Kaylee Wang",
               "Kristin Song"
            ]
         },
         "Rank 3": {
            "Player Name": [
               "Clarissa Chen",
               "Yuhe Lin"
            ]
         },
         "Rank 4": {
            "Player Name": [
               "Angelina Wang",
               "Janina Schieneman"
            ]
         },
         "Rank 5": {
            "Player Name": [
               "Anni Zhang",
               "Phoebe Shen"
            ]
         }
      }
   }
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
      priority_courts = 0
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
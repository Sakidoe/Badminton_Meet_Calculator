import xlsxwriter
final_schedule = {
   "11:00": {
      "1": [
         "WS3",
         [
            "Cindy Shing"
         ],
         [
            "Natasha Kulkarni"
         ]
      ],
      "2": [
         "XD3",
         [
            "Claudia Xu",
            "Jeremy Leung"
         ],
         [
            "Brian Huang",
            "Amy Sha"
         ]
      ],
      "3": [
         "MD1",
         [
            "Richard Huang",
            "Robert Chang"
         ],
         [
            "Brian Huang",
            "Sam Lai"
         ]
      ],
      "4": [
         "WS4",
         [
            "Xin Huang"
         ],
         [
            "Jenny Lei"
         ]
      ],
      "5": [
         "WD3",
         [
            "Aysia Saeturn",
            "Diana Del Rosario"
         ],
         [
            "Emily Lam",
            "Jennifer Kim"
         ]
      ],
      "6": [
         "MD5",
         [
            "Adrian Lam",
            "Jon Moser"
         ],
         [
            "Yash Malegaonkar",
            "Nathan Nguyen"
         ]
      ]
   },
   "11:30": {
      "1": [
         "WD2",
         [
            "Iris Lee",
            "Claudia Xu"
         ],
         [
            "Natasha Kulkarni",
            "Vara Madem"
         ]
      ],
      "2": [
         "WD1",
         [
            "Xin Huang",
            "Steffi Ling"
         ],
         [
            "Sarah Chun",
            "Hannah Wang"
         ]
      ],
      "3": [
         "MD3",
         [
            "Sidney Wang",
            "Bo Yan"
         ],
         [
            "Allan Sun",
            "Suneet Katrekar"
         ]
      ],
      "4": [
         "XD7",
         [
            "Joey Mai",
            "Geoffrey Ku"
         ],
         [
            "Akhilesh Nidamanuri",
            "Jennifer Kim"
         ]
      ],
      "5": [
         "MD2",
         [
            "Kevin Cuan",
            "Jeremy Leung"
         ],
         [
            "Eric Wang",
            "Brandon Wang"
         ]
      ],
      "6": [
         "MS9",
         [
            "Ethan Chen"
         ],
         [
            "Nathan Mei"
         ]
      ]
   },
   "12:00": {
      "1": [
         "WD5",
         [
            "Xin Huang",
            "Steffi Ling"
         ],
         [
            "Jenny Lei",
            "Iris Chan"
         ]
      ],
      "2": [
         "MS3",
         [
            "Justin Liu"
         ],
         [
            "Evan Chen"
         ]
      ],
      "3": [
         "WS2",
         [
            "Joy Yang"
         ],
         [
            "Sarah Chun"
         ]
      ],
      "4": [
         "MD10",
         [
            "Ethan Chan",
            "Anthony Ngo"
         ],
         [
            "Curtis Luu",
            "Akhilesh Nidamanuri"
         ]
      ],
      "5": [
         "MS11",
         [
            "Robert Chang"
         ],
         [
            "Yash Malegaonkar"
         ]
      ],
      "6": [
         "WD4",
         [
            "Joey Mai",
            "Amie Zheng"
         ],
         [
            "Dorothy Li",
            "Hazel Chen"
         ]
      ]
   },
   "12:30": {
      "1": [
         "MS2",
         [
            "Robert Chang"
         ],
         [
            "Allan Sun"
         ]
      ],
      "2": [
         "MD6",
         [
            "Geoffrey Ku",
            "Vo Ly"
         ],
         [
            "Andrew Ryu",
            "Nathan Mei"
         ]
      ],
      "3": [
         "WS1",
         [
            "Xin Huang"
         ],
         [
            "Amy Sha"
         ]
      ],
      "4": [
         "XD1",
         [
            "Robert Chang",
            "Xin Huang"
         ],
         [
            "Evan Chen",
            "Sarah Chun"
         ]
      ],
      "5": [
         "MD8",
         [
            "Kevin Cuan",
            "Jeremy Leung"
         ],
         [
            "Adam Vu ",
            "Justin Yi"
         ]
      ],
      "6": [
         "XD8",
         [
            "Richard Huang",
            "Amber Zhang"
         ],
         [
            "William Wu",
            "Jenny Lei"
         ]
      ]
   },
   "01:00": {
      "1": [
         "WS5",
         [
            "Joy Yang"
         ],
         [
            "Dorothy Li"
         ]
      ],
      "2": [
         "XD2",
         [
            "Steffi Ling",
            "Kevin Cuan"
         ],
         [
            "Sam Lai",
            "Hannah Wang"
         ]
      ],
      "3": [
         "MD7",
         [
            "Richard Huang",
            "Robert Chang"
         ],
         [
            "Shak Guruswami",
            "Dustin Wang"
         ]
      ],
      "4": [
         "MS12",
         [
            "Justin Liu"
         ],
         [
            "Nathan Nguyen"
         ]
      ],
      "5": [
         "XD5",
         [
            "Stephanie Lau",
            "Anthony Ngo"
         ],
         [
            "Brandon Wang",
            "Natasha Kulkarni"
         ]
      ],
      "6": [
         "MS7",
         [
            "Ethan Chan"
         ],
         [
            "Aidan Au Yeung"
         ]
      ]
   },
   "01:30": {
      "1": [
         "XD6",
         [
            "Collette Shu",
            "Ethan Chen"
         ],
         [
            "Shak Guruswami",
            "Vara Madem"
         ]
      ],
      "2": [
         "MS1",
         [
            "Kevin Cuan"
         ],
         [
            "Sam Lai"
         ]
      ],
      "3": [
         "MS5",
         [
            "Jon Moser"
         ],
         [
            "Anish Bansel"
         ]
      ],
      "4": [
         "MD4",
         [
            "Ethan Chan",
            "Anthony Ngo"
         ],
         [
            "Curtis Luu",
            "Akhilesh Nidamanuri"
         ]
      ],
      "5": [
         "MS10",
         [
            "Kevin Cuan"
         ],
         [
            "Nathan Yu"
         ]
      ],
      "6": [
         "MS8",
         [
            "Jeff Cheung"
         ],
         [
            "Andrew Ryu"
         ]
      ]
   },
   "02:00": {
      "1": [
         "XD4",
         [
            "Joy Yang",
            "Justin Liu"
         ],
         [
            "Curtis Luu ",
            "Emily Lam"
         ]
      ],
      "2": [
         "XD10",
         [
            "Steffi Ling",
            "Kevin Cuan"
         ],
         [
            "Brandon Wang",
            "Natasha Kulkarni"
         ]
      ],
      "3": [
         "MD9",
         [
            "Sidney Wang",
            "Bo Yan"
         ],
         [
            "Bruce Bai",
            "Van Ly"
         ]
      ],
      "4": [
         "XD9",
         [
            "Robert Chang",
            "Xin Huang"
         ],
         [
            "Julius Chang",
            "Dorothy Li"
         ]
      ],
      "5": [
         "MS4",
         [
            "Neil Patel"
         ],
         [
            "Eric Wang"
         ]
      ],
      "6": [
         "MS6",
         [
            "Sidney Wang"
         ],
         [
            "Suneet Katrekar"
         ]
      ]
   },
   "02:30": {},
   "03:00": {},
   "03:30": {},
   "04:00": {},
   "04:30": {},
   "05:00": {},
   "05:30": {}
}
# remember to adapt this later
team1 = "UCD"
team2 = "UCSC"
conflicts = {'01:00': ['Sarah Chun', 'Jenny Lei'], '02:00': ['Natasha Kulkarni']}
def conflictCheck(final_schedule, conflicts):
    for i in final_schedule:
        on_court = set()
        for j in final_schedule[i].values():
            for player in j:
                on_court.add(player[0])
                if len(player) > 1:
                    on_court.add(player[1])
            


def conflictDetect(final_schedule, conflicts, temp_dict):
    result_dict = dict()
    for i in conflicts.keys():
        info = set()
        for match_rank, match_info in final_schedule[i].items():
            for player in match_info:
                if player[0] in info:
                    print("conflict: ", player[0], "in match", match_rank, match_info, "at time", i)
                    if i not in result_dict.keys():
                        result_dict[i] = {match_rank : [match_info]}

                    else:
                        result_dict[i][match_rank] = match_info
                else:
                    info.add(player[0])
                try:
                    if player[1] in info:
                        print("conflict: ", player[1], "in match", match_rank, match_info, "at time", i)
                        if i not in result_dict.keys():
                            result_dict[i] = { match_rank : [match_info] }
                        else:
                            result_dict[i][match_rank] = [match_info]
                    else:
                        info.add(player[1])
                except:
                    pass
    print(result_dict)
    return result_dict
#temp_dict = dict()
#shuffle_conflicts = conflictDetect(final_schedule, conflicts, temp_dict)
#conflict_free_schedule = conflictCheck(final_schedule, shuffle_conflicts)
title = team1 + " vs " + team2
# for i in final_schedule.keys():
#    title = title + " vs " + i
court_counter = len(final_schedule[list(final_schedule.keys())[0]].keys())
print(court_counter)

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column("A:M", 15)
worksheet.set_column("E:F", 20)
worksheet.set_column("H:I", 20)
meet_title_format = workbook.add_format(
    {
        "bold": 1,
        "underline" : 1,
        "border": 1,
        "align": "center",
        "valign": "vcenter",
        "fg_color": "#FFD24C",
        "font" : "montserrat",
        "size" : 22,
         
    }
)
categories = workbook.add_format( 
    {   
        "bold": 1,
        "border": 1,
        "align": "center",
        "valign": "vcenter",
        "color" : "#FFFFFF",
        "fg_color": "#355B85",
        "font" : "montserrat",
        "size" : 10,
        "bottom" : 6,
        }
)
data_blue = workbook.add_format(
    {
      "font" : "montserrat",
      "align": "center",
      "size" : 10,
      "border": 1,
      "fg_color": "#B3C1D1",
     }
)
data_yellow = workbook.add_format(
    {
      "font" : "montserrat",
      "align": "center",
      "size" : 10,
      "border": 1,
      "fg_color": "#FFDF80",
     }
)
data_black = workbook.add_format(
    {
      "font" : "montserrat",
      "align": "center",
      "size" : 10,
      "border": 1,
      "bold" : 1,
      "color" : "#FFFFFF",
      "fg_color": "#333333",
     }
)
data_red = workbook.add_format(
    {
      "font" : "montserrat",
      "align": "center",
      "size" : 10,
      "border": 1,
      "bold" : 1,
      "color" : "#FFFFFF",
      "fg_color": "#79242F",
     }
)
data_grey = workbook.add_format(
    {
      "font" : "montserrat",
      "align": "center",
      "size" : 10,
      "border": 1,
      "fg_color": "#CCCCCC",
     }
)

worksheet.merge_range("A1:K4", title, meet_title_format)

worksheet.write('A5', 'Schedule', categories)
worksheet.write('B5', 'Court', categories)
worksheet.write('C5', 'In progress', categories)
worksheet.write('D5', 'Event', categories)
worksheet.merge_range('E5:F5', team1, categories)
worksheet.write('G5', 'vs.', categories)
worksheet.merge_range('H5:I5', team2, categories)
worksheet.merge_range('J5:K5', 'Score (Winner First)', categories)
start_counter = 6
start_cell = "A6"
end_cell = "A6"
team1_ATeam = []
team2_ATeam = []
team1_OTeam = []
team2_OTeam = []
for sched_i in final_schedule:
   end_counter = start_counter + court_counter -1
   start_cell = "A" + str(start_counter)
   end_cell=  "A" + str(end_counter)
   t_format = start_cell + ":" + end_cell
   if final_schedule[sched_i] != {}:
      worksheet.merge_range(t_format, sched_i, categories)
   c_number = 1
   for i in range(int(start_counter), int(end_counter)+1):
      court_cell = "B"+ str(i)
      event_cell = "D" + str(i)
      vs_cell = "G" + str(i)
      progress_cell = "C" + str(i)
      team1_cell = "E"+ str(i) + ":F" + str(i)
      team2_cell = "H" + str(i) + ":I" + str(i)
      score_cell = "J" + str(i) + ":K" + str(i)
      victory_cell_t1 = "L" + str(i)
      victory_cell_t2 = "M" + str(i)

      try:
         #print(final_schedule[sched_i][str(c_number)][1])
         event_data = final_schedule[sched_i][str(c_number)][0]
         if (event_data[2] == "1" or event_data[2] == "2" or event_data[2] == "3") and len(event_data) == 3:
            #print("this is a priority match", event_data)
            team1_ATeam.append("L" + str(i))
            team2_ATeam.append("M" + str(i))
         worksheet.write(progress_cell, "", data_yellow)
         try:
            team1_data = final_schedule[sched_i][str(c_number)][1][0] + " + " + final_schedule[sched_i][str(c_number)][1][1]
         except:
            team1_data = final_schedule[sched_i][str(c_number)][1][0]
         try:
            team2_data = final_schedule[sched_i][str(c_number)][2][0] + " + " + final_schedule[sched_i][str(c_number)][2][1]
         except:
            team2_data = final_schedule[sched_i][str(c_number)][2][0]
         worksheet.write(event_cell, event_data, data_yellow)
         worksheet.write(vs_cell, "vs", categories)
         worksheet.merge_range(team1_cell, str(team1_data), data_blue)
         worksheet.merge_range(team2_cell, str(team2_data), data_blue)
         worksheet.merge_range(score_cell, "",data_yellow)
         worksheet.write(victory_cell_t1, 1, data_blue)
         worksheet.write(victory_cell_t2, 1, data_blue)
         worksheet.write(court_cell, c_number, data_blue)
         team1_OTeam.append("L" + str(i))
         team2_OTeam.append("M" + str(i))

      
      except:
         pass
      c_number +=1
   start_counter = end_counter+1
worksheet.write("L1", team1, data_red)
worksheet.write("M1", team2, data_red)
worksheet.merge_range("L2:M2", "A-Team Tally", data_black)
worksheet.merge_range("L4:M4", "Overall Tally", data_black)
sumat1 = ""
sumat2 = ""
sumot1 = ""
sumot2 = ""
for at in range(0, len(team1_ATeam)):
    sumat1 = sumat1 + ", " + team1_ATeam[at]
    sumat2 = sumat2 + ", " + team2_ATeam[at]
for ot in range(0, len(team1_OTeam)):
    sumot1 = sumot1 + ", " + team1_OTeam[ot]
    sumot2 = sumot2 + ", " + team2_OTeam[ot]
sumat1 = "=SUM(" + sumat1[1:] + ")"
sumat2 = "=SUM(" + sumat2[1:] + ")"
sumot1 = "=SUM(" + sumot1[1:] + ")"
sumot2 = "=SUM(" + sumot2[1:] + ")"
worksheet.write_formula('L3', sumat1, data_grey)
worksheet.write_formula('M3', sumat2, data_grey)
worksheet.write_formula('L5', sumot1, data_grey)
worksheet.write_formula('M5', sumot2, data_grey)
print(sumat1)
      #worksheet.write(event_cell, final_schedule[sched_i][str(c_number)][0])
        
workbook.close()
import xlsxwriter
final_schedule = {
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
# remember to adapt this later
team1 = "UCD"
team2 = "UCSC"
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
        "underline": 1,
        "border": 1,
        "align": "center",
        "valign": "vcenter",
        "fg_color": "#FFD24C",
        "font_name": "montserrat",
        "font_size": 22,
    }
)

categories = workbook.add_format( 
    {   
        "bold": 1,
        "border": 1,
        "align": "center",
        "valign": "vcenter",
        "font_color": "#FFFFFF",
        "fg_color": "#355B85",
        "font_name": "montserrat",
        "font_size": 10,
        "bottom": 6,
    }
)

data_blue = workbook.add_format(
    {
        "font_name": "montserrat",
        "align": "center",
        "font_size": 10,
        "border": 1,
        "fg_color": "#B3C1D1",
    }
)

data_yellow = workbook.add_format(
    {
        "font_name": "montserrat",
        "align": "center",
        "font_size": 10,
        "border": 1,
        "fg_color": "#FFDF80",
    }
)

data_black = workbook.add_format(
    {
        "font_name": "montserrat",
        "align": "center",
        "font_size": 10,
        "border": 1,
        "bold": 1,
        "font_color": "#FFFFFF",
        "fg_color": "#333333",
    }
)

data_red = workbook.add_format(
    {
        "font_name": "montserrat",
        "align": "center",
        "font_size": 10,
        "border": 1,
        "bold": 1,
        "font_color": "#FFFFFF",
        "fg_color": "#79242F",
    }
)

data_grey = workbook.add_format(
    {
        "font_name": "montserrat",
        "align": "center",
        "font_size": 10,
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
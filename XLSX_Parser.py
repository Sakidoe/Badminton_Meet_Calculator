import xlsxwriter
final_schedule = {
   "10:00": {
      "1": [
         "WD1",
         [
            "Xin Huang",
            "Betty Yang"
         ],
         [
            "Reanne Chan",
            "Ariel Shan"
         ]
      ],
      "2": [
         "MS1",
         [
            "Leyang Ding"
         ],
         [
            "Adam Tay"
         ]
      ],
      "3": [
         "WS1",
         [
            "Jamie Yip"
         ],
         [
            "Ziyi Huang"
         ]
      ],
      "4": [
         "WD5",
         [
            "Winnie Wu",
            "Mallika Chou"
         ],
         [
            "Anni Zhang",
            "Phoebe Shen"
         ]
      ],
      "5": [
         "WS2",
         [
            "Carolyn Suryapermana"
         ],
         [
            "Emily Qian"
         ]
      ],
      "6": [
         "MD6",
         [
            "Sean Tan",
            "Kevin Cuan"
         ],
         [
            "Kelsey Lin",
            "Jansen Mok"
         ]
      ]
   },
   "10:45": {
      "1": [
         "WD2",
         [
            "Kristine Ngo",
            "Erika Lai"
         ],
         [
            "Kaylee Wang",
            "Kristin Song"
         ]
      ],
      "2": [
         "MS4",
         [
            "Geoffray Lee"
         ],
         [
            "Zheng Zhou"
         ]
      ],
      "3": [
         "WS3",
         [
            "Chonticha Phanphanit"
         ],
         [
            "Chaemin Lee"
         ]
      ],
      "4": [
         "WD3",
         [
            "Muyen Liang",
            "Jamie Yip"
         ],
         [
            "Clarissa Chen",
            "Yuhe Lin"
         ]
      ],
      "5": [
         "MD3",
         [
            "Jon Moser",
            "Jonathan Li"
         ],
         [
            "Aarav Rathi",
            "Shengkai Jiang"
         ]
      ],
      "6": [
         "MD11",
         [
            "Ryan Lei",
            "Adrian Luu"
         ],
         [
            "Zevin Bansal",
            "Vinayak Prathikanti"
         ]
      ]
   },
   "11:30": {
      "1": [
         "MD4",
         [
            "Sidney Wang",
            "Adrian Luo"
         ],
         [
            "Reanne Chan",
            "Ariel Shan"
         ]
      ],
      "2": [
         "XD8",
         [
            "Ryan Lei",
            "Jamie Yip"
         ],
         [
            "Kelsey Lin",
            "Trinity Nguyen"
         ]
      ],
      "3": [
         "MS8",
         [
            "Jonathan Li"
         ],
         [
            "Ryan Zhu"
         ]
      ],
      "4": [
         "MD9",
         [
            "Jordon Kwong",
            "Chimnay"
         ],
         [
            "Kyle Huang",
            "Khai Ho"
         ]
      ],
      "5": [
         "XD9",
         [
            "Adrian Li",
            "Isabella Li"
         ],
         [
            "Howard Huang",
            "Rosamund Li"
         ]
      ],
      "6": [
         "MD1",
         [
            "Leyang Ding",
            "Richard Huang"
         ],
         [
            "Patrick Chi",
            "Jason Arya"
         ]
      ]
   },
   "12:15": {
      "1": [
         "XD10",
         [
            "Richard Huang",
            "Livia Rice"
         ],
         [
            "Jeff Chen",
            "Stephanie Kuang"
         ]
      ],
      "2": [
         "MD13",
         [
            "Marc Ethan Saguiped",
            "Donnovan Saelee"
         ],
         [
            "Wesley Tan",
            "Jansen Mok"
         ]
      ],
      "3": [
         "MS14",
         [
            "Bill Wong"
         ],
         [
            "Jack Chu"
         ]
      ],
      "4": [
         "MS11",
         [
            "Adrian Li"
         ],
         [
            "Arav Sachdeva"
         ]
      ],
      "5": [
         "MD2",
         [
            "Benson Ngai",
            "Geoffray Lee"
         ],
         [
            "Ashley Huang",
            "Natalie Chi"
         ]
      ],
      "6": [
         "XD14",
         [
            "Jerry Qiu",
            "Suhani Shokeen"
         ],
         [
            "Haoran Qu",
            "Janina Schieneman"
         ]
      ]
   },
   "01:00": {
      "1": [
         "MD5",
         [
            "Mariano Elizondo",
            "Jerry Qiu"
         ],
         [
            "Jonathan Pan",
            "Harry Zhang"
         ]
      ],
      "2": [
         "MS15",
         [
            "Finn"
         ],
         [
            "Arion Togelang"
         ]
      ],
      "3": [
         "XD11",
         [
            "Aaron Lim",
            "Gaby Solei"
         ],
         [
            "Howie Liang",
            "Angel Yeung"
         ]
      ],
      "4": [
         "MS6",
         [
            "Adrian Luo"
         ],
         [
            "Jason Arya"
         ]
      ],
      "5": [
         "XD13",
         [
            "Booker Brown",
            "Chonticha Phanphanit"
         ],
         [
            "Ajay Sharma",
            "Zinong Wang"
         ]
      ],
      "6": [
         "XD2",
         [
            "Benson Ngai",
            "Kristine Ngo"
         ],
         [
            "Patrick Chi",
            "Natalie Chi"
         ]
      ]
   },
   "01:45": {
      "1": [
         "XD7",
         [
            "Jonathan Li",
            "Ehong Ng"
         ],
         [
            "Aarav Rathi",
            "Jane Dong"
         ]
      ],
      "2": [
         "MS16",
         [
            "Booker Brown"
         ],
         [
            "Kwanghyun Kim"
         ]
      ],
      "3": [
         "XD12",
         [
            "Daniel Lin",
            "Carolyn Surypermana"
         ],
         [
            "Vinayak Prathikanti",
            "Caitlin Tong"
         ]
      ],
      "4": [
         "MD12",
         [
            "Josh Luo",
            "Karthik Villavan"
         ],
         [
            "Justin Wang",
            "Anton Luu"
         ]
      ],
      "5": [
         "WD4",
         [
            "Livia Rice",
            "Isabella Li"
         ],
         [
            "Angelina Wang",
            "Janina Schieneman"
         ]
      ],
      "6": [
         "MS13",
         [
            "Michael Salim"
         ],
         [
            "Joon Choi"
         ]
      ]
   },
   "02:30": {
      "1": [
         "MD7",
         [
            "Aaron Lim",
            "Bill Wong"
         ],
         [
            "Jonathan Pan",
            "Jeff Chen"
         ]
      ],
      "2": [
         "XD6",
         [
            "Adam Dinh",
            "Minh Nguyen"
         ],
         [
            "Shengkai Jiang",
            "Kristin Song"
         ]
      ],
      "3": [
         "XD3",
         [
            "Kevin Cuan",
            "Iris Lee"
         ],
         [
            "Ashton Lee",
            "Ashley Huang"
         ]
      ],
      "4": [
         "XD4",
         [
            "Richard Huang",
            "Erika Lai"
         ],
         [
            "Patrick Chi",
            "Kaylee Wang"
         ]
      ],
      "5": [
         "MD8",
         [
            "Daniel Lin",
            "Yawei He"
         ],
         [
            "Arav Sachdeva",
            "Arun Yadavalli"
         ]
      ],
      "6": [
         "MD10",
         [
            "Michael Salim",
            "Kyle Kimura"
         ],
         [
            "Howard Huang",
            "Cameron Kato"
         ]
      ]
   },
   "03:15": {
      "1": [
         "MS7",
         [
            "Sidney Wang"
         ],
         [
            "Ryan Zhu"
         ]
      ],
      "2": [
         "MS10",
         [
            "Aaron Lim"
         ],
         [
            "Jake Kim"
         ]
      ],
      "3": [
         "MS5",
         [
            "Jon Moser"
         ],
         [
            "Zheng Zhou"
         ]
      ],
      "4": [
         "XD1",
         [
            "Leyang Ding",
            "Xin Huang"
         ],
         [
            "Adam Tay",
            "Angie Huang"
         ]
      ],
      "5": [
         "MS3",
         [
            "Mariano Elizondo"
         ],
         [
            "Brad Chiu"
         ]
      ],
      "6": [
         "MS9",
         [
            "Sean Tan"
         ],
         [
            "Arun Yadavalli"
         ]
      ]
   },
   "04:00": {
      "1": [
         "MS12",
         [
            "Kyle Kimura"
         ],
         [
            "Khai Ho"
         ]
      ],
      "2": [
         "MS2",
         [
            "Kevin Cuan"
         ],
         [
            "Brad Chiu"
         ]
      ],
      "3": [
         "XD5",
         [
            "Sidney Wang",
            "Betty Yang"
         ],
         [
            "Ashton Lee",
            "Angie Huang"
         ]
      ]
   }
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
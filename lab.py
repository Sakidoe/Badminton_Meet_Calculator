import json
import openpyxl
from datetime import datetime
from pandas import DataFrame
Meet = {
   "UCSC": {
      "MD": {
         "Rank 1.0": {
            "Player Name": [
               "Brian Huang",
               "Sam Lai"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Eric Wang",
               "Brandon Wang"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Allan Sun",
               "Suneet Katrekar"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Curtis Luu",
               "Akhilesh Nidamanuri"
            ]
         },
         "Rank 5.0": {
            "Player Name": [
               "Yash Malegaonkar",
               "Nathan Nguyen"
            ]
         },
         "Rank 6.0": {
            "Player Name": [
               "Andrew Ryu",
               "Nathan Mei"
            ]
         },
         "Rank 7.0": {
            "Player Name": [
               "Shak Guruswami",
               "Dustin Wang"
            ]
         },
         "Rank 8.0": {
            "Player Name": [
               "Adam Vu ",
               "Justin Yi"
            ]
         },
         "Rank 9.0": {
            "Player Name": [
               "Bruce Bai",
               "Van Ly"
            ]
         },
         "Rank 10.0": {
            "Player Name": [
               "Curtis Luu",
               "Akhilesh Nidamanuri"
            ]
         }
      },
      "MS": {
         "Rank 1.0": {
            "Player Name": [
               "Sam Lai"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Allan Sun"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Evan Chen"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Eric Wang"
            ]
         },
         "Rank 5.0": {
            "Player Name": [
               "Anish Bansel"
            ]
         },
         "Rank 6.0": {
            "Player Name": [
               "Suneet Katrekar"
            ]
         },
         "Rank 7.0": {
            "Player Name": [
               "Aidan Au Yeung"
            ]
         },
         "Rank 8.0": {
            "Player Name": [
               "Andrew Ryu"
            ]
         },
         "Rank 9.0": {
            "Player Name": [
               "Nathan Mei"
            ]
         },
         "Rank 10.0": {
            "Player Name": [
               "Nathan Yu"
            ]
         },
         "Rank 11.0": {
            "Player Name": [
               "Yash Malegaonkar"
            ]
         },
         "Rank 12.0": {
            "Player Name": [
               "Nathan Nguyen"
            ]
         }
      },
      "XD": {
         "Rank 1.0": {
            "Player Name": [
               "Evan Chen",
               "Sarah Chun"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Sam Lai",
               "Hannah Wang"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Brian Huang",
               "Amy Sha"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Curtis Luu ",
               "Emily Lam"
            ]
         },
         "Rank 5.0": {
            "Player Name": [
               "Brandon Wang",
               "Natasha Kulkarni"
            ]
         },
         "Rank 6.0": {
            "Player Name": [
               "Shak Guruswami",
               "Vara Madem"
            ]
         },
         "Rank 7.0": {
            "Player Name": [
               "Akhilesh Nidamanuri",
               "Jennifer Kim"
            ]
         },
         "Rank 8.0": {
            "Player Name": [
               "William Wu",
               "Jenny Lei"
            ]
         },
         "Rank 9.0": {
            "Player Name": [
               "Julius Chang",
               "Dorothy Li"
            ]
         },
         "Rank 10.0": {
            "Player Name": [
               "Brandon Wang",
               "Natasha Kulkarni"
            ]
         }
      },
      "WS": {
         "Rank 1.0": {
            "Player Name": [
               "Amy Sha"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Sarah Chun"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Natasha Kulkarni"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Jenny Lei"
            ]
         },
         "Rank 5.0": {
            "Player Name": [
               "Dorothy Li"
            ]
         }
      },
      "WD": {
         "Rank 1.0": {
            "Player Name": [
               "Sarah Chun",
               "Hannah Wang"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Natasha Kulkarni",
               "Vara Madem"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Emily Lam",
               "Jennifer Kim"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Dorothy Li",
               "Hazel Chen"
            ]
         },
         "Rank 5.0": {
            "Player Name": [
               "Jenny Lei",
               "Iris Chan"
            ]
         }
      }
   },
   "UCD": {
      "MD": {
         "Rank 1.0": {
            "Player Name": [
               "Richard Huang",
               "Robert Chang"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Kevin Cuan",
               "Jeremy Leung"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Sidney Wang",
               "Bo Yan"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Ethan Chan",
               "Anthony Ngo"
            ]
         },
         "Rank 5.0": {
            "Player Name": [
               "Adrian Lam",
               "Jon Moser"
            ]
         },
         "Rank 6.0": {
            "Player Name": [
               "Geoffrey Ku",
               "Vo Ly"
            ]
         }
      },
      "MS": {
         "Rank 1.0": {
            "Player Name": [
               "Kevin Cuan"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Robert Chang"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Justin Liu"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Neil Patel"
            ]
         },
         "Rank 5.0": {
            "Player Name": [
               "Jon Moser"
            ]
         },
         "Rank 6.0": {
            "Player Name": [
               "Sidney Wang"
            ]
         },
         "Rank 7.0": {
            "Player Name": [
               "Ethan Chan"
            ]
         },
         "Rank 8.0": {
            "Player Name": [
               "Jeff Cheung"
            ]
         },
         "Rank 9.0": {
            "Player Name": [
               "Ethan Chen"
            ]
         }
      },
      "XD": {
         "Rank 1.0": {
            "Player Name": [
               "Robert Chang",
               "Xin Huang"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Steffi Ling",
               "Kevin Cuan"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Claudia Xu",
               "Jeremy Leung"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Joy Yang",
               "Justin Liu"
            ]
         },
         "Rank 5.0": {
            "Player Name": [
               "Stephanie Lau",
               "Anthony Ngo"
            ]
         },
         "Rank 6.0": {
            "Player Name": [
               "Collette Shu",
               "Ethan Chen"
            ]
         },
         "Rank 7.0": {
            "Player Name": [
               "Joey Mai",
               "Geoffrey Ku"
            ]
         },
         "Rank 8.0": {
            "Player Name": [
               "Richard Huang",
               "Amber Zhang"
            ]
         }
      },
      "WS": {
         "Rank 1.0": {
            "Player Name": [
               "Xin Huang"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Joy Yang"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Cindy Shing"
            ]
         }
      },
      "WD": {
         "Rank 1.0": {
            "Player Name": [
               "Xin Huang",
               "Steffi Ling"
            ]
         },
         "Rank 2.0": {
            "Player Name": [
               "Iris Lee",
               "Claudia Xu"
            ]
         },
         "Rank 3.0": {
            "Player Name": [
               "Aysia Saeturn",
               "Diana Del Rosario"
            ]
         },
         "Rank 4.0": {
            "Player Name": [
               "Joey Mai",
               "Amie Zheng"
            ]
         }
      }
   }
}
def makeMeet(Meet):# for a MEET, not trimeet
    #first make structure: how long each game will take, how many courts, how much time
    #priority courts named courts 1, 2 and 3. <- these hold the best courts.
    
    print("//MAKE PROGRAM START\\\ ")
    tpm = input("what is the time given for each game cycle? write in terms of minutes(30 = 30 minutes)") #tpm = time per match
    meet_time_start = input("when does the meet start? Write in the 24:00 clock format(16:00 = 4pm)")
    meet_time_end = input("When does the meet end? Write in the 24:00 clock format(16:00 = 4pm)")
    court_number = input("How many courts are used in this meet?")
    t1 = datetime.strptime(meet_time_start, "%H:%M")
    t2 = datetime.strptime(meet_time_end, "%H:%M")
    difference = t2 - t1
    plausible_minutes = difference.total_seconds() / 60
    plausible_total_matches = (plausible_minutes / int(tpm)) * int(court_number)
    plausible_check = True
    MD_MAX = 0
    MS_MAX = 0
    XD_MAX = 0
    WD_MAX = 0
    WS_MAX = 0
    for i in Meet:
        for j in Meet[i]:
            if j == "MD" and len(Meet[i][j].values()) > MD_MAX:
                MD_MAX = len(Meet[i][j].values())
            elif j == "MS" and len(Meet[i][j].values()) > MS_MAX:
                MS_MAX = len(Meet[i][j].values())
            elif j == "XD" and len(Meet[i][j].values()) > XD_MAX:
                XD_MAX = len(Meet[i][j].values())
            elif j == "WD" and len(Meet[i][j].values()) > WD_MAX:
                WD_MAX = len(Meet[i][j].values())
            elif j == "WS" and len(Meet[i][j].values()) > WS_MAX:
                WS_MAX = len(Meet[i][j].values())
    print("MD" , MD_MAX,"MS" , MS_MAX,"XD" , XD_MAX,"WD" , WD_MAX,"WS" , WS_MAX)
    TOTAL_MATCHES = MD_MAX + MS_MAX + XD_MAX+ WD_MAX+ WS_MAX
    print("PLAUSible matches", plausible_total_matches, "||TOTAL matches" , TOTAL_MATCHES)
    if(plausible_total_matches < TOTAL_MATCHES):
        print("NO TIME FOR THE MEET\nPlausible matches based on tpm and meet time:",plausible_total_matches, "\nTotal matches required for meet:", TOTAL_MATCHES)
        return
    df = DataFrame(Meet)#dict -> dataframe obj
    df.to_excel('result.xlsx') #to excel
makeMeet(Meet)
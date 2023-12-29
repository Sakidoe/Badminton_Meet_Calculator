# Badminton_Meet_Calculator
  This is a university badminton meet calculator that creates an interactive .XLSX file from parameters and team rosters inputted by the user, by Richard Huang.
# Instructions
# 1.
  Replace the ucd.xlsx and ucsc.xlsx with the team rosters of the schools, in a format in the form of something like this and rename the files:
  ![image](https://github.com/Sakidoe/Badminton_Meet_Calculator/assets/114327608/a7b267f5-6bc4-4611-94c2-c8b3d9a95b0e)

# 2
  Run app.py through an application such as VSC, after installing python, and the relevant extensions; json, openpyxl, datetime, pandas, random, xlsxwriter.
  You can do this by running pip3 install [extension] in your terminal.

# 3
  The program will begin by asking you basic questions about the meet, namely the team number(which will only work at 2 currently), and team names. It
  will then prompt a menu, for where you can press A to begin adding team rosters. This program is not caps sensitive. 
  ![image](https://github.com/Sakidoe/Badminton_Meet_Calculator/assets/114327608/46fae821-24b0-4c02-894b-48647441f2d9)

# 4
  After adding the rosters, press s to save the rosters in json format in save.txt. Double check that all the players are correct.
  ![image](https://github.com/Sakidoe/Badminton_Meet_Calculator/assets/114327608/310be6c9-818e-4d1f-8ef6-afb3d5167798)

# 5
  Press M to make the meet, and following the prompts to add court numbers, time of event, match duration, and priority courts, it will make a meet schedule
  in json format and produce it in schedule.txt.
  ![image](https://github.com/Sakidoe/Badminton_Meet_Calculator/assets/114327608/8402500d-cd18-439a-9f33-284ad4834d17)

  
# 6
  Press E to export the json formatted schedule into result.xlsx, which will complete your meet!
  ![image](https://github.com/Sakidoe/Badminton_Meet_Calculator/assets/114327608/a10edcfc-3624-4eb1-88cc-9f65bddaf7b2)

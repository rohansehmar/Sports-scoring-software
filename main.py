from prettytable import PrettyTable
import os
from art import *
import time

running=True

valid_name=False

#Individual scores table layout: ID, Name, Score
individual_scores=[[1, "Rohan", 10], [2, "Andy", 3], [3, "Tom", 15], [4, "Jess", 12], [5, "Ally", 12], [6, "Ben", 12], [7, "Carly", 12], [8, "Derek", 6], [9, "Elly", 3], [10, "Frank", 14], [11, "Gabriella", 13], [12, "Harry", 5], [13, "Isabelle", 4], [14, "Justin", 11], [15, "Kelly", 12], [16, "Lucas", 8], [17, "Molly", 2], [18, "Ned", 2], [19, "Oscar", 12], [20, "Perry", 6]]

number_range=(len(individual_scores))


#team scores
team_scores=[[1, "Team 1", 10], [2, "Team 2", 3], [3, "Team 3", 15], [4, "Team 4", 12]]

#Team events
teamEvents=[[1, "Football"], [2, "Basketball"], [3, "Volleyball"], [4, "Netball"], [5, "Dodgeball"]]
#Individual events
individualEvents=[[1, "100m sprint"], [2, "Boxing"], [3, "Karate"], [4, "Cycling"], [5, "Swimming"], [6, "Tennis"]]

#Team mebers
Team1=[[1, "Abdullah"], [2, "Wylbher"], [3, "Jack"], [4, "Tim"], [5, "Sarah"]]
Team2=[[1, "ROOohan"], [2, "Isaac"], [3, "Achmad"], [4, "Justin"], [5, "JAgg"]]
Team3=[[1, "LEVII"], [2, "SUBeen"], [3, "Mary"], [4, "Timmothy"], [5, "Mark"]]
Team4=[[1, "Mariah"], [2, "Louis"], [3, "Joe"], [4, "Kat"], [5, "Elly"]]

#Sorts players by score
individual_scores.sort(key = lambda x: x[2])
individual_scores.reverse()



# Clears the screen 
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
      command = 'cls'
    os.system(command)


def get_individual_scores():
  individual_scores.sort(key = lambda x: x[0])
  f=open("individual_scores.txt", "r")
  readfile=f.readlines()
  for i in range(len(individual_scores)):
    readfile[i] = readfile[i].strip()
    individual_scores[i][2] = readfile[i]
    individual_scores[i][2] = int(individual_scores[i][2])
  f.close()

def get_team_scores():
  team_scores.sort(key = lambda x: x[0])
  f=open("team_scores.txt", "r")
  readfile=f.readlines()
  for i in range(len(team_scores)):
    readfile[i] = readfile[i].strip()
    team_scores[i][2] = readfile[i]
    team_scores[i][2] = int(team_scores[i][2])
  f.close()
  

def record_team_scores():
  global readfile
  team_scores.sort(key = lambda x: x[0])
  f=open("team_scores.txt", "r")
  readfile=f.readlines()
  for i in range(len(team_scores)):
    text=str(team_scores[i][2])
    text=(text + "\n")
    readfile[i]=(text)
  f.close()
  f=open("team_scores.txt", "w")
  f.writelines(readfile)
  f.close()

def record_individual_scores():
  global readfile
  individual_scores.sort(key = lambda x: x[0])
  f=open("individual_scores.txt", "r")
  readfile=f.readlines()
  for i in range(len(individual_scores)):
    text=str(individual_scores[i][2])
    text=(text + "\n")
    readfile[i]=(text)
  #print(readfile)
  f.close()
  f=open("individual_scores.txt", "w")
  f.writelines(readfile)
  f.close()

def make_individual_score_table():
  global individual_score_table
  individual_scores.sort(key = lambda x: x[2])
  individual_scores.reverse()
  individual_score_table=PrettyTable(["Person ID", "Person name", "Score"])
  individual_score_table.title="Individual scores"
  for i in range(len(individual_scores)):
    individual_score_table.add_row([individual_scores[i][0], individual_scores[i][1], individual_scores[i][2]])
    #ONLY GOES UP TO 19


def make_team_score_table():
  team_scores.sort(key = lambda x: x[2])
  team_scores.reverse()
  global team_score_table
  team_score_table=PrettyTable(["Team ID", "Team name", "Score"])
  team_score_table.title="Team scores"
  team_score_table.add_row([team_scores[0][0], team_scores[0][1], team_scores[0][2]])
  team_score_table.add_row([team_scores[1][0], team_scores[1][1], team_scores[1][2]])
  team_score_table.add_row([team_scores[2][0], team_scores[2][1], team_scores[2][2]])
  team_score_table.add_row([team_scores[3][0], team_scores[3][1], team_scores[3][2]])

def make_team_tables():
  #team 1
  global team1Table
  team1Table=PrettyTable(["Person ID", "Person name"])
  team1Table.title = 'Team1'
  team1Table.add_row([Team1[0][0], Team1[0][1]])
  team1Table.add_row([Team1[1][0], Team1[1][1]])
  team1Table.add_row([Team1[2][0], Team1[2][1]])
  team1Table.add_row([Team1[3][0], Team1[3][1]])
  team1Table.add_row([Team1[4][0], Team1[4][1]])

  #team 2
  global team2Table
  team2Table=PrettyTable(["Person ID", "Person name"])
  team2Table.title = 'Team2'
  team2Table.add_row([Team2[0][0], Team2[0][1]])
  team2Table.add_row([Team2[1][0], Team2[1][1]])
  team2Table.add_row([Team2[2][0], Team2[2][1]])
  team2Table.add_row([Team2[3][0], Team2[3][1]])
  team2Table.add_row([Team2[4][0], Team2[4][1]])

  #team 3
  global team3Table
  team3Table=PrettyTable(["Person ID", "Person name"])
  team3Table.title = 'Team3'
  team3Table.add_row([Team3[0][0], Team3[0][1]])
  team3Table.add_row([Team3[1][0], Team3[1][1]])
  team3Table.add_row([Team3[2][0], Team3[2][1]])
  team3Table.add_row([Team3[3][0], Team3[3][1]])
  team3Table.add_row([Team3[4][0], Team3[4][1]])

  #team 4
  global team4Table
  team4Table=PrettyTable(["Person ID", "Person name"])
  team4Table.title = 'Team4'
  team4Table.add_row([Team4[0][0], Team4[0][1]])
  team4Table.add_row([Team4[1][0], Team4[1][1]])
  team4Table.add_row([Team4[2][0], Team4[2][1]])
  team4Table.add_row([Team4[3][0], Team4[3][1]])
  team4Table.add_row([Team4[4][0], Team4[4][1]])

def make_team_event_table():
  global team_event_table
  team_event_table=PrettyTable(["Event number", "Event name"])
  team_event_table.title="Team events"
  team_event_table.add_row(["1", teamEvents[0][1]])
  team_event_table.add_row(["2", teamEvents[1][1]])
  team_event_table.add_row(["3", teamEvents[2][1]])
  team_event_table.add_row(["4", teamEvents[3][1]])
  team_event_table.add_row(["5", teamEvents[4][1]])

def make_individual_event_table():
  global individual_event_table
  individual_event_table=PrettyTable(["Event number", "Event name"])
  individual_event_table.title="Individual events"
  individual_event_table.add_row(["1", individualEvents[0][1]])
  individual_event_table.add_row(["2", individualEvents[1][1]])
  individual_event_table.add_row(["3", individualEvents[2][1]])
  individual_event_table.add_row(["4", individualEvents[3][1]])
  individual_event_table.add_row(["5", individualEvents[4][1]])


def boolean_score_increase_individual(eventID):
  global eventType
  global valid_name
  global competitor1_name
  global competitor1
  global competitor2_name
  global competitor2
  number_range=(len(individual_scores))
  
  clearConsole()      
  for x in range (len(individualEvents)):
    if eventID == (individualEvents[x][0]):
      chosen_event=str(individualEvents[x][1])
      tprint(individualEvents[x][1], font="tarty2")
  
  #NEW SCORE REOCRDER
  print(individual_score_table)
  print("Who competed? (Enter the team ID)")
  competitor1=int(input("Person 1 - "))
  competitor2=int(input("Person 2 - "))
  for i in range(len(individual_scores)):
    if competitor1 == individual_scores[i][0]:
      competitor1_name=individual_scores[i][1]
    elif competitor2 == individual_scores[i][0]:
      competitor2_name=individual_scores[i][1]

  clearConsole()
  tprint(chosen_event, font="tarty2")
  print("-------------------------------------")
  print("=========", competitor1_name, "Vs ", competitor2_name, "=========")
  print("-------------------------------------")
  print("How many points did", competitor1_name, "get?")
  competitor1_score=int(input("-"))
  print("How many points did", competitor2_name, "get?")
  competitor2_score=int(input("-"))
  
  if competitor1_score > competitor2_score:
    winner=competitor1
    print(competitor1_name, "is the winner")
    for i in range (len(individual_scores)):
      if competitor1==individual_scores[i][0]:
        individual_scores[i][2]+=3
  elif competitor1_score < competitor2_score:
    winner=competitor2
    print(competitor2_name, "is the winner")
    for i in range (len(individual_scores)):
      if competitor2==individual_scores[i][0]:
        individual_scores[i][2]+=3 
  else:
    print("It's a draw")
    for i in range (len(team_scores)):
      if competitor1==individual_scores[i][0]:
        individual_scores[i][2]+=1
      elif competitor2==individual_scores[i][0]:
        individual_scores[i][2]+=1
  make_individual_score_table()
  print(individual_score_table)

  

def boolean_score_increase_team(eventID):
  global eventType
  global valid_name
  global competitor1_name
  global competitor2_name
  number_range=(len(individual_scores))

  clearConsole()
  for x in range (len(teamEvents)):
    if eventID == (teamEvents[x][0]):
      chosen_event=str(teamEvents[x][1])
      tprint(teamEvents[x][1], font="tarty2")
  
  #NEW SCORE REOCRDER
  print(team_score_table)
  print("Who competed? (Enter the team ID)")
  competitor1=int(input("Team 1 - "))
  competitor2=int(input("Team 2 - "))
  clearConsole()
  #Finds team name using Team ID
  for i in range(len(team_scores)):
    if competitor1 == team_scores[i][0]:
      competitor1_name=team_scores[i][1]
    elif competitor2 == team_scores[i][0]:
      competitor2_name=team_scores[i][1]
      
  tprint(chosen_event, font="tarty2")
  print("-------------------------------------")
  print("=========", competitor1_name, "Vs ", competitor2_name, "=========")
  print("-------------------------------------")
  print("How many points did", competitor1_name, "get?")
  competitor1_score=int(input("-"))
  print("How many points did", competitor2_name, "get?")
  competitor2_score=int(input("-"))
  
  if competitor1_score > competitor2_score:
    for i in range (len(team_scores)):
      if competitor1==team_scores[i][0]:
        team_scores[i][2]+=3      
    print(competitor1_name, "is the winner")
    
  elif competitor1_score < competitor2_score:
    print(competitor2_name, "is the winner")
    for i in range (len(team_scores)):
      if competitor2==team_scores[i][0]:
        team_scores[i][2]+=3
  else:
    print("It's a draw")
    for i in range (len(team_scores)):
      if competitor1==team_scores[i][0]:
        team_scores[i][2]+=1
      elif competitor2==team_scores[i][0]:
        team_scores[i][2]+=1
  make_team_score_table()
  print(team_score_table)
  



def ranked_score_increase(eventID):
  global number_range
  number_range=(len(individual_scores))
  clearConsole()
  for x in range (len(individualEvents)):
    if eventID == (individualEvents[x][0]):
      tprint(individualEvents[x][1], font="tarty2")
  first_place=int(input("Who came in first place?"))
  second_place=int(input("Who came in second place?"))
  third_place=int(input("Who came in third place?"))
  for i in range (number_range):
    if first_place==individual_scores[i][0]:
      individual_scores[i][2]+=3

    elif second_place==individual_scores[i][0]:
      individual_scores[i][2]+=2
      
    elif third_place==individual_scores[i][0]:
      individual_scores[i][2]+=1
  make_individual_score_table()
  print(individual_score_table)
      
def record_boolean_score(sportname):
  tprint(sportname, font="tarty2")


get_team_scores()
get_individual_scores()
make_team_tables()
make_individual_score_table()
make_team_event_table()
make_individual_event_table()
make_team_score_table()



print("""
          
    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
      
      """)

#print(individual_score_table)

while running==True:

  print("\t  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\t  | Please type the number of the corresponding menu option |\n\t  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
  menu_choice=input("\n\nWould you like to:\n-------------------\n1)View scores\n2)Update scores\n3)Edit info\n4)View team members\n5)View events\n-------------------\n->")
  

  
  #VIEW SCORES
  if menu_choice == "1":
    clearConsole()
    view_choice=input("Would you like to view\n1)Team scores\n2)Individual scores")
    if view_choice == "1":
      clearConsole()
      print(team_score_table)
      
    elif view_choice == "2":  
      print(individual_score_table)
      
    time.sleep(1)
    back=input("Would you like to return to the main menu?")
    if back=="no":
      break
    else:
      clearConsole()
  
  #LOG RESULTS
  elif menu_choice == "2":  
    clearConsole()
    eventType=int(input("Would you like to log the results of a:\n1)Team event\n2)Individual event"))
    
    #Log team event
    if eventType==1:
      clearConsole()
      print(team_event_table)
      event_name=int(input("What event do you want to log the score of?\n(Enter the event ID)"))
      boolean_score_increase_team(event_name)
      time.sleep(1)
      back=input("Would you like to return to the main menu?")
      if back=="no":
        break
      else:
        print(" ")
        clearConsole()
      
    #Individual events
    elif eventType == 2:
      clearConsole()
      print(individual_event_table)
      event_name=int(input("What event do you want to log the score of?\n(Enter the event ID)"))
      
      #Ranked
      if event_name==1 or event_name==4 or event_name==5:
        ranked_score_increase(event_name)
      #Boolean
      elif event_name == 2 or event_name==3:
        boolean_score_increase_individual(event_name)
      else:
        print("Inlvalid ID")
      time.sleep(1)
      back=input("Would you like to return to the main menu?")
      if back=="no":
        break
      else:
        clearConsole()

  
  #EDIT INFO
  elif menu_choice == "3": 
    change=input("What name do you want to change")
    new_name=input("Enter new name")
    if change==individual_scores[0][1]:
      individual_scores[0][1] = new_name
    elif change==individual_scores[1][1]:
      individual_scores[1][1] = new_name
    elif change==individual_scores[2][1]:
      individual_scores[2][1] = new_name
    elif change==individual_scores[3][1]:
      individual_scores[3][1] = new_name
    else:
      print("Invalid name")
  
    make_individual_score_table()
    print(individual_score_table)
    time.sleep(1)
    back=input("Would you like to return to the main menu?")
    if back=="no":
      break
    else:
      clearConsole()
  
  elif menu_choice == "4":
    clearConsole() #calls clear function
    print(team_score_table)
    print(team1Table)
    print(team2Table)
    print(team3Table)
    print(team4Table)
    time.sleep(1)
    back=input("Would you like to return to the main menu?")
    if back=="no":
      break
    else:
      clearConsole()
  
  elif menu_choice == "5":
    clearConsole()
    print(team_event_table)
    print(individual_event_table)
    time.sleep(1)
    back=input("Would you like to return to the main menu?")
    if back=="no":
      break
    else:
      clearConsole()
      



record_individual_scores()
record_team_scores()
""" 
Goal Difference Program
    1. Description:  This program returns the team name with the lowest goal difference (GD) in a league

    2. Pre-condition: input file with format header and goal infomation of 20 soccer teams

    3. Post-condition: the team with lowest goal difference
    Note*: The goal difference could be negative (assumption), so the program finds the team with
    smallest value of (goals_for - goals_against). i.e, the program finds the team that scores the least and loses scores 
    the most
    If the assumption makes the goal difference positive, get the absolute value of (goals_for - goals_against) when computing GD. 
    i.e Replace line 38 with line 39
    This should returns a different team from the first assumption

    4. Return: n/a 
"""

file = open("./../resources/soccer.dat", "r")
lines =  file.readlines()

lowestGoalsDiff= float("inf") # initilized with biggest value
findTeam = None # to find the team with lowest goal difference (GD)
START_LINE  = 3
# read starting from line 4 to second last line
for line in lines[START_LINE: len(lines)-1]:
    line = line.strip() # remove pre and post characters

    if line[-1] == '-': # remove the seperate line (line 21)
        continue

    tokens = line.split('  ') # convert the string into an array
    #tokens now has format:  tokens = [......., 'F', '-', 'A', '' , 'Pts']

    #parse goals_against and goals_for into according variables
    goalsAgainst = int(tokens[-3])  # GA
    goalsFor = int(tokens[-5])      # GF

    goalsDifference = goalsFor - goalsAgainst     
    #goalsDifference = abs(goalsFor - goalsAgainst) 

    #find lowest GD and the team
    if goalsDifference < lowestGoalsDiff:
        lowestGoalsDiff = goalsDifference
        findTeam = tokens[0]
        
#print the team name only without ranking
teamName = findTeam[3:]
print("Team with lowest goal difference: ", teamName)



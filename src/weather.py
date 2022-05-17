""" 
Temperature Difference Program
    1. Description:  This program finds the day with the lowest temperature spread within a month

    2. Pre-condition: input file with format header and temperature infomation of 30 days in a month

    3. Post-condition: the day with lowest temperature difference

    Note*: The tempature difference should always be positive, because maximum temperature should be greater than
    minimum temperature in a day, and the temperature difference formula is:  max_Temperature - min_Temparature

    4. Return: n/a 
"""

file = open("./../resources/w_data.dat", "r")
lines =  file.readlines()

lowestTempDiff= float("inf") # initilized with biggest value

findDay = 0 # to find the day with smallest temperature spread

# read from line 7 to third last line
for line in lines[6: len(lines)-2]: # read from line 7
    line = line.strip() ## remove pre and post characters
    tokens = line.split('   ') # convert the string into a words array

    # tokens with format: tokens =  ['day  maxTemp', ' minTemp', etc...]
    # so only need to use the first two elements
    # parse values into according variables
    day = int(tokens[0].split(' ')[0])
    maxTemp = int(tokens[0].split(' ')[2].split('*')[0])
    minTemp =  int(tokens[1].split('*')[0])

    # temperature spread in a day
    tempDiff = maxTemp - minTemp
    
    # get the smallest spread and the day
    if tempDiff < lowestTempDiff:
        lowestTempDiff =  tempDiff
        findDay = day

print("The day with smallest temperature spread: ", findDay)




import os, sys, math
from sys import argv

# Receives Table Name as parameter
script, sqlServerTxt = argv

# valid DB2 SQL statements
sqlStatements = {
    'INSERT' : ['INSERT INTO ', sqlServerTxt, ' VALUES (', ');'],
    'UPDATE' : ['UPDATE ', 'SET ', '= ', 'WHERE', ');'],
    'DELETE' : ['DELETE FROM ', 'WHERE', ');']
}

# Creating output file (SPUFI)
mySpufi = open('mySpufi.txt', 'w+', encoding='utf-8')

def lineStatement(string):
    if string == '^':
        string = ' '
    if string.find('.') >= 0:
        return string + ','
    newString = '\'' + string + '\','
    return newString


# This function receives an output file as a parameter and reads input file as and object
# Then it will read each line from the input file, split it into an array of strings and
# generate SQL statements inserting each string from this array as a value.
def sqlGen(mySpufi):
    with open(sqlServerTxt + '.txt', encoding = 'utf-8') as queryResult:
        # Writing initial SQL statements:
        for i in range (0, 3):
            mySpufi.write(sqlStatements['INSERT'][i])

        listOfLines = queryResult.readlines()

        for i in range(2, len(listOfLines) - 3):
            counter = 0
            # The reason you need this counter is to keep track of how many
            # lines are being written in a single line due to the fact that
            # z/OS assumes your line's width to be <= 72 characters.

            mySpufi.write('\n  (')

            data = listOfLines[i].split()
            for j in range(0, len(data)):
                mySpufi.write(lineStatement(data[j]))
                counter += len(data[j]) + 2
                if counter > 45:
                    mySpufi.write('\n  ')
                    counter = 0

            mySpufi.write(' CURRENT_TIMESTAMP),')
        mySpufi.close()
    return

def removeLastComma():
    with open('mySpufi.txt', 'rb+') as mySpufi:
        mySpufi.seek(-1, os.SEEK_END)
        mySpufi.truncate()
        mySpufi.close()
    with open('mySpufi.txt', 'a') as mySpufi:
        mySpufi.write('\n' + sqlStatements['INSERT'][3])
        mySpufi.close()
    return

sqlGen(mySpufi)
removeLastComma()

# -*- coding: utf-8 -*-
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

tableKeys = {
    'Table1' : ['BLAUS0', 'BLAUS1', 'BLAUS2', 'BLAUS3', 'BLAUS4']
}



# Creating output file (SPUFI)
mySpufi = open('mySpufi.txt', 'w+', encoding='utf-8-sig')

def lineStatement(*args):
    newString = args[0]
    if newString == '^':
        newString = ' '
    if newString.find('.') == -1:
        newString = '\'' + newString + '\''
    if 'L' not in args:
        newString += ','
    return newString


# This function receives an output file as a parameter and reads input file as and object
# Then it will read each line from the input file, split it into an array of strings and
# generate SQL statements inserting each string from this array as a value.

def insert(*args):
    for i in range (0, 3):
        args[0].write(sqlStatements['INSERT'][i])

        counter = 0
        # The reason you need this counter is to keep track of how many
        # lines are being written in a single line due to the fact that
        # z/OS assumes your line's width to be <= 72 characters.

        args[0].write('\n  (')
        for j in range(0, len(args[2])):
            args[0].write(lineStatement(args[2][j]))
            counter += len(data[j]) + 2
            if counter > 45:
                args[0].write('\n  ')
                counter = 0

        mySpufi.write(' CURRENT_TIMESTAMP),')
    return


def update(*args):
#    key = '_KEY'
#    keys = for any(key in word for word in args[1])
    keys = tableKeys[sqlServerTxt]
    args[0].write(sqlStatements['UPDATE'][0] + sqlServerTxt + '\n' + sqlStatements['UPDATE'][1] + '(\n')
    for i in range(0, len(args[1]) - 2):
        args[0].write('  ' + args[1][i] + ' = ' + lineStatement(args[2][i]) + '\n')
    args[0].write('  ' + args[1][i + 1] + ' = ' + lineStatement(args[2][i + 1], 'L') + '\n')

    args[0].write('  )\n  WHERE (\n  ' +  keys[0] + ' = ' + lineStatement(args[2][0]) + '\n')
    for i in range(1, len(keys) - 1):
        args[0].write('  AND ' + keys[i] + ' = ' + lineStatement(args[2][i]) + '\n')
    args[0].write('  AND ' + keys[i + 1] + ' = ' + lineStatement(args[2][i + 1], 'L') + '\n')
    args[0].write(');\n')

def delete():
    pass

def sqlGen(mySpufi):
    with open(sqlServerTxt + '.txt', encoding = 'utf-8-sig') as queryResult:
    
        listOfLines = queryResult.readlines()
        
        fields = listOfLines[0].split()
        
        options = {
            'A' : insert,
            'C' : update,
            'D' : delete
        }
        for i in range(2, len(listOfLines) - 3):
            data = listOfLines[i].split()
            # Reads ROW_ACTION from line as a key and returns value
            # as a function:
            #print(len(data) - 1); print(data[len(data) - 1])
            rowAction = data[len(data) - 1]
            options[rowAction](mySpufi, fields, data)
        return

sqlGen(mySpufi)

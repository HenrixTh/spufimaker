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
    key = '_KEY'
    keys = for any(key in word for word in args[1])
    args[0].write(sqlStatements['UPDATE'][0] + sqlServerTxt + '\n' + sqlStatements['UPDATE'][1] + '\n')
    for i in range(0, len(args[1] - 1):
        args[0].write(args[1][i] + '=' + lineStatement(args[2][i]) + ',\n')


def sqlGen(mySpufi):
    with open(sqlServerTxt + '.txt', encoding = 'utf-8') as queryResult:

        listOfLines = queryResult.readlines()

        columns = listOfLines[0].split()
        options = {
            'A' : 'insert',
            'C' : 'update',
            'D' : 'delete'
        }
        for i in range(2, len(listOfLines))
            data = listOfLines[i].split
            options[data[len(data) - 1]](mySpufi, columns, data)
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

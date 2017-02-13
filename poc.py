import os, sys
from sys import argv
from os.path import exists

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

# This function receives an output file as a parameter and reads input file as and object
def sqlGen(mySpufi):
    with open(sqlServerTxt + '.txt', encoding = 'utf-8') as queryResult:
        # INSERT INTO sqlServerText VALUES (
        for i in range (0, 3):
            mySpufi.write(sqlStatements['INSERT'][i])

        listOfLines = queryResult.readlines()

        for i in range(2, len(listOfLines) - 3):
            #Handling with my list of strings:
            data = listOfLines[i].split()
            #Writing (
            mySpufi.write('\n    (')

            for j in range(0,int((len(data) - 1)/2)):
                mySpufi.write('\'' + data[j] + '\',')

            mySpufi.write('\n    ')

            for k in range(int((len(data) - 1)/2), len(data) - 1):
                mySpufi.write('\'' + data[k] + '\',')

            # Closing )
            mySpufi.write(' \'' + data[len(data) - 1] + '\'),')
    mySpufi.write('\n' + sqlStatements['INSERT'][3])

sqlGen(mySpufi)
mySpufi.close()

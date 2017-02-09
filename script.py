#  -*- coding: utf-8 -*-


from sys import argv
from os.path import exists

# Recebe txt com o resultado da query como argumento
script, sqlServerTxt = argv


# este dicionario inclui todos os statements necessarios para gerar um SPUFI
sqlStatements = {
    'INSERT' : ['INSERT INTO ', 'VALUES (', ');'],
    'UPDATE' : ['UPDATE ', 'SET ', '= ', 'WHERE', ');'],
    'DELETE' : ['DELETE FROM ', 'WHERE', ');']
}

table5081Fields = [
    'PBE_INSTNCE_ID',
    'PROD_BLNG_ID',
    'BLNG_ELEM_CD',
    'EFFECTDATE',
    'PBE_INSTNCE_NB',
    'PBE_INSTNCE_STRT_DT',
    'PBE_INSTNCE_END_DT',
    'CHRG_FROM_INSTL_DT_ND',
    'BLNG_MTHD_CD',
    'DERV_TYPE_CD',
    'PROD_BLNG_PRD_CD',
    'BIT_RERATE_CD',
    'DERV_ND',
    'PRORATE_ACTN_CD',
    'ZERO_RATE_USG_JRNL_CD',
    'RATING_PROD_BLNG_ID',
    'PRIMARY_CHRG_ND',
    'RATE_MODEL_SET_ID',
    'BUNDLE_ZERO_RATE_IND'
]

# Criando o arquivo de saida (resultado)
mySpufi = open('mySpufi.dat', 'w+')

# Esta funcao recebe o novo arquivo como parametros e le o arquivo de entrada como um objeto
# A cada linha do objeto eu gero uma list contendo varias strings.
def sqlGen(mySpufi):
    with open(sqlServerTxt, encoding = 'utf-8') as queryResult:
        listOfLines = queryResult.readlines()
        for line in listOfLines:
            data = line.split()
            statements = sqlStatements['INSERT']
            for i in range(0, len(statements)):
                statements.insert(1 + i ,data[i])
            statements[0] += sqlServerTxt
            for j in range(0, len(statements)):
                mySpufi.write(statements[j])
            mySpufi.write("\n")

sqlGen(mySpufi)
mySpufi.close()
            # This is were you'll write your data into the new file!



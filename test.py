import main


origem = '\\192.168.41.98\publico\Douglas\TCLE - Unidade NOS'
destino = 'Users\dayvid.silva\Documents'
nameFile = 'teste'


try: 
    origem = '/' + main.convertBackSlash(origem)
    destino = 'C:/' + main.convertBackSlash(destino)
except:
    print('Erro to convert backslash')


#main.copyFile(origem, destino)
main.writeFileBatCopy(nameFile, origem, destino)
main.executeFileCode(nameFile)


'''
try:
    main.copyFile(origem, destino)
except:
    print('Error on copy file')
'''

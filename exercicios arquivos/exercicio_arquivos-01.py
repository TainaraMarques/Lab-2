import sys
import os
def nomes():
    try:
        lista = open("C:\\Users\\Tainara Marques\\Documents\\lab\\exercicios arquivos\\nomes.txt","r")
        for i in range(6):
            print(lista.readline())
            
    except (FileNotFoundError, SystemExit):
        print("Erro!! O arquivo nomes não existe. ")
        sys.exit()
    finally:
        lista.close() 
    
nomes()


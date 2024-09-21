def verificandolista(lista):
    ate100=[]
    ate120=[]
    ate140=[]
    ate160=[]
    ate180=[]
    maior180=[]
    for x in range(len(lista)):
        x = lista[x]
        if x <= 100:
            ate100.append (x)
        elif x > 100 and x <= 120:
            ate120.append (x)
        elif x > 120 and x <= 140:
            ate140.append (x)
        elif x > 140 and x <= 160:
            ate160.append (x)
        elif x > 160 and x <= 180:
            ate180.append (x)
        else:
            maior180.append (x)
    return ate100,ate120,ate140,ate160,ate180,maior180
lista = []
import random
for i in range (10):
    numero = random.randint (90,210)
    lista.append (numero)

a100,a120,a140,a160,a180,m180 = verificandolista(lista)

print (f"""
    Lista:{lista}
    Até 100 ={a100}
    Até 120 ={a120}
    Até 140 ={a140}
    Até 160 ={a160}
    Até 180 ={a180}
    Maior 180 ={m180}
    """)
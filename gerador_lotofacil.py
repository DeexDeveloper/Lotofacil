import random
soma = par = impar = 0
fibonacci = [1,2,3,5,8,13,21]
primo = [2,3,5,7,11,13,17,19,23]
moldura = [1,2,3,4,5,6,10,11,15,16,20,21,22,23,24,25]
#Digite abaixo, entre colchetes, os números sorteados no sorteio anterior.
anterior = [1,3,4,5,6,9,10,13,16,17,18,20,23,24,25]

while impar!=7:
    num=random.sample(range(1,26),15)
    num.sort()
    somamoldura = somaant = somaprimo = fibona = par = impar = soma = 0
    for i in range(1,26):
        if i in num:
            soma+=i
            if i % 2 == 0:
                par+=1
                if i in fibonacci:
                    fibona+=1
                if i in primo:
                    somaprimo+=1
                if i in moldura:
                    somamoldura+=1
                if i in anterior:
                    somaant+=1
            else:
                impar+=1
                if i in fibonacci:
                    fibona+=1
                if i in primo:
                    somaprimo+=1
                if i in moldura:
                    somamoldura+=1
                if i in anterior:
                    somaant+=1
    if soma >= 215 or soma<= 170 or somamoldura >11 or somamoldura< 8 or fibona>6 or fibona<3 or somaprimo>7 or somaprimo<4 or somaant!=10 :
        par = impar = soma = 0    
print(num)
print("Impar e par:",impar,par)
print("Soma:",soma)
print("Primos:",somaprimo)
print("Moldura:",somamoldura)
print("Fibonacci:",fibona)
print("Anterior:",somaant)

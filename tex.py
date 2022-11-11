import numpy as de
def saisir():
    test = False
    while test == False:
        print('donner un entier n')
        n = int(input())
        test = 2 <= n <= 20
    return n
def remplir(t,n):
    for i in range(n):
        test = False
        while test == False:
            t[i] = input("T["+str(i)+"]=")
            test = (11 <= t[i] <= 99) and (t[i] % 10 != 0)

def inser(x,p,t,n):
    for i in range(n,p,-1):
        t[i] = t[i-1]
    t[p] = x
    n += 1

def traiter():
    global T,n
    j = 0
    while (j < n):
        if T[j] % 2 == 0:
            inser(T[j]//2,j+1,T,n)
            j += 2
            n += 1
        else:
            j += 1
def afficher(t,n):
    for i in range(n):
        print(t[i],end="--")
n = saisir()
T = de.array([int()]*40)
remplir(T,n)
afficher(T,n)
print("\n")
print("----------------")
traiter()
afficher(T,n)
print('\n')
print("----------------")

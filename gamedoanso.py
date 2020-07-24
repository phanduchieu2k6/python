from random import randrange
from time import clock

print('-'*20)
print("Game doan so")
x=randrange(0,50)
start=clock()
while True:
    print('Ban con so nao: ',end='')
    n=int(input())
    if n<x:
        print("Low")
    elif n>x:
        print("Height")
    else:
        print("correct")
        break
end=clock()
print("Ban choi trong: ",end-start," giay")

    

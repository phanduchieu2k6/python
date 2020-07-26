def tcc(arr):
    '''duong cheo chinh'''
    s=""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i==j:
                s+=arr[i][j]
    return s
def tcp(arr):
    '''duong cheo phu'''
    s=""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i+j==len(arr)-1:
                s+=arr[i][j]
    return s
def th(arr,k):
    '''tong hang k'''
    s=""
    for j in range(len(arr[k])):
        s+=arr[k][j]
    return s
def tc(arr,k):
    '''tong cot k'''
    s=""
    for i in range(len(arr)):
        s+=arr[i][k]
    return s
def dk(arr):
    '''dieu kien de duoc choi game'''
    ok=False
    if tcc(arr)=="XXX" or tcp(arr)=="XXX" or th(arr,0)=="XXX" or th(arr,1)=="XXX" or th(arr,2)=="XXX" or tc(arr,1)=="XXX" or tc(arr,2)=="XXX" or tc(arr,0)=="XXX":
        ok=True
    elif tcc(arr)=="OOO" or  tcp(arr)=="OOO"or th(arr,1)=="OOO" or th(arr,2)=="OOO" or th(arr,0)=="OOO" or tc(arr,1)=="OOO" or tc(arr,2)=="OOO" or tc(arr,0)=="OOO":
        ok=True
    else:
        pass
    return ok
def choi(arr,k,p):
    '''ham nay de khi nguoi choi nhap so se lam thay doi gia tri '''
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==k:
                if p==1:
                    arr[i][j]='X'
                else:
                    arr[i][j]='O'
    return arr
def w(arr):
    '''ham nay de viet'''
    for i in arr:
        for j in i:
            print("[",j,"]",end='')
        print()
arr=[['1','2','3'],['4','5','6'],['7','8','9']]
ok=False
w(arr)
while ok==False:
    ok=dk(arr)
    if ok==False:
        p1=input("P1: ")
        arr=choi(arr,p1,1)
        w(arr)
    ok=dk(arr)
    if ok==False:
        p2=input("P2: ")
        arr=choi(arr,p2,2)
        w(arr)
print("Cam on ban da choi")
print("-"*20)
het=input()






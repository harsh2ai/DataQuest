N = int(input())
m = 0
def sam(p):
    n=0
    while p!=0:
        p = int(p/10)
        n=n+1
    return n
for s in range(0, N):
    a = int(input())
    x = []
    z = sam(a)
    c=a
    for i in range(0, z):
        x.append(int(c%10))
        c=c/10
    x.reverse()
    end =z-1
    start=0
    while(end>=start):
        if x[start]<x[end]:
            x[end-1]+=1
            x[end]= x[start]
        if x[start]>x[end]:
            x[end]= x[start]
        end-=1
        start+=1
    print(''.join(map(str, x)))

    

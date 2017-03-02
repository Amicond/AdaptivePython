s=input()
a=input()
n=s.find(a)
if n==-1:print('-1')
else:
    while n!=-1:
        print(n,end=' ')
        n=s.find(a,n+1)

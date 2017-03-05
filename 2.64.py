s=input()
cur=s[0]
count=1
for i in s[1:]:
    if i!=cur:
        print(cur,count,end='',sep="")
        cur=i
        count=1
    else:
        count+=1
print(cur,count,sep="")
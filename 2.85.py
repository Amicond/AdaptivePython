s=input().split('.')
if(len(s)!=4):
    print('NO')
else:
    r=0
    for i in s:
        if i.isdigit():
            if (int(i)<256 and int(i)>=0):
                r=r+1
    if r==4:
        print('YES')
    else:
        print('NO')
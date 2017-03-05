s=input().split('_')
s=[i[0].capitalize()+i[1:] for i in s]
print(''.join(s))

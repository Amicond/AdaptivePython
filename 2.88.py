s=input()
print(s.upper() if 97<=ord(s)<=122 and s.islower() else s)
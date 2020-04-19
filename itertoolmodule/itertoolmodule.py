from itertools import combinations_with_replacement
s=input().split()
arr=s[0]
r=int(s[1])
templl=combinations_with_replacement(sorted(arr),r)
for i in templl:
    print(''.join(i))



    
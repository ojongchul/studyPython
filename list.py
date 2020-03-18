a = [1,2,3,4,5]
print (a[0:2])
print (a[1:2])

b = '12345'
print (b[0:2])
print (b[1:2])

c = [2,3,4,5,6]
d = a+c
f = [1,2,3,4,5,2,3,4,5,6]
print (a+c)
print (d)
d.sort()
print (d.sort())
f.sort()
print (f)
f.reverse()
print(f)

del a[2]
print (a)

a.append(3)
print (a)

e = [1,4,3,2]
e.sort()
print (e)

print(a.index(3))
#print (a.index(6))

if (3 in a):
    print ('3 in a')
    print('3 index {index} '.format(index=a.index(3)))
else:
    print ('3 is not in a')

if (6 in a):
    print ('6 in a')
    print(a.index(6))
else:
    print ('6 is not in a')
'''
if a.index(6):
    print ('index 6 is true')
else:
    print ('index 6 is false')
'''



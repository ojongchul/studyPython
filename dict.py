dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print (dic['name'])
dic['addr'] = 'China'
print (dic)
dic[(1,2)] = 3
print (dic)
print (dic[(1,2)])
print (dic.keys())
print (dic.values())
print (dic.items())
#print (dic.clear())

print(dic['name'])
print (dic.get('name'))
print (dic.get('age'))

if dic.get('name'):
    print ('name is ' + dic.get('name'))
if dic.get('age'):
    print ('age is ' + dic.get('age'))
else:
    print ('age is undefined')

print ('name' in dic)
print ('age' in dic)

# key check는 in, 값 가져오기는 get
if 'age' in dic:
    print ('age is ' + dic.get('age'))
else:
    print ('age is undefined')



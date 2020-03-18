# 3 => fizz
# 5 => buzz
# 15 => fizzbuzz
# else => num

for i in range(1,101):
    if(i % 3 == 0 and i % 5 == 0):
        print (str(i) + ' FizzBuzz')
    elif i % 3 == 0:
        print (str(i) + ' Fizz')
    elif i % 5 == 0:
        print (str(i) + ' Buzz')
    else:
        print (i)

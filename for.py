test = ['one', 'two', 'three']
for i in test:
    print (i)

test = [(1,2), (3, 5), (8,13)]
for (first, second) in test:
    print(first * second)

marks = [90, 25,67, 45, 80]
average = 0
count = 0
total = 0
for i in marks:
    count = count + 1
    total += i
    if i >= 60:
        print ("%d번째 학생은"  % count)
    else:
        print ("%d번째 학생은 불합격"  % count)
average =  total / len(marks)
print ("총점 : {total} & 평균 : {average}".format(total=total, average=average))

from collections import namedtuple

#Point = namedtuple('Point', 'x, y')
#pt1 = Point(1, 2)
#pt2 = Point(3, 6)
#print(pt1.x, pt2.x)

Point = namedtuple('Point', 'x, y')
print(Point(*input().split()).y)


'''Car = namedtuple('Car', 'price, model, year')
Tata = Car(6.00, "tiago", 2016)
print(Tata.price)

n = int(input())
print("ID" + " MARKS" + " NAME" + " CLASS")
credentials = []
total = 0
for i in range(n):
    ID, MARKS, CLASS, NAME = map(str, input().split())
    Average = namedtuple('Average', 'ID, MARKS, NAME, CLASS')
    Average.ID = ID
    Average.MARKS = int(MARKS)
    Average.CLASS = CLASS
    Average.NAME = NAME
    credentials.append(Average.MARKS)

for j in credentials:
    total += j
print(format(float(total/n), '.2f'))

from collections import namedtuple

N = int(input())
student = namedtuple('student', input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N)) / N)

n = int(input())
student = namedtuple('student', input().split())
Total_marks = []
Total_marks_count = 0
for i in range(n):
    stud_credentials = student(*input().strip().split()).MARKS
    Total_marks.append(stud_credentials)
for k in Total_marks:
    Total_marks_count += int(k)
print(Total_marks_count/n)



for j in Total_marks:
    Total_marks_count += int(j)
print(format(Total_marks_count, '%.2f'))'''


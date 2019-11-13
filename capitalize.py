# Complete the solve function below.
import os

s = input()
def solve(s):
    s = s.split(" ")
    new = []
    for i in s:
        new.append(i.capitalize())
    new = " ".join(new)
    return new

print(solve(s))






'''if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()'''

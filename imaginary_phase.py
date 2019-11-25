'''from cmath import phase
from math import sqrt
z = input()
x, y = complex(z).real, complex(z).imag
print(sqrt((x**2)+(y**2)))
print(phase(complex(x, y)))

import cmath
z = complex(input())
pol_cord = list(cmath.polar(z))
for i in pol_cord:
    print(i)'''
import cmath
print(*cmath.polar(complex(input())), sep='\n')
















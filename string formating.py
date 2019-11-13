'''n = int(input())
width = len("{0:b}".format(n))
for i in range(1, n + 1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))'''

# print("{1} {0}".format('one', 'two'))
"""class Data(object):
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


print("{0!s} {0!r}".format(Data()))"""

# print('{0:>10}'.format('test'))

'''def print_formatted(num):
    form = "{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}"
    for n in range(1, num + 1):
        print(form.format(n, w=num.bit_length()))

print('{:{w}d}'.format(42, w=4))'''

n = int(input())
for i in range(1, n+1):
    print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i, w=n.bit_length()))

from collections import *
from random import *

sendr = open(input("Which file would you like me to print? "))
dump_list = sendr.read().split()
print(dump_list)

d = defaultdict(list)
print(f'Length:{len(dump_list)}')
for i in range(len(dump_list)):
    d[dump_list[i-1]].append(dump_list[i])
    #print(f'Index:{i}')
print(d.items())

print("Now I will attempt to write a predictive text based on a markov chain prediction:")

seed = list(d.keys())[randrange(0, len(d.keys()), 1)]
print(type(seed))
print(seed,'\t')

next = d[seed]
for j in range(100):
    print(str(next),end=' ')
    #print(d[str(next)])
    #print(list(d[str(next)])[randrange(0, len(d[next]), 1)])

    try:
        next = (list(d[str(next)])[randrange(0, len(d[str(next)]), 1)])
    except ValueError:
        next = 'The'

    if j%25 == 0:
        print()

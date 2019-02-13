#/bin/python3
from random import randint
from os import system
lines = []
fname = 'nums.txt'
#for i in range(10**6):
#    lines.append(randint(0,10**10))
#nums = [str(randint(0,10**10))for i in range(10**6)]
#for i in nums: print(i)
with open(fname, 'w') as f:
    for i in range(10**6):
        x = str(randint(0,10**20)) + '\n'
        print(i, x)
        f.write(x)
cmd = 'cp ./' + fname + ' ./' +fname + '.bak'
system(cmd)

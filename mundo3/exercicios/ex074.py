from random import randint
nrs = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(nrs)
nrs = sorted(nrs)
print(f'{nrs[0]} - {nrs[4]}')
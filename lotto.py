import random

lottonums = set()

while len(lottonums) < 6:
    n = random.randint(1, 50)
    lottonums.add(n)
print(lottonums)

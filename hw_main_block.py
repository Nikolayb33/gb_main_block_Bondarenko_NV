import random

old_massive = ['Hello', '2', 'world', ':-)']
random.shuffle(old_massive)
# print(old_massive)
a = random.randint(0, 3)
# print(a)
new_massive = []
if a > 0:
    while a != 0:
        new_massive.append(old_massive.pop())
        a -= 1
        
print(new_massive)
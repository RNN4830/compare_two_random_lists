
import random
randomlist1 = [random.randint(1,50)for x in range(10)]
print(randomlist1)
randomlist2 = [random.randint(1,100) for y in range(15)]
print(randomlist2)
combolist = [a for a in randomlist1 if a in randomlist2]
print(combolist)
#The long way
# randomlist1 = []
# randomlist2 = []
# combolist = []
# for x in range(0,10):
#     x=random.randint(1,50)
#     randomlist1.append(x)
# for y in range(0,15):
#     y=random.randint(1,100)
#     randomlist2.append(y)
# print(randomlist1)
# print(randomlist2)
# for a in randomlist1:
#     if a in randomlist2:
#         combolist.append(a)
# print(combolist)
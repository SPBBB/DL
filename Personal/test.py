# a = "   c cc  c   c a "
# print(a.strip("a            "))
# print(type(" "))

# a = "   c cc  c   c a "
# print(a[:-4])

import random as r


def experi_randint(ran) :

    counter = [] 

    for i in ran : 
        counter.append(0)

    for i in range(10000) : 
        a = r.randint(ran[0],ran[-1])
        for j in ran : 
            if a == j : 
                counter[j] += 1

    print("range: [{0},{1}]".format(ran[0],ran[-1]))
    print("result:",counter)
    return counter

experi_randint(range(7))
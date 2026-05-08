# Dictionary 

# A = [1,2,3,4,5]
# for i in A[:-1] : 
#     print(i)
# for i in A[:-2] : 
#     print(i)
# > 1 2 3 4 1 2 3  (negaive number ordering)

# cards = list()
# cards.append(21)
# cards.append(3)
# cards.append(75)
# print(cards)
# print(cards[1])
# cards[1] = cards[1] + 2
# print(cards)

# cabinet = dict()
# cabinet[0] = 21 
# cabinet[1] = 3
# cabinet[2] = 75
# print(cabinet)
# print(cabinet[1])
# cabinet[1] = cabinet[1] + 2 
# print(cabinet)

# def abcd(a,b,c,d) : 
#     print(a,b,c,d)
#     return None 

# abcd(d=1,a=3,c=34,b=-34) Q. does this line make error? > Nope!

# dict().get(key,default)
# dict().update(dict())
# dict().pop(key) > return the value of the argumented key
# c,b = dict().popitem()


"""
ooo = {}
>>> ooo
{}
>>> type(ooo)
<class 'dict'>
"""

"""
>>> jjj = {'chunk' : 1, 'ff' : " faf", 123 : '2er'}
>>> jjj
{'chunk': 1, 'ff': ' faf', 123: '2er'}
>>> ooo = {}
>>> ooo
{}
>>> type(ooo)
<class 'dict'>
>>> dic = {x : x*x for x in range(6) if x%2 == 0 }
>>> dic
{0: 0, 2: 4, 4: 16}
>>> x = {'a':1}
>>> x['b'] = 2
>>> x
{'a': 1, 'b': 2}
>>> x['a']=9
>>> x
{'a': 9, 'b': 2}
>>> x.update(jjj)
>>> x
{'a': 9, 'b': 2, 'chunk': 1, 'ff': ' faf', 123: '2er'}
>>> val = x.pop('b)
  File "<stdin>", line 1
    val = x.pop('b)
                ^
SyntaxError: unterminated string literal (detected at line 1)
>>> val = x.pop('b')
>>> val
2
>>> x
{'a': 9, 'chunk': 1, 'ff': ' faf', 123: '2er'}
>>> k,v= x. popitem()
>>> k
123
>>> v
'2er'
>>> k
123
>>> del x['a']     
>>> x
{'chunk': 1, 'ff': ' faf'}
>>> x.claer()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'claer'. Did you mean: 'clear'?
>>> x.clear
<built-in method clear of dict object at 0x000001EA9BA4BC40>
>>> x.clear()
>>> x
{}
"""
# dict().popitem() 맨뒤? 팝하고 return key, value

# split word and count 
counts = dict()
print('Enter a line of text:')
line = input('') # the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car 
words = line.split()
print('Words:', words)

print('Counting...')
for word in words : 
    counts[word] = counts.get(word,0) + 1 
print('Counts', counts)

# data structure
# print([])
# x = list((1,2,1,3,1,4,5)) # 튜플을 리스트로 만들어
# print(x)
# # print(x[-6]) <- error

# list_1 = [0.01*x for x in range(1,1001)]
# print(list_1)

# #append(item)
# # insert(index, item)
# # remove(item)
# # pop(index)
# # clear() -all

# x.remove(1)
# print(x)

# x.remove(1)
# print(x)

# x.remove(1)
# print(x)

# a= [1,2,3]
# b = a*3
# print(b)

# lab.1

## 1 [Sum of input integers]
"""
# input and split str into list of flural str 
a = input('Enter a single line of integers: ')
b = a.split(',')

# preprocees the list and spontaneously find the sum 
sum = 0
for i in b : 
    sum += int(i.strip())
print('sum is',sum)
"""


## 2  [Energy Meter CSV (sum per house)]


# input CSV file and split pairs 
"""
CSV = input('Enter one-line CSV file: ')
house_value = CSV.split(';') # ['house,value', 'house,values' , . .]

# print(CSV)
# print(house_value)

# strip list
list = []
for i in house_value : 
    house_value_strip = i.split(',') # [house, value]
    house_value_strip[0] = house_value_strip[0].strip()
    house_value_strip[1] = house_value_strip[1].strip()
    list.append(house_value_strip) # list = [ [house, value] , [house,value] , . .]

# change type of values from str to float
for i in range(len(list)) : 
    list[i][1] = float(list[i][1])
# print("list: {}".format(list))

# make two list to save house_id and its total kWh seprately
label_list = []
value_list = []
for i in range(len(list)) : 
    if list[i][0] in label_list : 
        continue
    label_list.append(list[i][0])
    total_value = 0
    for j in range(len(list)) : 
        if list[i][0] == list[j][0] : 
            total_value += list[j][1]
    value_list.append(total_value)

# make a output from lists
finalText = ""
for i in range(len(label_list)) :
    finalText += f"{label_list[i]}:{value_list[i]}, "
finalText = finalText[:-2]
# print(label_list)
print(finalText)

"""

## 3. [Random movie recommendation] 
"""
# input movies by one-line str and make it movies' list
movies = input("Enter movie list: ").split(',')
movie_list = []
for i in movies :
    movie_list.append(i.strip())

# selenct random movie and print it
import random 
randint = random.randint(0, len(movie_list)-1)
print("Movie recommendation:",movie_list[randint])
"""

## 4. [Find the Second Largest Number]
"""
# define a funtion that find second max from integer list and print, retrun it.
def find_second_max(num_list) : 
    num_list.remove(max(num_list))
    print("Second max =", max(num_list))
    return max(num_list)

# input str and make it a list of integers
integers = input("Enter a single line of integers: ").split(',')
integer_list = [int(x.strip()) for x in integers]
find_second_max(integer_list)
"""

## 5. [Matrix Transpose] 혹시 이거 인풋을 one-line input()으로 받아야 하나요 
"""
Origin_matrix = [[1,2,3],[4,5,6],[7,8,9]]

# assign the size of Transposed matrix
Transposed_matrix = [ [0 for j in range(len(Origin_matrix))] for i in range(len(Origin_matrix[0])) ] #  TypeError: 'int' object is not subscriptable > len(Origin_matrix)[0] 

# make Tran. maxtrix
for i in range(len(Origin_matrix)) : 
    for j in range(len(Origin_matrix[i])) : 
        Transposed_matrix[j][i] = Origin_matrix[i][j] # the defintion of transpose 

# print result
input("Original matrix = ")
print("Transposed matrix =",Transposed_matrix)
"""

##6. [Data Cleaning: Filter Invalid Temperature Values] 
"""
# input data
data_list = input("Enter a single line of temp. measurement: ").split(',')

# a function cofirming whether string can be converted to float
def CanBeConverted_str_To_float(string) : 
    try :
        fl = float(string.strip())
        return True
    except : 
        return False 

# make before cleaning list (not strip)
before_clean = []
for i in range(len(data_list)) :
    if CanBeConverted_str_To_float(data_list[i]) : 
        before_clean.append(data_list[i])
    else : 
        if data_list[i].strip() == 'None' : before_clean.append(data_list[i])
        else : before_clean.append('"abc"')

# make After cleaning list
After_clean = []
for i in before_clean : 
    if CanBeConverted_str_To_float(i) : 
        num = float(i.strip())
        if 30.0 < num < 45.0 : 
            After_clean.append(num)

# print result
print("Before cleaning:", before_clean)
print("After cleaning:", After_clean)
"""
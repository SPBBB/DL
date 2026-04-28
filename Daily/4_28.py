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
"""
# 1 
a = input('Enter a single line of integers: ').strip()
b = a.split(',')
sum = 0
for i in b : 
    sum += int(i)
print('sum is',sum)

"""

# 2 

"""

CSV = input('Enter one-line CSV file: ').strip()
house_value = CSV.split(';')
list = []
# print(CSV)
# print(house_value)
for i in house_value : 
    house_value_strip = i.split(',')
    house_value_strip[0] = house_value_strip[0].strip()
    house_value_strip[1] = house_value_strip[1].strip()
    list.append(house_value_strip) # [ [house, value] , [house,value] , ]
for i in range(len(list)) : 
    list[i][1] = float(list[i][1])
# print("list: {}".format(list))
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

finalText = ""
for i in range(len(label_list)) :
    finalText += f"{label_list[i]}:{value_list[i]}, "
finalText = finalText[:-2]
# print(label_list)
print(finalText)

"""

#3.

#4.

#5.

#6.
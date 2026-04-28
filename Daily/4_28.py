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

# 1 
a = input('Enter a single line of integers: ').strip
b = a.split(',')
sum = 0
for i in b : 
    sum += int(i)
print('sum is',sum)


# 2
CSV = input('Enter one-line CSV file: ').strip()
house_value = CSV.split(';')
list = []
for i in house_value : 
    list.append(i.split(',')) # [ [house, value] , [house,value] , ]
for i in list : 
    for j in (0,len(list)) : 
        i[0] = list[j][0]
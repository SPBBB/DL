# 5;Loops and iterations

# # while
# while True: 
#     line = input('> ')
#     if line == 'done' : 
#         break
#     print(line)
# print('Done!')

# # continue
# while True:
#     line = input('> ')
#     if line == '':
#         continue
#     if line[0] == '#':
#         continue
#     if line == 'done': 
#         break
#     print(line)
# print('Done!')
""" 공백문자 성질, str 어트리뷰트 """

### Lab 1

# # 1. 
# i = 1
# while i < 6 : 
#     print(i)
#     i = i + 1

# # 2. 
# while True : 
#     password = input("Enter your password: ")
#     if password == "robot123" : 
#         print("Access Granted!")
#         break
#     else:
#         print("Wrong Password!")
        
# # 3. 
import random 
target = random.randint(1,10) # 1~10 random

try_number = 0 
while True:
    
    try_number += 1
    if try_number == 6 : 
        print('opportunity gone..')
        break
        
    try : 
        guess = float(input('guess what number is selected: '))
    except : 
        print('input a number please')
        continue
    
    if guess == target : 
        print('You got it!')
        break
    if guess < target : 
        print('Too low!')
    if guess > target : 
        print('Too High!')
    
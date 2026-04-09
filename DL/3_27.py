# 3_24 내용 연장(operator)

# Identity op. 시메틱 에러(의미상 오류) / 그래머틱 오류
# 불값, None는 싱글톤이라 id비교(is) 추천 (== not recommended)

# Membership op.

# L = [1,2,3]
# # FTTF
# print(5 in L)
# print(5 not in L)
# print(3 in L)
# print(3 not in L)

# T = "Membership operators"
# # TTFT
# print("embership" in T)
# print("member" in T)
# print("Member" in T)
# print("ship op" in T)

## lab.3
# 1.
# a=[1,2,3]
# b=[1,2,3]
# c=a

# print(a==b) # 넹
# print(a is b)  # 넹(아니었다)
# print(a is c) # 넹

# print(id(a))
# print(id(b))

# 2.
# sentence = input("Enter a sentence: ")
# print("does cantain 'AI'?", "AI" in sentence )


## Conditional
# x = 1
# if x == True : 
#     print("x = True")
# if x is True : 
#     print("x is True")
# if not True is False : 
#     print("not True is False")
# if not True == False : 
#     print("not True = False")
# print(id(None))
# print(id(0))
# print(type(None))

# indent(ation) (조건문 구분 - 여백 하는 거 말함)

## try - except
# rawstr = input("Enter a national number: ")
# try : 
#     ival = int(rawstr)
# except :
#     ival = -1 

# if ival > 0 : 
#     print('Nice work')
# else:
#     print('Not a national')

# Lab 1.

# 1. & 2.
# try : 
#     integer = int(input("Enter a integer value: "))
#     remainder = integer % 2
# # if remainder == 0 : 
# #     print("even")
# # else : 
# #     print("odd")

# # print("even" if remainder == 0 else "odd")
#     parity = "even" if remainder == 0 else "odd"
#     print(parity)
# except:
#     print("Input is not a integer!")

# 3. 
# password = "!admin123"
# if password is "!admin123" : 
#     print("Access Granted") # offered
# else :
#     print("Access Denied")
    
# if password in "!admin123" : 
#     print("Access Granted") # offered
# else :
#     print("Access Denied")
    
# 4. 
# score = int(input("Enter your score: "))
# if score >= 90 : 
#     print("Excellent!")
# elif score >= 70 : 
#     print("Good")
# elif score >= 50 : 
#     print("Pass")
# else:
#     print("Fail")

# 5.
ID = "IamAdmin"
PW = "!admin123"


input_id = input("Enter your ID: ")
input_pw = input("Enter your pasword: ")

corr_id = (input_id == ID)
corr_pw = (input_pw == PW)

if corr_id and corr_pw : print("Access okay")
if not corr_id and corr_pw : print("ID issue")
if corr_id and not corr_pw : print("password issue")
if not corr_id and not corr_pw : print("denied.")

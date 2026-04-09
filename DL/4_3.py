# lsf=-1
# print('Before',lsf)
# for the_num in [54,34,2463,245,34,7] :
#     if the_num > lsf:
#         lsf=the_num
#     print(lsf,the_num)
# print('After',lsf)

# lab 2. 
N = int(input("Enter any poitive integer:"))
N_sum = 0
N_list = range(N+1)

for  i in N_list : 
    N_sum += i
print("Sum of 1 to",N,"is",N_sum)

N_sum_divisible_by_three = 0 
for i in N_list:
    if i % 3 == 0:
        N_sum_divisible_by_three += i
print("Sum of the all positive multiplies of three from 1 to",N,"is",N_sum_divisible_by_three)

for i in range(9) :
    print(N,"*",i+1,"=",N*(i+1))
    
for i in range(0,N) : 
    print("*"*(i+1))
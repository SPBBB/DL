# function
"""
3
5
5
print('efr')
577757575
# return None == void ? 

def greet(name, message="Hello!") : 
    print(f"{name}, {message}") 
    return None 

greet("Alice")
greet(369,"Hi!")

a = greet(435)
print(a)

def greet1(name, message="Hello!") : 
    print(f"{name}, {message}") 

b = greet1(324)
print(b) # no comment about return equals to setting return None

# default vaules & 명시!!! 
greet(name="Alphs")
greet("Kim",message=1234) # type of default value and arg is not neccessary to be equal.  

def greet2(name, game, message="Hello!") : 
    print(f"{name}, {game}, {message}") 
    return None 

greet2("kim",message="higg",game="retr")
"""
# arg 개수 유동적이게 하기 *args < tuple
"""
def add_numbers(*args) :
    print(args)
    added = 0 
    for i in args : 
        added += i
    return added

x = add_numbers(3)
y = add_numbers(5,6,2)
z = add_numbers(10,3,3,3,3)
print(x,y,z)
"""
# **kwargs < dictinonary
## 용어 : fruitful < a funtinon is fruitful if it has a return that is not None(if it has a result) (?)
# modify global variable in function : set the variable with the keyword type 'global' 
"""function
reusablity
readabiity
maintainablity
abstraction 
. . . 
one func. to one well-defined work .
"""

## lab 1. Function 
# 1. 

def is_even(n) : # if n is even reutrn True and is not return False. 
    if n % 2 == 0 : 
        return True 
    else : return False 

while True : # repeatedely input integer and test it whether it is even
    input_data = input("Enter any integer number: ")
    if input_data == "quit" : 
        break
    int_num = int(input_data)
    print("Is the input value even?", is_even(int_num))

# 2. 
def greet(name) :
    print("Hello, {Name}!".format(Name=name)) 
# Q. How would you make name optional and default to “Student”
# A: def greet(name="student") : ..
while True :
    name = input("Enter any name: ")
    if name == "" : 
        break # no input makes break
    greet(name)

# 3. 

# Enter datas 
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
operator = input("Enter operation (+ or *): ")

if operator == "+" : 
    print("Sum:",first_num+second_num)
if operator == "*" : 
    print("Product:", first_num*second_num)

# does a function makes code more nice?
def binary_operation(num1,num2,operator) : 
    None
    
# 4. 

# define converting funtion 
def celsius_to_fahrenheit(c):
    return (1.8*c + 32)
def fahrenheit_to_celsius(f):
    return (f-32)/(1.8)

# set a repeated menu
while True : 
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Exit")
    choice = input("Select a menu: ")
    
    if choice == "1" : 
        temp_c = float(input("Enter Celsius temperature: "))
        temp_f = celsius_to_fahrenheit(temp_c)
        print(f"Fahrenheit = {temp_f}")
    if choice == "2" : 
        temp_f = float(input("Enter Fahrenheit temperature: "))
        temp_c = fahrenheit_to_celsius(temp_f)
        print(f"Celsius = {temp_c}")
    if choice == "3" : 
        print("Program terminated")
        break  
# Standard I/O
# number = input("number: ")
# print(number)

"""
# print 잘 쓰는 법
# 1. , 써서 프린트
# print("Name:", "Alice", "Age:", 20)

# 2. % 써서 프린트 %he'x'a 16진법 %octave
print("Name: %s, Age: %s"%("Alice",20))
x=5.945
y=2
print("%d"%(x)) # %d는 내림 
print("%o, %x, %.2f"%(31,15,x)) # .(n)f는 반올림

# 3. 포맷
print("Yellow is similar to {}, {}".format("orange",12321))
print("Yellow is similar to {na}, {n}".format(na="orange",n=123))

# 4. f-string
print(f"I want to show {x}+{y}={x+y}")

# DLF02 lab 5,6 하기
"""
"""-------------------------------------------------------------------------"""

import math as m 

# print(m.sqrt(2)**m.sqrt(2))

# lab 1.numeric operators
seconds = float(input("Enter total seconds: "))
seconds = f"{seconds:.0f}"
seconds = int(seconds)

print(f"{seconds//3600:02.0f}:{seconds%3600//60:02.0f}:{(seconds%3600)%60:02.0f}")

solar_panel_area = float(input("solar panel area: "))
efficiency_rate = float(input("efficiency: "))/100
sunlight = float(input("sunlight: "))
hours = float(input("hours: "))
print("total generated energy={}".format(solar_panel_area*efficiency_rate*sunlight*hours/1000))

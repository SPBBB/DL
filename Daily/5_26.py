class Person : 
    def __init__(b,name,age,sex,height,weight) : 
        b.name = name
        b.age = age 
        b.sex = sex
        b.heigtg = height
        b.weight = weight
    
    def greet(a): 
        print(f"Hello, my name is {a.name} and I am {a.age} years old.\nYou look me as {a.heigtg}? I want to be {a.weight-4} kg..")
        
    def __del__(self) : 
        print("Bye.")

P1 = Person("Min",20,"man",170,70)
P1.greet()
print(P1.name)
print(dir(Person))
print(dir(P1))

P1 = 123456
print(dir(P1))

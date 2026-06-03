## class and object
#  Class atribute vs Instance attr. 
"""
class Person : 
    species = "Human" # Class atribute 
    
    def __init__(self,name,age=20,sex="man",height=170,weight=70) : 
        #Instance attr.
        self.name = name 
        self.age = age 
        self.__sex = sex # private attr.
        self.heigtg = height
        self.weight = weight
    
    def greet(a): 
        print(f"Hello, my name is {a.name} and I am {a.age} years old.\nYou look me as {a.heigtg}? I want to be {a.weight-4} kg..")
        print(a.__sex)
    
    def __print_real(self) :  # private function -> Mangling(이름 바꾸기): the real name is _<Class>__print_real() ( print dir(Person) ) 
        print(self.__sex)
        
    def __del__(self) : 
        print(self.name,"Bye.")


P1 = Person("Min")
P2 = Person("Kim")
print(P1.name)
print(P2.age)
print(P1.species, P2.species) # class attr.이 진짜 같은지 타ㅇㅍ
print("adsa") # del이 언제 발동? -> 프로그램(코드진행) 끝나기 직전 | 오브젝트마다 순서는? -> 아마 생성된 순인듯? 
P1.greet()
# P1.__print_real() # no attr __print_real
P1._Person__print_real() # wow private system was destroyed
P1Name = P1.name # getter를 안쓰고 바로 접근하면 뭐가 안좋을까 -> 혹시 c# 인스턴시에잇마냥 attr. 수정이 변수에 바로 반영되나?
print(P1Name)
P1.name = "Pin"
print(P1Name) # Min -> 일단 그건 아닌듯 
print(dir(Person))
"""

## Inheritance
"""
class Person() :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self) :
        print(f"My name is {self.name}, and I am {self.age} years old.")

class Student(Person) :
    def __init__(self, name, age, major) :
        self.name = name
        self.age = age
        self.major = major
        
    def set_major(self, new_major):
        print("Old Major:", self.major)
        self.major = new_major
        print("New major:", self.major)
        
S1 = Student("Min", 20, "En")    
S1.introduce()
S1.set_major("DL")
"""
# initializer is not heritage
# child class must not need to have instance attr. of parents but just inheritance method use <object>.<attr.> variable(name).  
# >> use super().__init__(name,age) when self. ... lines are too long to rewrite in child class. 

"""
class Person() :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self) :
        print(f"My name is {self.name}, and I am {self.age} years old.")

class Student(Person) :
    def __init__(self, name, age, major) :
        super().__init__(name,age)
        self.major = major
        
    def introduce(self) :  # not overriding, just new define > how can we recall parents' functions that have same name with child's?
        super().introduce()
        print(f"And I study {self.major}.")
        
    def set_major(self, new_major):
        print("Old Major:", self.major)
        self.major = new_major
        print("New major:", self.major)
        
    # special methods
    
    def __str__(self):
        return f"Student(name:{self.name}, major:{self.major})"
    
    def __eq__(self,other):
        return self.name == other.name 
    
    # def __

# test methods  
S1 = Student("Min", 20, "En")    
S1.introduce()
S1.set_major("DL")
print(S1)
S2 = Student("Min", 21, "DL")
print(S1==S2)
"""

# PDB
import pdb
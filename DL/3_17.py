# # 3
# name = "Alice" 
# age = 20 
# print(name + " is",age,"years old")

# #4 
# a=10
# b=10
# print("a= ", a, "id: ", id(a))
# print("b= ", b, "id: ", id(b   ))

# c=400
# d=400
# print("c= ", c, "id: ", id(c))
# print("d= ", d, "id: ", id(d))
# A.q : 인터랙티브로 하면 c,d의 id가 다름 그러게 왜일까 
# # >> 코파일럿한테 물어봤는데 정수 캐싱이라는 매크로 > -4~256까지 객체 저장 후 불러옴이 있고 그 밖의 수는 새로 만드는데, 스크립트 모드는 컴파일러 최적화로 동기화가 되고 인터랙티브는 한줄한줄이라 안된대

# 5
# x=765
# print("Before: ", id(x))
# x=766
# print("After: ", id(x))
# q : 변함

#6
m="Hello"
n=m
print("m= ",m,"id: ", id(m))
print("n= ",n,"id: ", id(n))
# q : 그런듯 ?  + 얘네는 인터랙티브로 해봐도 같음 

#7
p = 3.14
q = "3.14"
print("p=",p,"id:", id(p))
print("q=",q,"id:", id(q))
# q: 데이터타입이달라서



a=-6
b=-6
print("a= ", a, "id: ", id(a))
print("b= ", b, "id: ", id(b   ))
 
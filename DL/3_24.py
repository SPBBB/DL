# A = (True, 1, 0 , False)
# print(A)
# print(True)
# print(True+True)
# A = (2, True+True)
# print(A) <- (2,2) 불리안타입을 누메릭처럼 연산하면 숫자로 바뀜을 확인함

# 비교연산자 comparison op.
# 실수 에서 양수 음수 판정 

# num = float(input("enter the number: "))
# if 2**num == 1 : 
#     print("the number=0")
# elif 2**num < 1 : 
#     print("the number is neg.")
# elif 2**num > 1 : 
#     print("the number is pos.")

# 논리연산자 logical op.

# username = "admin"
# password = "1234"
# if username == "admin" and password=='1234': 
#     print("Login allowed")
# else:
#     print("Please log in first")
# #  negation
# is_login = False
# if not is_login :
#     print("Please Log in first")
    
# Assignment op.

#  Bitwise op. 
WIFI = 0b0001
BLUETOOTH = 0b0010
GPS = 0b0100
CAMERA = 0b1000
# 0b | 0b < 각 비트마다 or 연산 
config = WIFI | GPS
print("Initial config:", bin(config)) ## Initial config: 0b101

config |= BLUETOOTH # config = config | BLUETOOTH
print("After enabling Bluetooth:",bin(config))

print("GPS enabled?:",bool(config & GPS))

# 0b & 0b < 각 비트마다 and 연산
config &= ~WIFI # config = config & !WIFI
print("After disabling Wi-fi:",bin(config))

# ~0b < 0,1 반전
print(bin(~WIFI)) #-0b10
print(~WIFI) # -2 .. < 왜이러지Q.
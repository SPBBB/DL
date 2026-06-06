"""
this program makes a One-Time Password, which has <OTPdigits> digits.
OTPdigits, populations and populations_mustincluded are may be input data
if I use it.
모듈로 만들면 각각 int, string 데이터 스트럭쳐, ditctionary로 받으면 기모찌할 듯 
"""
import random 

OTPdigits = 8

# populations 
numbers = "0123456789"
Lchars = "abcdefghijklmnopqrstuvwxyz" 
Uchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# make must included digits 
populations_mustincluded = { numbers : 1, Lchars : 1, Uchars : 1 }

# I don't know whether we set keys to strings of variables' name
mustincluded = []
for item in populations_mustincluded.items():
    OTPdigits -= item[1]
    for element in random.sample(item[0],item[1]):
        mustincluded.append(element)

# substitute
OTP = mustincluded

# take remainders
universal_set = numbers + Lchars + Uchars
for taken in random.sample(universal_set,OTPdigits): 
    OTP.append(taken)

random.shuffle(OTP) # shuffle order

OTP_str = "".join(OTP) # OTP is a list of the password charcters
print(OTP_str)


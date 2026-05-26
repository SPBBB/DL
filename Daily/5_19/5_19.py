# 아 숙제 해야되는데 안했다 
# Strings and files 

## lab1.
# 1.
"""
while True : 
    pw = input("Enter a new password (letters and digits only): ")
    if pw.isalnum() : 
        print("Password accepted.")
        break
    else: print("Use only letters and digits. Try again.")
    """
# 2. 
"""
letters = input("Enter a phrase: ").strip()
acronym = ""
for i in letters.split() : 
    acronym += i[0].upper()
print(acronym)
"""

# File 
# close < 를 안하면 다른 프로그램에서 그 file 못 열음

fhand = open('data.txt', 'r')
Content = fhand.read()
fhand.close()
#  close 괄호 빼도 ㄱㅊ은듯
stuff = 'Hello\nWorld!'
# print(stuff)

"""
4가지 open, read의차이 
1. \n을 포함한 띄어쓰기 없는 글 
2. list임 
3. 메모장에 쓰인대로 나옴 <= print(line, end="") 로 수정 가능 
4. \n 처리가 됐는데 print가 한칸 띄우기도 해서 줄바꿈 2번 됌
"""

## Lab2. 

# 1.

# 2. 

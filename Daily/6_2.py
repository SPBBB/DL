# Library

"""
import matplotlib.pyplot as plt 

X = ["Mon","Tue","Wed","Thr","Fri","Sat","Sun"]
# Y1 = [1,2,3,4,5,6,7]
Y1 = range(1,8)
print(Y1)
Y2 = [2,3,4,5,6,7,8]

plt.plot(X, Y1, "sm", label="week1")
plt.plot(X, Y2, label="week2")
plt.ylabel("Temperature")
plt.xlabel("Day")
plt.legend()
plt.show()

plt.bar(X,Y1)
plt.show()
"""
import matplotlib.pyplot as plt 
from wordcloud import WordCloud

text=""
with open("mobydick.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    i =  0
    for line in lines:
        text += line
        i += 1 
        if i == 10 : 
            print(text)

wc = WordCloud(width=600,height=400)

wc.generate(text)
wc.to_file("wc.png")

plt.figure(figsize=(30,10))
plt.imshow(wc)
plt.show()
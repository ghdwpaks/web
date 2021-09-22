import random as r
import time as t


print("two dic are rolling ...")

t.sleep(2)

while True :

    m = r.randint(1,6)
    c = r.randint(1,6)
    if m > c :
        break
print("나 :",m)
print("컴 :",c)

if m == c :
    print("비겼습니다!")
elif m > c :
    print("플레이어가 이겼습니다!")
else :
    print("컴퓨터가 이겼습니다!")


# 產生一個隨機整數 1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了！"
# 猜錯的話 要告訴他 比答案大/小

import random
start = input("請輸入隨機數字開始值:")
end = input("請輸入隨機數字結束值:")
start = int(start)
end = int(end)
num = random.randint(start, end)
count = 0
while True:
    count += 1
    ans = input("請輸入數字:")
    ans = int(ans)
    if ans == num:
        print("終於猜對了！")
        print("這是你猜的第",count,"次")
        break
    elif ans > num:
        print("比答案大")
    elif ans < num:
        print("比答案小")
    print("這是你猜的第",count,"次")
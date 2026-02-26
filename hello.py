import random

def guess_number_game():
    # 1. 電腦隨機產生一個 1 到 100 的數字
    answer = random.randint(1, 100)
    guess = 0
    count = 0

    print("--- 歡迎來到猜數字遊戲！ ---")
    print("我已經想好了一個 1 到 100 之間的數字。")

    # 2. 使用迴圈讓玩家重複輸入，直到猜中為止
    while guess != answer:
        try:
            # 取得玩家輸入並轉換成整數
            guess = int(input("請輸入你猜的數字："))
            count += 1 # 記錄猜測次數

            # 3. 判斷大小並給予提示
            if guess < answer:
                print("太低了！再試一次。")
            elif guess > answer:
                print("太高了！再試一次。")
            else:
                print(f"恭喜你！你答對了！答案就是 {answer}")
                print(f"你總共猜了 {count} 次。")
                
        except ValueError:
            print("請輸入有效的數字喔！")

# 執行遊戲
if __name__ == "__main__":
    guess_number_game()
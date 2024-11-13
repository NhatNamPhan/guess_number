import random

print("Chào mừng bạn đến với trò chơi đi tìm số bí ẩn")
print("Chọn chế độ:")
print("1.Chế độ dễ(1-100)")
print("2.Chế độ khó(1-200)")

while True:
    mode_game = input("Mời bạn chế độ chơi (1 hoặc 2):")
    if mode_game in ["1" , "2"]:
        break
    else:
        print("Hãy chọn đúng chế độ chơi(1 hoặc 2).")


def check_number():
    dem = 0
    if mode_game == "1":
        number_secret = random.randint(1,100)
    else:
        number_secret = random.randint(1,200)
    
    while True:
        try:
            number_guess = int(input("Số bí ẩn là: "))
            if number_guess > number_secret:
                print("Số bạn đoán cao hơn số bí ẩn")
                dem += 1
            elif number_guess < number_secret:
                print("Số bạn đoán thấp hơn số bí ẩn")
                dem += 1
            else:
                dem += 1
                if dem > 5:
                    print(f"Chúc mừng bạn đã đoán đúng số bí ẩn với số lần đoán là: {dem}")
                else:
                    print("Chúc mừng bạn đã đoán đúng số bí ẩn")
                    print(f"Bạn đã hoàn thành trò chơi xuất sắc với số lần đoán là: {dem}")
                break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ")

check_number()
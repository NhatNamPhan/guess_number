import random

print("Chào mừng bạn đến với trò chơi đi tìm số bí ẩn")
print("Chọn chế độ:")
print("1.Chế độ dễ(1-100)")
print("2.Chế độ khó(1-200)")

while True:
    mode_game = input("Mời bạn chế độ chơi (1 hoặc 2):")
    if mode_game == ["1" , "2"]:
        break
    else:
        print("Hãy chọn đúng chế độ chơi(1 hoặc 2).")


def check_number():
    if mode_game == "1":
        number_secret = random.randint(1,100)
    elif mode_game == "2":
        number_secret = random.randint(1,200)
    else :
        print("Hãy chọn đúng chế độ chơi(1 hoặc 2)")
    while True:
        try:
            number_guess = int(input("Số bí ẩn là:"))
            if number_guess > number_secret :
                print("Số bạn đoán cao hơn số bí ẩn")
            elif number_guess < number_secret :
                print("Số bạn đoán thấp hơn số bí ẩn")
            else :
                print("Chúc mừng bạn đã đoán đúng số bí ẩn")
                break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ")

check_number()
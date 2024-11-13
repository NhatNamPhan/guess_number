import random
import tkinter as tk
from tkinter import messagebox

secret_number = None
dem = 0
difficulty = "easy"


def set_difficulty(mode):
    global difficulty, secret_number, dem
    difficulty = mode
    dem = 0
    if difficulty == "easy":
        secret_number = random.randint(1, 100)
    else:
        secret_number = random.randint(1, 200)
    label_result.config(text="")


def guess_number():
    try:
        global dem
        dem += 1
        number_guess = int(number_entry.get())
        if number_guess == secret_number:
            if dem > 5:
                label_result.config(text=f"Chúc mừng bạn đã đoán đúng số bí mật với số lần đoán là: {dem}")
            else:
                label_result.config(text=f"Chúc mừng bạn đã hoàn thành trò chơi xuất sắc!!!\nSố lần đoán là: {dem}")
        elif number_guess > secret_number:
            label_result.config(text="Số bạn đoán cao hơn số bí mật")
        else:
            label_result.config(text="Số bạn đoán thấp hơn số bí mật")
    except ValueError:
        label_result.config(text="Vui lòng nhập một số hợp lệ")


window = tk.Tk()
window.title("Trò chơi đoán số")
window.configure(bg='#f0f0f0')


main_frame = tk.Frame(window, bg='#f0f0f0', pady=20)
main_frame.pack(expand=True)

label = tk.Label(
    main_frame,
    text="Tôi đã chọn số bí mật từ 1 đến 100. Hãy đoán số bí mật",
    font=('Arial', 10, 'bold'),
    bg='#f0f0f0',
    wraplength=250
)
label.pack(pady=10)

label_secret = tk.Label(
    main_frame,
    text="Số bí mật:",
    font=('Arial', 10),
    bg='#f0f0f0'
)
label_secret.pack()

number_entry = tk.Entry(
    main_frame,
    font=('Arial', 12),
    width=15,
    justify='center'
)
number_entry.pack(pady=5)

button_check = tk.Button(
    main_frame,
    text="Kiểm tra",
    command=guess_number,
    font=('Arial', 10, 'bold'),
    bg='#4CAF50',
    fg='white',
    width=15,
    cursor='hand2'
)
button_check.pack(pady=10)

label_result = tk.Label(
    main_frame,
    text="",
    font=('Arial', 10, 'bold'),
    bg='#f0f0f0',
    fg='#333333'
)
label_result.pack(pady=5)

difficulty_frame = tk.Frame(main_frame, bg='#f0f0f0')
difficulty_frame.pack(pady=5)

easy_button = tk.Button(
    difficulty_frame,
    text="Dễ (1-100)",
    command=lambda: set_difficulty("easy"),
    font=('Arial', 10),
    bg='#4CAF50',
    fg='white',
    width=10,
    cursor='hand2'
)
easy_button.pack(side=tk.LEFT, padx=5)

hard_button = tk.Button(
    difficulty_frame,
    text="Khó (1-200)",
    command=lambda: set_difficulty("hard"),
    font=('Arial', 10),
    bg='#FF5722',
    fg='white',
    width=10,
    cursor='hand2'
)
hard_button.pack(side=tk.LEFT, padx=5)

set_difficulty("easy")

window.geometry("350x300")
window.mainloop()
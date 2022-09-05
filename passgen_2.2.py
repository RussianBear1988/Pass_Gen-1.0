import random

print("Этот код генерирует случайный пароль из стандартного набора переменных")
run = 1

def lengh_check(length_input):
    try:
        int(length_input)
    except ValueError:
        print("Вы ввели букву или слово. Мы не можем сгенерировать пароль из этих значений. Пожалуйста, введите число от 12 до 30: ")
        return False
    if int(length_input) < 12:
        print("""Вы ввели слишком маленькое число. Мы не сможем сгенерировать такой пароль :(
Попробуйте ввести его снова: """)
        return False
    elif  int(length_input) > 31:
        print("""Вы ввели слишком большое число. Мы не сможем сгенерировать такой пароль :(
        Попробуйте ввести его снова: """)
        return False
    else:
        return True

def password(length_input):
    passord_key = []

    for number in range(random.randint(2, 7)):
        number = random.randint(0, 9)
        passord_key.append(number)

    for symbol in range(random.randint(3, 9)):
        letter = 'abcdefghijklmnopqrstuvwxyz'
        symbol = random.choice(letter)
        passord_key.append(symbol)

    for symbol_h in range(random.randint(3, 9)):
        letter_h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        symbol = random.choice(letter_h)
        passord_key.append(symbol)

    for special in range(random.randint(3, 9)):
        symbol_list = '!@#$%^&*()_+{}:"|>?<~╥↕╕'
        special = random.choice(symbol_list)
        passord_key.append(special)
    random.shuffle(passord_key)
    real_password = "".join(map(str, passord_key))

    if len(real_password) == length_input:
        print(f"""Ваш новый пароль:
{real_password}""")
        print(f"Он состоит из {len(real_password)} символов.")
        return real_password
    else:
        password(length_input)


while run == 1:
    length_input = input("Введите минимальную желаемую длину пароля. Эта программа может сгенерировать пароль от 12 до 30 символов: ")
    if lengh_check(length_input):
        password(int(length_input))
        run -= 1

import random
print("Этот код генерирует случайный пароль из стандартного набора переменных")
length_input = int(input("Введите минимальную желаемую длину пароля: "))
while length_input > 30:
    length_input = int(input("""Вы ввели слишком большое число (или слишком маленькое число). Мы не сможем сгенерировать такой пароль :(
Попробуйте ввести его снова: """))
def password():
    passord_key = []

    for number in range(random.randint(2, 6)):
        number = random.randint(0, 9)
        passord_key.append(number)

    for symbol in range(random.randint(3, 8)):
        letter = 'abcdefghijklmnopqrstuvwxyz'
        symbol = random.choice(letter)
        passord_key.append(symbol)

    for symbol_h in range(random.randint(3, 8)):
        letter_h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        symbol = random.choice(letter_h)
        passord_key.append(symbol)

    for special in range(random.randint(3, 8)):
        symbol_list = '!@#$%^&*()_+{}:"|>?<~'
        special = random.choice(symbol_list)
        passord_key.append(special)
    random.shuffle(passord_key)
    real_password = "".join(map(str, passord_key))
    if len(real_password) == length_input:
        return real_password
    else:
        password()


print(password())


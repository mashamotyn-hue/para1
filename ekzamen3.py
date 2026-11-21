import random
import string


def generate_password(length=12):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for _ in range(length))
  return password


if __name__ == '__main__':
  print('Генератор надежных паролей ')

  try:
    user_input = input('Ввиде длинну желемого пароля (можно нажать Enter для длины 12): ').strip()

    if user_input:
      length = int(user_input)
    else:
      length = 12
    new_password = generate_password(length)
    print(f'\nТвой новый пароль:\n{new_password}')

  except ValueError:
    print('Не правильно! Нужно ввести число')
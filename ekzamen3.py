import random
import string


def generate_password(length=12):
  # Все буквы (маленькие и большие), цифры и знаки препинания
  characters = string.ascii_letters + string.digits + string.punctuation

  # Собираем случайный пароль нужной длины
  password = ''.join(random.choice(characters) for _ in range(length))
  return password


if name == 'main':
  print('=== Генератор надежных паролей ===')

  try:
    # Запрашиваем длину у пользователя
    user_input = input(
        'Введи желаемую длину пароля (просто нажми Enter для длины 12): '
    ).strip()

    if user_input:
      length = int(user_input)
    else:
      length = 12

    # Генерируем и выводим
    new_password = generate_password(length)
    print(f'\nТвой новый пароль:\n{new_password}')

  except ValueError:
    print('Ошибка! Нужно было ввести целое число.')
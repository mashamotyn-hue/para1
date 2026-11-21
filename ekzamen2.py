import random


def guess_number_game():
  print(' igra ygadai chislo ')
  print('Я загадал число от 1 до 100. ygadai\n')

  secret_number = random.randint(1, 100)
  attempts = 0

  while True:
    try:
      user_input = input('vvedi chislo: ')
      guess = int(user_input)
      attempts += 1

      if guess < secret_number:
        print(' chislo bolshe. davay again\n')
      elif guess > secret_number:
        print(' chislo menshe. davay again\n')
      else:
        print(f' УРЫ! ti ygadal {secret_number}!')
        print(f' ti potratil stolko popitok: {attempts}\n')
        break

    except ValueError:
      print(' ne pravilno! nyshno vvesti imenno chislo.\n')


if __name__ == '__main__':
  while True:
    guess_number_game()
    play_again = (
        input('hochesh esche poigrat? (yes/no): ').strip().lower()
    )
    if play_again != 'yes' and play_again != 'no':
      print('prihodi kogda sveta ne bydet')
      break
    print('\n' + '=' * 30 + '\n')
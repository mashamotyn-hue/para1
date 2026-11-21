import random


def hangman_game():
  # 100 слов разной длины в случайном порядке
  words = [
      'кот',
      'электричество',
      'луна',
      'программирование',
      'мяч',
      'достопримечательность',
      'сыр',
      'кибернетика',
      'дом',
      'холодильник',
      'лес',
      'экскаватор',
      'сок',
      'космонавтика',
      'нос',
      'аккумулятор',
      'снег',
      'путешествие',
      'мост',
      'температура',
      'ключ',
      'энциклопедия',
      'тигр',
      'воображение',
      'слон',
      'университет',
      'хлеб',
      'велосипедист',
      'парк',
      'метеорология',
      'град',
      'эксперимент',
      'зонт',
      'архитектура',
      'кран',
      'лаборатория',
      'стул',
      'инструмент',
      'море',
      'библиотекарь',
      'рыба',
      'микроволновка',
      'лиса',
      'независимость',
      'волк',
      'понедельник',
      'утка',
      'калькулятор',
      'гусь',
      'телевизор',
      'шарф',
      'справедливость',
      'плащ',
      'фотография',
      'гном',
      'приключение',
      'трон',
      'информация',
      'клад',
      'землетрясение',
      'звук',
      'благодарность',
      'свет',
      'строительство',
      'тьма',
      'электростанция',
      'пыль',
      'супермаркет',
      'грязь',
      'аквариумист',
      'соль',
      'парикмахерская',
      'боль',
      'сковородка',
      'ночь',
      'авиаконструктор',
      'день',
      'подснежник',
      'утро',
      'ветеринар',
      'зима',
      'небоскреб',
      'лето',
      'дирижабль',
      'осень',
      'хамелеон',
      'ветер',
      'крокодил',
      'огонь',
      'дикобраз',
      'вода',
      'пингвин',
      'земля',
      'фламинго',
      'небо',
      'осьминог',
      'звезда',
      'медуза',
      'облако',
      'черепаха',
  ]

  word = random.choice(words)
  guessed_letters = []
  attempts = 6

  print('igra: visiliza (raznie yrovni)')
  print(f'ya zagadala slovo {len(word)} bykv. y tebya est {attempts} chizney.')

  while attempts > 0:
    display_word = ''
    for letter in word:
      if letter in guessed_letters:
        display_word += letter + ' '
      else:
        display_word += '_ '

    print(f'\nclovo: {display_word.strip()}')

    if '_' not in display_word:
      print(f'\n pobeda. zagadanoe clovo: {word}')
      return True

    guess = input('Введи букву: ').lower().strip()

    if not guess.isalpha() or len(guess) != 1:
      print('moshno vvodit tolko 1 bykvy')
      continue

    if guess in guessed_letters:
      print(f'Bykva «{guess}» yshe bila vvedena')
      continue

    guessed_letters.append(guess)

    if guess in word:
      print(f' Есть такая буква: «{guess}»!')
    else:
      attempts -= 1
      print(f' LOX! Ostaloc: {attempts}')

      if attempts == 0:
        print(f'\n proigral! slovo bilo: {word}')
        return False


if __name__ == '__main__':
  while True:
    hangman_game()
    again = (
        input('\nСыграть ещё раз? Напиши "да" (или Enter для выхода): ')
        .strip()
        .lower()
    )
    if again != 'да':
      print('Выход из игры.')
      break
    print('\n' + '=' * 40 + '\n')
import random


class Letet:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.alive = True

    def to_fly(self):
        print('ya lechy')
        self.hunger -= 9

    def to_eat(self):
        print('ya keshayu')
        self.hunger += 9
        if self.hunger > 100:
            self.hunger = 100

    def is_alive(self):
        if self.hunger <= 0:
            self.hunger = 0
            print('ya ne pokyshal...')
            self.alive = False

    def end_of_day(self):
        print(f'Hunger = {self.hunger}')

    def live(self, day):
        mess = f'Day {day} of {self.name} life'
        print(f'{mess:=^30}')

        live_cube = random.randint(1, 2)

        if live_cube == 1:
            self.to_fly()
        elif live_cube == 2:
            self.to_eat()

        self.end_of_day()
        self.is_alive()


letet = Letet('Lechy')

for day in range(10):
    if not letet.alive:
        break
    letet.live(day + 1)

    if letet.alive:
        if letet.hunger == 100:
            print('ya obyelas')
        else:
            print('ya mnogo keshala')
    else:
        print('a zgolodala')

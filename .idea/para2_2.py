class Student:
    def __init__(self, name, height=180):
        self.name = name
        self.height = height

    def say_height(self):
        print(f"My height is {self.height}")

    def say_my_name(self):
        print(f"My name is {self.name}")


student1 = Student("vasya", 180)
student1.say_my_name()
student1.say_height()
        
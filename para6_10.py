class AgeError(Exception):
    def __str__(self):
        return "chilipizdrik idi ledi bag smotri"


def check_age(age, limit_age):
    if age >= limit_age:
        return "vot vash beletick"
    else:
        raise AgeError(age)


age = int(input("Enter your age: "))
print(check_age(age, 16))
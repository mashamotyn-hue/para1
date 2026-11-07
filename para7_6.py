class Helper:
    def __init__(self, work):
        self.work = work
        
    def __call__(self, new_work):
        return (f"i will help you with your {self.work}. "
                f"afterw3ard i will help you with{new_work}")

helper = Helper("homework")
print(helper("cleaning"))

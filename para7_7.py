def helper(work):
    work_in_memory = work

    def helper(work):
        return (f"i will help you with your {work_in_memory}. "
                f"afterw3ard i will help you with {work}")
    return helper

helper = helper("homework")
print(helper("cleaning"))
print(helper("driving"))










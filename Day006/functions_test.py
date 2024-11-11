def get_user_name():
    username = input("Was ist dein Name?: ")
    return username


def greet_user():
    username = get_user_name()
    print(f"Hallo {username}")


greet_user()

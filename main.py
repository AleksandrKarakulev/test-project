def main():
    username = input()
    if not check_is_name(username):
        username = fix_name(username)
    greeting = f"Hello {username}!"
    fency_output(greeting)


def fency_output(line):
    print("=============")
    print(line)
    print("=============")


def check_is_name(username):
    first_letter = username[0]
    return first_letter.isupper()


def fix_name(username):
    username = username[0].upper() + username[1:]
    return username


if __name__ == "__main__":
    main()

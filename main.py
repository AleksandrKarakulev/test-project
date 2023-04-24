def main():
    username = input()
    greeting = f"Hello {username}"
    fency_output(greeting)


def fency_output(line):
    print("=============")
    print(line)
    print("=============")


def check_is_name(username):
    first_letter = username[0]
    return first_letter.isupper()


if __name__ == "__main__":
    main()

def main():
    username = input()
    greeting = f"Hello {username}"
    fency_output(greeting)


def fency_output(line):
    print("=============")
    print(line)
    print("=============")


if __name__ == "__main__":
    main()

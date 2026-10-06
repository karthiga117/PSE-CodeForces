from unicodedata import name


def solve():
    name = input()
    textLen = len(name)
    remainingletter = textLen - 2
    print(f"The length of the {name} is: {textLen}")
    print(f" {name[0]}{remainingletter}{name[textLen-1]}")


if __name__ == "__main__":
    solve()
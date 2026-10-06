def solve():
    word_count = int(input())
    abbreviated_words = []

    for _ in range(word_count):
        word = input().strip()
        if len(word) > 10:
            word = f"{word[0]}{len(word) - 2}{word[-1]}"
        abbreviated_words.append(word)

    print("\n".join(abbreviated_words))


if __name__ == "__main__":
    solve()

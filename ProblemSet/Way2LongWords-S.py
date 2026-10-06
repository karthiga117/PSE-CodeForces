def FindLongWord():
    n = int(input(""))
   
    user_word = []
    for i in range(n):
        word = input()
        user_word.append(word)

    for name in user_word:
        textLen = len(name)

        if(textLen>10):
            remainingletter = textLen - 2
            print(f"{name[0]}{remainingletter}{name[textLen-1]}")
        else : print(name)



if __name__ == "__main__":
    FindLongWord()
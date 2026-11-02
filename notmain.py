import random

def main():
    words = ["rain", "hate", "next", "vain", "lame", "fear", "read", "pale", "loop", "nest", "rest", "pope"]
    word = random.choice(words)
    tries = 0
    list1 = [" _ ", " _ ", " _ ", " _ "]
    while True:
        guess = input("make your guess, its a 4 letter word: ")
        if guess.isalpha():
            if len(guess) != 4:
                print("bro its 4 letters only")
            else:
                if guess == word:
                    tries += 1
                    print("wow you won")
                    print(f"it took you {tries} tries")
                    break
                else:
                    tries += 1
                    guess = guess.lower()
                    for letter in guess:
                        if letter in word:
                            index = 0
                            letter2 = word[index]
                            while letter2 != letter:
                                index += 1
                                letter2 = word[index]
                            print(f"yes {letter} was in the word")
                            list1[index] = f" {letter} "
            print(list1)
        else:
            print("no digits or anything besides a 4 letter word")


if __name__ == "__main__":
    main()
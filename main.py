import random

file = open("wordList.txt", "r")
wordList = file.readlines()
word = wordList[random.randint(0, len(wordList) - 1)].upper()

print("Welcome to Wordle!")
i = 1
while i < 7:
    print()
    print(i)

    choice = input("Choose a 5-letter word: ").upper()
    i = i + 1

    if len(choice) == 5:
      if (choice[0] != word[0] and choice[0] != word[1]
      and choice[0] != word[2] and choice[0] != word[3]
      and choice[0] != word[4] and choice[1] != word[0]
      and choice[1] != word[1] and choice[1] != word[2]
      and choice[1] != word[3] and choice[1] != word[4]
      and choice[2] != word[0] and choice[2] != word[1]
      and choice[2] != word[2] and choice[2] != word[3]
      and choice[2] != word[4] and choice[3] != word[0]
      and choice[3] != word[1] and choice[3] != word[2]
      and choice[3] != word[3] and choice[3] != word[4]
      and choice[4] != word[0] and choice[4] != word[1]
      and choice[4] != word[2] and choice[4] != word[3]
      and choice[4] != word[4]):
        print("There is no letter in the word.")

      if (choice[0] == word[0] and choice[1] == word[1]
      and choice[2] == word[2] and choice[3] == word[3]
      and choice[4] == word[4]):
        print("You guessed the word: " + word)
        quit()

      if (choice[0] == word[0]):
        print(word[0] + " is correct.")

      if (choice[1] == word[1]):
        print(choice[1] + " is correct.")

      if (choice[2] == word[2]):
        print(choice[2] + " is correct.")

      if (choice[3] == word[3]):
        print(choice[3] + " is correct.")

      if (choice[4] == word[4]):
        print(choice[4] + " is correct.")

      if ((choice[0] != word[0])
      and (choice[0] == word[1] or choice[0] == word[2]
      or choice[0] == word[3] or choice[0] == word[4])):
        print(choice[0] + " is in the word but not in that place.")

      if ((choice[1] != word[1])
      and (choice[1] == word[0] or choice[1] == word[2]
      or choice[1] == word[3] or choice[1] == word[4])):
        print(choice[1] + " is in the word but not in that place.")

      if ((choice[2] != word[2])
      and (choice[2] == word[0] or choice[2] == word[1]
      or choice[2] == word[3] or choice[2] == word[4])):
        print(choice[2] + " is in the word but not in that place.")

      if ((choice[3] != word[3])
      and (choice[3] == word[0] or choice[3] == word[1]
      or choice[3] == word[2] or choice[3] == word[4])):
        print(choice[3] + " is in the word but not in that place.")

      if ((choice[4] != word[4]) and (choice[4] == word[0] or choice[4] == word[1] or choice[4] ==         word[2] or choice[4] == word[3])):
        print(choice[4] + " is in the word but not in that place.")

    else:
      print("The letter must be 5 letters! Please try again.")
      i = i - 1
      continue

    if i == 7:
      print("\nYou ran out of tries! The word was " + word)
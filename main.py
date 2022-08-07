import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
file = open("wordList.txt", "r")
wordList = file.readlines()
word = wordList[random.randint(0, len(wordList) - 1)].upper() # makes all the words uppercase

print(word)

print("Welcome to Wordle!")
tries = 1
while tries < 7:
	print()
	print("Try", tries)
	print(alphabet)
	choice = input("\nChoose a 5-letter word: ").upper()
	tries = tries + 1

	if word[0] == choice[0] and word[1] == choice[1] and word[2] == choice[2] and word[3] == choice[3] and word[4] == choice[4]:
		print("You guessed the word: " + word)
		break
		
	else:
		if len(choice) == 5:    
			for i in range(5):
				if choice[i] == word[i]:
					print(word[i] + " is correct.")

				# if the letter is in the word but not in that place
				if choice[i] in word and choice[i] != word[i]:
					print(choice[i] + " is in the word but not in that place")
					
				if choice[i] not in word:
					if choice[i] not in alphabet: # have to put this if statement because it will give an error if it tries to remove a letter from the alphabet list that is already taken out.
						print(choice[i], "is not in the word")
					else:
						print(choice[i], "is not in the word.")
						alphabet.remove(choice[i])

		else:
			print("The letter must be 5 letters! Please try again.")
			tries = tries - 1
			continue

	if tries == 7:
		print("\nYou ran out of tries! The word was " + word) # prints once while loop is done


# for loop is used when we are comparing each letter in one iteration.
# for loop is not used when all the letters have to be compared with each other like guessing the entire word
import random


def loadWords():
    wordsLocation = "words.txt"
    with open(wordsLocation, "r") as file:
        print("Loading words...")
        line = file.readline()
        wordsList = line.split(" ")
        print("{} words loaded".format(len(wordsList)))
    return wordsList


def getWord():
    return random.choice(loadWords())


def checkLetterGuessed(letter, storageOfLetters):
    count = 0
    for item in storageOfLetters:
        if letter in item:
            count += 1
        else:
            pass
    if count > 0:
        return True
    else:
        return False


def availableLetters(usedLetters):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    for letter in alphabet:
        if letter in usedLetters:
            alphabet.remove(letter)
    return ", ".join(alphabet)


def checkLetterInWord(letter, word):
    locations = {}
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                locations[i] = letter
        return {"boolean": True, "locations": locations}
    else:
        return {"boolean": False, "locations": locations}


def displayUserWordProgress(userWord, gameWord, letterLocations):
    userWord = userWord.split(" ")
    if len(userWord) > len(gameWord):
        del userWord[len(userWord)-1]
    for index in letterLocations:
        userWord[index] = letterLocations[index]
    userWord = " ".join(userWord)
    return userWord


def hangman():
    print()
    gameWord = getWord()
    # print(gameWord)
    userWord = "- "*len(gameWord)
    cleanUserWord = "".join(userWord.split(" "))
    remainingGuesses = 8
    lettersGuessed = {}
    print("There are {} letters in the word".format(len(gameWord)))
    print()
    while remainingGuesses > 0 and cleanUserWord != gameWord:
        print("-"*80)
        userLetter = input("Guess a letter: ")
        print()
        letterWasGuessed = checkLetterGuessed(userLetter, lettersGuessed)
        letterInWord = checkLetterInWord(userLetter, gameWord)["boolean"]
        letterLocations = checkLetterInWord(userLetter, gameWord)["locations"]
        if letterWasGuessed:
            print("You already guessed that letter. Guess again.")
        elif (not letterWasGuessed) and (letterInWord):
            print("Way to go, {} is in the word".format(userLetter))
            lettersGuessed[userLetter] = userLetter
            userWord = displayUserWordProgress(userWord, gameWord, letterLocations)
            cleanUserWord = "".join(userWord.split(" "))
            print(userWord)
        elif (not letterWasGuessed) and (not letterInWord):
            print("Sorry, {} is not in the word".format(userLetter))
            lettersGuessed[userLetter] = userLetter
            userWord = displayUserWordProgress(userWord, gameWord, letterLocations)
            cleanUserWord = "".join(userWord.split(" "))
            print(userWord)
            remainingGuesses -= 1
        if cleanUserWord != gameWord:
            print("You have {} guesses remaining".format(remainingGuesses))
            print()
            print("Your available letters are {}".format(availableLetters(lettersGuessed)))
            print("-"*80)
    else:
        if cleanUserWord == gameWord:
            print("Congratulations, you guessed the word! It was {}!".format(cleanUserWord))
        else:
            print("Better luck next time! The word we were looking for was: {}".format(gameWord))


hangman()

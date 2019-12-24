import json
from difflib import get_close_matches

# loading words and defenitions from the json 
with open("dictionary.json") as data:
    dictData = json.load(data)


# a function that return the definition of a word entered as an argument


def getDefinition(word, dictData):
    word = word.upper()
    if word in dictData:
        return dictData[word]
    elif len(get_close_matches(word, dictData.keys())) > 0:
        recommend = input(
            f"did u mean : {get_close_matches(word,dictData.keys())[0].lower()} !?? Enter yes or no ?  ")
        if recommend == "yes":
            return dictData[get_close_matches(word, dictData.keys())[0]]
        elif recommend == "no":
            return(" sorry this word doesn't exist")
        else:
            return("sorry we couldn't understand what you've entered ")
    else:
        return("sorry this word doesn't exist")


while True:
    word = input("enter a word please!:  ")
    print(getDefinition(word, dictData))
    anotherWord = input("do u want to enter another word!? Enter yes or no ?  ")
    if anotherWord == "yes":
        continue
    else:
        break

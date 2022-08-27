import json
from difflib import get_close_matches

data = json.load(open("E:\Projects\Python\Dictionary\data.json"))
word = input("Enter The Word You want to Search: ")

def translate(word):
    word = word.lower()
    if word in data:
        print(data[word])
    elif word.title() in data:
        print(data[word.title()])
    elif word.upper() in data:
        print(data[word.upper()])
    elif len(get_close_matches(word,data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == 'n':
            return["You Entered the wrong word"]
        else:
            return["You have entered wrong input please enter just y or n"]
    else:
        print("No Data Found")


output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
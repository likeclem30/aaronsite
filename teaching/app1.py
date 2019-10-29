import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    if w.title() in data:
        return data[w.title()]
    if w.upper() in data:
        return data[w.upper()]
    elif w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for YES and N for No :" % get_close_matches(w,data.keys())[0]).upper()
        if yn== 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return 'The word does not exits. Please double check'
        else:
            return 'We do not understand your entry'
    else:
        return "The word does not exit.Please double check it"

word = input("Enter word to define :").lower()
output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
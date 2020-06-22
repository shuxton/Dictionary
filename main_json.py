import json
from difflib import SequenceMatcher,get_close_matches

data=json.load(open("data.json"))

def translate(word):
    try:
        return data[word]
    except:
        try:
            word=word.lower()
            return data[word]
        except:
            if len(get_close_matches(word,data.keys()))>0:
                print("Did you mean %s instead?"%get_close_matches(word,data.keys())[0])
                choice=input("Press (Y/N): " )
            
                if choice.lower() == "y":
                    return data[get_close_matches(word,data.keys())[0]]
        
                else:
                    return "The word doesn't exist.Please double check it."
        

while(True):
    word= input("Enter word: ")
    try:
        if(int(word) == 0):
            break
    except:
        output=translate(word)
        if type(output)==list:
            for item in output:
                print(item)
        else:
            print(output)

import requests

key = "d1af44d2-bfbd-41bc-8db9-409dca19b996" #The API key you need to get the synonyms
word = "run"
#r = requests.get("http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/{}?".format(word), params = {"key":key})

#print(r.text)

wikipedia = requests.get("http://simple.wikipedia.org/wiki/Wikipedia:Basic_English_combined_wordlist")

def check_if_simple(word):
    if(word in wikipedia.text):
        return True
    else: return False
    




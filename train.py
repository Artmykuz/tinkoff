import re 

model = "model.txt"

text = open('data/gogol.txt', encoding='utf8').read()   
text = re.sub("[^А-Яа-я- ]", "", text)                  
text = text.lower()                                     

wordsCollection = text.split()

with open(model, "w+") as acd:  
    for listitem in wordsCollection:
        acd.write('%s\n' % listitem)

exec(open('generate.py').read())
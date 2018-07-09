import markovify
import sys

newLineChars = ':,;.?!'

corpusFileName = 'sonnets.txt'

with open(corpusFileName, 'r') as corpusFile:
    corpus = corpusFile.read()

wftModel = markovify.Text(corpus)

userIn = ''

while(userIn != 'exit'):
    sentence = None
    while(sentence == None):
        sentence = wftModel.make_sentence()
    generatedSonnet = ''
    for (i,c) in enumerate(sentence):
        if(c in newLineChars):
            #firstHalf = sentence[:i+1]
            #secondHalf = sentence[i+1:]
            #sentence = firstHalf + '\r\n' + secondHalf
            generatedSonnet = generatedSonnet + c + '\r\n'
        else:
            generatedSonnet = generatedSonnet + c
    with open('generatedSonnet.txt', 'w+') as f:
        f.write(generatedSonnet)
    print(sentence)
    userIn = input('Enter \'exit\' to exit or anything else to make another sentence: ')
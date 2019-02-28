from random import randint
import re

def generate(grammar, nt):
    index = randint(0, len(grammar[nt]) - 1)
    choice = grammar[nt][index]
    literal = choice.split(' ')
    sentence = ''
    for word in literal:
        if word.startswith('<'):
            if not word.endswith('>'):
                sentence += ' ' + generate(grammar, word[:-1]) + word[-1:]
            else:
                sentence += ' ' + generate(grammar, word)
        else:
            sentence += ' ' + word
    return sentence[1:]

def gen(howmany):
    result = []
    grammar = {}

    with open('advice.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            res = line.split('::=')
            choices = res[1].split('|')
            grammar[res[0]] = choices 

    howmany = 10
    for i in range(howmany):
        result.append(re.sub(r'\s+', ' ', generate(grammar, '<s>')))
    return result
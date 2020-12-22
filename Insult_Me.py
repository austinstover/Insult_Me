'''
Author: Austin Stover
Date: December 2020

Generates excellent/strange insults: adjective+curseword+noun.

Requires nltk. May need to run "nltk.download('wordnet')" in python before running this code.
'''

#from random_word import RandomWords
from nltk.corpus import wordnet as wn
import random

nouns, verbs, adjectives, adverbs = [list(wn.all_synsets(pos=POS))
                                     for POS in [wn.NOUN, wn.VERB, wn.ADJ, wn.ADV]]

curses = [
            'ass',
            'asshole',
            'bastard',
            'bitch',
            'bloody',
            'bugger',
            'bullshit',
            'cock',
            'cow',
            'crap',
            'damn',
            'dick',
            'dickhead',
            'fucking',
            'goddamn',
            'hobgoblin',
            'horseshit',
            'piece of shit',
            'piss',
            'prick',
            'pussy',
            'shit',
            'sod',
            'son of a bitch',
            'tit',
            'twat'
        ]

phrases = [
            ['No one asked for your opinion, you ',                 '',     '',     '!'],
            ['I fail to understand how you\'ve become such ',       'a ',   'an ',  '.'],
            ['Get out of my way, you sorry excuse for ',            'a ',   'an ',  '!'],
            ['I cannot believe that ',                         'a ',   'an ',  ' such as yourself could ever be remotely polite.'],
            ['Maybe if you weren\'t such ',                         'a ',   'an ',  ', we could get some things done around here.'],
            ['You\'re ',                                            'a ',   'an ',  '.'],
            ['You ',                                                '',     '',     '.'],
            ['You\'re more dissappointing than ',                   'a ',   'an ',  '.'],
            ['I seem to have forgotten the first time you became ', 'a ',   'an ',  ' but I certainly remember today.']
        ]

while True:
    value = input("\nPress enter for an insult...\n")
    phrase = random.choice(phrases)
    adj = random.choice(adjectives).lemmas()[0].name()
    curseword = random.choice(curses)
    noun = random.choice(nouns).lemmas()[0].name()

    a_or_an_ind = 2 if (adj[0]=='a' or adj[0]=='e' or adj[0]=='i'
                        or adj[0]=='o' or adj[0]=='u') else 1

    print(phrase[0] + phrase[a_or_an_ind]+adj + ' ' + curseword + ' ' + noun + phrase[-1])


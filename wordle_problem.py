# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:36:23 2022

@author: Louis
"""

import pandas as pd

class wordle_problem:
    """
    Creates a wordle_problem object. Takes a path to the unigram frequency
    file from Kaggle, an initial guess ('stare' by default), and the number of
    letters in the word (five by default). The initial guess should be entered
    into Wordle. The object is then updated using the 'update' function, which
    takes the colours of the Wordle response as a string, e.g. a response of
    black, yellow, black, black, and green squares would be entered as
    'bybbg'. After updating a second guess can be made using the 'new_guess'
    function. The procedure is repeated until the correct word is found.
    """
    def __init__(self, vocab_path, guess='stare', letters=5):
        self.guess = guess
        self.letters = letters
        self.query = ['abcdefghijklmnopqrstuvwxyz'] * self.letters
        self.contains = ''
        self.get_word_list(vocab_path)
        self.previous_guesses = [guess]
        print('Initial guess: ' + guess)
    
    def get_word_list(self, path):
        data = pd.read_csv(path, index_col='word')
        flws = [word for word in data.index if (type(word) == str) and (len(word) == self.letters)]
        self.word_list = data.loc[flws]
    
    def construct_query(self):
        re_query = ['['+x+']' for x in self.query]
        re_query = ''.join(re_query)
        return(re_query)
    
    def update(self, colours):
        """
        Updates the wordle_problem object with a string representing the
        Wordle response, e.g. a response of black, yellow, black, black, and
        green squares would be entered as 'bybbg'
        """
        for x in range(self.letters):
            guess_x = self.previous_guesses[-1][x]
            if colours[x] == 'g':
                self.query[x] = guess_x
            if colours[x] == 'y':
                self.query[x] = ''.join([x for x in self.query[x] if x != guess_x])
                if guess_x not in self.contains:
                    self.contains = self.contains + self.previous_guesses[-1][x]
            if colours[x] == 'b':
                for query_num in range(self.letters):
                    if len(self.query[query_num]) > 1:
                        self.query[query_num] = ''.join([x for x in self.query[query_num] if x != guess_x])
        print('Updated')
    
    def new_guess(self):
        """
        Produces a new guess for the word based on previous results. If the
        guess is not accepted by Wordle, e.g. if it is a proper name or not
        recognised as a word the function may be called again for a new guess.
        """
        re_query = self.construct_query()
        matches = [x[0] for x in self.word_list.index.str.findall(re_query) if x != []]
        for letter in self.contains:
            matches = [match for match in matches if letter in match]
        matches = [match for match in matches if match not in self.previous_guesses]
        self.previous_guesses.append(matches[0])
        print('New guess: ' +matches[0])

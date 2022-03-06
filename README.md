# wordle_problem
Program to solve Wordle problems with any number of letters

Creates a wordle_problem object. Takes a path to the unigram frequency file from Kaggle, an initial guess ('stare' by default), and the number of letters in the word (five by default). The initial guess should be entered into Wordle. The object is then updated using the 'update' function, which takes the colours of the Wordle response as a string, e.g. a response of black, yellow, black, black, and green squares would be entered as 'bybbg'. After updating a second guess can be made using the 'new_guess' function. The procedure is repeated until the correct word is found.

Uses the English word frequency database from https://www.kaggle.com/rtatman/english-word-frequency

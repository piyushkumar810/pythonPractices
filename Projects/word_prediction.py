'''
----------------------------- psedo code-------------------------

1. start the program
2. show welcome messages and the rules of the game.
3. let user choose a difficulty level
    a. based on level, set a list of possible secret words.

4. randomly select a secret word form the chosen list.

5.tell the user how many letters are in the secret word.

6. set attempts counter to 0.

7. while the user hasn't gussed the word:
    a. ask user to enter a guess.
    b. increment attempts counter

    c. if guess equals secret word
        i. print "congratulation" and show attempts.
        ii. break loop

    d. else:
        i. compair each letter in the guss to the secret word.
        ii. count how many letters are correct and the correct place
'''
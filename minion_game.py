'''Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.'''

def minion_game(string):
    p1 = {
        "name" : "Kevin",
        "score" : 0
    }
    p2 = {
        "name" : "Stuart",
        "score" : 0
    }
    
    for i, char in enumerate(string):
        if char.lower() in "aeiou":
            p1["score"] += len(string) - i
        else:
            p2["score"] += len(string) - i
    if p1["score"] > p2["score"]:
        print(p1["name"],p1["score"])
    elif p1["score"] < p2["score"]:
        print(p2["name"],p2["score"])
    else:
        print("Draw")
        
minion_game("An")
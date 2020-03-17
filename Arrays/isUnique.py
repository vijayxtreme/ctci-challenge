#IsUnique
'''
Implement an algorithm to determine if a string has all unique characters.  What if you cannot use additional data structures?

My Ideas
--------
Get the word, then convert it to an array.
In Python, we can just use list over a word.
(In the future, I'll do this with other languages like Java, JS)

To check unique we can use a hash to count over each letter.

I know I can just compare to letters of the alphabet or ASCII length size, but I wanted to also figure out how to use a hash like in JS.

'''

from collections import defaultdict

word = "smoch"

def isUnique(str):
    flag = True
    l = list(str) #basically use this to turn a string into an array with python
    d = defaultdict(lambda: 0) # we need defaultdict otherwise, dict will throw an error

    for k in l:
        if d[k] == k:
           flag = False
           break
        else:
            d[k] = k
    return flag            

   

print(isUnique(word))

'''
What happens if you can't use another data structure?
Then you have an algorithm that takes O(n^2) time, as you need to compare to previous value.
'''
#Palindrome Permutation
'''
Given a string, write a function to check if it is a permutation of a palindrome.  A palindrome is a word or phrase that is the same forwards and backwards.  A permutation is a rearrangement of letters.   The palindrome does not need to be limited to just dictionary words.

Example: 
Input: Tact Coa
Output: True (permutations: "taco cat", "acto cta", etc.)

My idea:
--------
We basically need to check if this string can be rewritten as a palindrome.  A palindrome has 2 pairs of every letter, with exception being one letter can be without a pair.

So just get the string, then sort, then check if there's a pair for each letter traversed.  If there isn't, then raise a flag (or increase count).  If we raise another flag, then return false.

Another way, could be to just put each element found into a hash, and update its count.  If count mod 2, we're good, however if only 1 count, increment global count; if global count is higher than 2, we don't have a palindrome.  Don't need to sort then.

The only thing to do here extra is to regex test for spaces, commas, non alphachars to make this rock solid
'''
import re
from collections import defaultdict

def isPalindromePermutation(str):
    #creates a hash with all 0s in it (dynamic hash, similar to dynamic array)
    d = defaultdict(lambda: 0)

    # use an if statement if regex doesn't work, with a for loop
    pattern = r"[\s\,]"
    replace = r""
    new_string = re.sub(pattern, replace, str)

    #check the character in the new clean string, add 1 to its value in the hash
    for i in range(0, len(new_string)):
        d[new_string[i].lower()] += 1
    
    more_than_one_non_pair = 0

    #go thru each hash item, check if it's even or odd. if it's even, there's a pair.
    for k,v in d.items():
        print(k,v)
        if(v % 2 != 0):
            more_than_one_non_pair += 1

    if more_than_one_non_pair > 1:
        return False
    
    return True

print(isPalindromePermutation("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canalPanama"))
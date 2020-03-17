#URLify
'''
Write a method to replace all spaces in a string with '%20'.  You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.  

Example:
Input: "Mr John Smith", 13
Output: "Mr%20John%20Smith"

My idea:
- Since we're given the true length of the string, we don't need to worry about "trimming" that much.

I could do a simple regex function.  That's actually kinda great given that it's the fastest algo around, and takes care of tabs, line returns, etc.  But then I'd have to explain why.

Here's a regex:

import re

re.replace(/\s/g, '%20')

What else?  A for loop?

If a for loop, then solution below.

Questions:
Is string mutable or immutable? Is it okay to make a copy of the string, then remove the original string?  I think the Java version of this question is a bit more difficult, given you have to think about this.  Python lets you off.
'''
#runs in O(N) time
def stringReplace(string, length):
    new_string = ""

    for i in range(0, length): 
        if(string[i] == " "):
            new_string += "%20"
        else:
            new_string += string[i]

    return new_string

res = stringReplace('Mr John Smith   ', 13)
print(res)

import re
#regex version, the re.sub matches all instances of a pattern globally by default

def stringReplace2(string):
    pattern = r'\s'
    replace = r'%20'

    return re.sub(pattern, replace, string)

res2 = stringReplace2('Hello John, good to see you')
print(res2)
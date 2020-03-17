#String Rotation
'''
Assume you have a method isSubstring which checks if one word is a substring of another.  Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat").

My idea:
---
If the method isSubstring checks a word is a substring of another, that basically means that we can use to see if the second word was a string of the first word.

Essentially a substring of the first word is somewhere in the second string.  We just need to see how much of the substring exists.

1) The string would have to be the same size as the original string to be considered a rotation.  
2) The letters in a rotation would need to continue in same order; this might be a clue.

If we moved the characters one by one over to the right, the characters would end up again on the other side.  Like a scrolling LED.  This could also work in reverse.  All we would have to do is scroll the text to the right or left until it matched the original string at the same index.  Then we could call the isSubstring function to check.  The trick here is assuming the letters all remain in the same ordering even if they "move" left or right.

'''
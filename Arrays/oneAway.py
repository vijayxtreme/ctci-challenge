#One Away

'''
There are three types of edits that can be performed on strings: Insert a character, remove a character, or replace a character.  Given two strings, write a function to check if they are one edit (or zero edits) away

EXAMPLE
pale, ple -> true #remove a character, 1 edit
pales, pale -> true #remove a character, 1 edit
pale, bale -> true #replace a character, 1 edit
pale, bake -> false #replace 2 characters, 2 edits -> false

My idea:
The first thing we can do is look at the length of each string.  Do they match? If not, by how much do they not match?  If string2 is off by more than string1 - 1, then we know that it's not one away.  

If string2 is off by just 1, then it's one away.  But we still need to now search thru string to make sure no other letters are off. 

If a letter doesn't match, we just up the counter.  If more than one letter isn't matching, then return false.  Also if a letter doesn't match, and it doesn't match the next letter, return false.

I think this will take O(N) time.
'''
#worst case is O(N)
def oneAway(str1, str2):
    counter = 0
    copy_str = ""

    if len(str1) - len(str2) > 1:
        print(False, "Lengths off by more than 1")
        return False 

    if len(str1) - len(str2) == 1:
        #off by 1
        counter +=1
    
    # at this point, we know lengths of str1 & str2 are same or off by 1, so next compare
    for i in range(0, len(str1)):
        if str1[i] != str2[i] and str1[i+1] != str2[i] and i < len(str2):
            counter +=1
            if counter > 1:
                break;

        if i+1 >= len(str2):
            break;
        
    print(counter)
    #not one away
    if counter > 1:
        return False 

    #one
    return True

res = oneAway("pale", "plz")
res2 = oneAway("pales", "pale")
res3 = oneAway("pale", "bale")
res4 = oneAway("pale", "bake")
print(res)
print(res2)
print(res3)
print(res4)
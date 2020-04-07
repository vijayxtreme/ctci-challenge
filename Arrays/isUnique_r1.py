#Is Unique 
'''
I rewrote this one for ASCII / Alphabet

Basically if there are more than 256 characters, this can't be unique because there are only 256 ASCII characters allowed.

If we wanted to just do letters, we could do 26 letters and lowercase all entries

The trick here is that unicode goes up to 128, so we can index every array here 0-128.  If we come across a letter, we can just set it to True, so if we come across it again, we return False.
Pretty brilliant using unicode.
'''

def isUnique(str):
    if(len(str)>128):
        return False

    uniqs = [False] * 128
    for i in range(0, len(str)):
        #ord converts to ascii 1-128, which is fine for an array
        val = ord(str[i])
        if uniqs[val]:
            return False
        uniqs[val] = True

    return True

print(isUnique("hello"))
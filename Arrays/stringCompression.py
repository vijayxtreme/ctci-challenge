#String Compression
'''
Implement a method to perform basic string compression using the counts of repeated characters.  For example, the string aabcccccaaa would become a2b1c5a3.  If the "compressed" string would not become smaller than the original string, your method should return the original string.  You can assume the string has only uppercase and lowercase letters (a-z).

My idea:

So long as the string is the same, iterate. 
Stop when the letter changes, then get the length of the string.

concatenate the letter with the count, then do all these steps again.
Repeat until string finished.
'''

def stringCompression(string):
    count = 0
    compressed_string = ""

    for i in range(0, len(string)):
        count += 1
        if ((i+1>=len(string)) or (string[i] != string[i+1])):
            compressed_string += string[i] + str(count)
            count = 0
    
    return compressed_string

#bad way of doing this, always behind
def stringCompression2(string):
    count = 0
    temp = string[0]
    compressed_string = ""

    for i in range(1, len(string)):
        count += 1
        if string[i] != temp:
            compressed_string += temp + str(count)
            temp = string[i]
            count = 0

        if i+1 >= len(string):
            compressed_string += temp + str(count+1)
    
    return compressed_string

print(stringCompression("aabcccccaaa"))
        
print(stringCompression2("aabcccccaaaab"))

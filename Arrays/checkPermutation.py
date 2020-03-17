#Check Permutation
'''
Given two strings, write a method to decide if one is a permutation of the other.

My idea:
This one seems simple, just sort both strings and compare that they are equal.

O(N log N) time if using MergeSort / QuickSort
'''

def isPermutation(str1, str2):
    return sorted(str1) == sorted(str2)

print(isPermutation("Hello", "elloH"))
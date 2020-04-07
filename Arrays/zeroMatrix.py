#Zero Matrix
#Difficult - please study again
'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

If a value is 0, set entire row to 0 and column to 0.
Before:
[
    [1,0],
    [2,3],
    [4,5]
]
=> Result
[
    [0,0],
    [2,0],
    [4,0]
]

My idea:
--------
Iterate thru the array.  Given this is MxN, it could be O(N^2).
If we encounter a 0, then we mark its position in the array (i,j) and store it in a temp array.

Manually if I had to do this, I'd then look at the t array, and say okay at 0,0 there was a 0.  So go to my other array and find row 0.  All of its values now need to be 0. So I'd say okay for j in arr[0]: arr[0][j] = 0.

Next I'd say okay at 0,0 there was a 0, and look at all columns 0.
for i n arr: arr[i][0] = 0. 

Doing this again if positon 0,1 was 0, I'd go to all rows and turn them 0.  Then I'd go to all columns at pos 1 and turn them 0.

'''

#small test case array 2x2
l = [
    [0,1],
    [1,2]
]

l2 = [
    [0,1,1,0,5],
    [1,1,3,4,1]
]

def zeroMatrix(arr):
    t = [] 

    #get all 0s in the array
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 0:
                #store the row and column number in t
                t.append([i,j])
            print(arr[i][j], end='')
        print('')

    print(t)
    #Check all rows saved in t.
    for i in range(0, len(t)):
        for k in range(0, len(arr)):
            for l in range(0, len(arr[k])):
                #make all the affected rows 0
                arr[t[i][0]][l] = 0

    #Check all cols saved in t.
    for i in range(0, len(t)):
        for k in range(0, len(arr)):
            for l in range(0, len(arr[k])):
                #make all the affected cols 0
                arr[k][t[i][1]] = 0
    
    #Print result
    print("="*3)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            print(arr[i][j], end='')
        print('')

#zeroMatrix(l)
zeroMatrix(l2)
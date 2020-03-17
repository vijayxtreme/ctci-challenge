#Rotate Matrix
'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.  Can you do this in place?

My idea:

An image represented by an NxN matrix.  That means something like an array with x,y coordinates.  NxN means square, since N is same.  

So a square could look like 

 (0,1)-------(1,1)
  |             |
  |             |
  |             |
  |             |
 (0,0)-------(1,0)

 Represented by an array, this would look like: [[0,0],[0,1],[1,0],[1,1]].

 To rotate the image by 90 degrees, all coordinates would change by 1 x or y value.

 [0,0] would become [0,1] 
 [0,1] would become [1,1]
 [1,1] would become [1,0]
 [1,0] would become [0,0]

 The math seems to be like add 1.  0+1 = 1.  1+1=0.

 We could then for loop through the array:

'''
def rotate90(pair):
    x = pair[0]
    y = pair[1]
    if x == 0 and y == 0:
        return [0,1]
    elif x == 0 and y == 1:
        return [1,1]
    elif x == 1 and y == 1:
        return [1,0]
    else:
        return [0,0]

matrix = [[0,0],[0,1],[1,1],[1,0]]
new_rotated_array = []
for i in range(0, len(matrix)):
   print(rotate90(matrix[i]))

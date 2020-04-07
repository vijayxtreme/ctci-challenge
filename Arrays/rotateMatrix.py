#Rotate Matrix
# Not sure - check solution
'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.  Can you do this in place?

My idea:

An image represented by an NxN matrix, basically a square. 

So a square could look like 

 (B)-------(C)
  |         |
  |         |
  |         |
 (A)-------(D)

Represented by an array, this would look like: ["A","B","C","D"].

Moving in 90 degrees just means going top, right, down, left.

Questions:
What does in place mean?
What is the significance of this question being a pixel 4 bytes?
'''

matrix = ["A","B","C","D"]

def rotate90(arr):
    new_rotated_array = []

    left = matrix[3]
    top = matrix[0]
    right = matrix[1]
    down = matrix[2]

    new_rotated_array.append(left)
    new_rotated_array.append(top)
    new_rotated_array.append(right)
    new_rotated_array.append(down)

    return new_rotated_array

print(matrix)
for i in range(0,4):
    matrix = rotate90(matrix)
    print(matrix)

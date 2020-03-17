#Zero Matrix
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
If we encounter a 0, then we need to run a function to go through this row and turn each item to 0.
(What if other items are 0?) - come back to this later
We need to then remember this position in the array.  We can store it in a temp var.
Next go through additional rows and find the same position from temp, then turn that index into a 0 to have the column go zero.
Coming back to the other items are 0, so long as we remember where they were, we can go thru successive rows and turn those same indices 0.  So maybe it makes sense to have a second "memory" array.
What if all rows&cols are 0? Do nothing then.
'''
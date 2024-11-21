"""
Given a vector/ array and 2 numbers, eg 2 and 5. Between those 2 positions in the vector (2 and 5) reverse the order of the elements


we can use a two-pointer approach to swap elements in-place. We'll have two pointers, left and right, initially pointing to start and end, respectively. We'll then iterate while left is less than right, swapping the elements at those indices and moving the pointers towards each other.
"""

def reverse_subarray(arr, start, end):
    left, right = start, end
    
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1
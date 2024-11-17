"""

Given a vector/ array and 2 numbers, eg 2 and 5. Between those 2 positions in the vector (2 and 5) reverse the order of the elements

"""

def reverse_range(arr, start, end):
    
    while start < end:
        if start > end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -+ 1
    
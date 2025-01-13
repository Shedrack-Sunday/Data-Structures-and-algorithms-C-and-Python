def twosum(nums, target):
   seen = {}

  for i, num in enumerate(nums):
      comp = target - num
      if comp in seen:
         return [seen[comp], i]
      seen[num] = i

time complexity: O(n)
Space Complexity: O(n)
One pass method

"""
Most efficient solution requires a hash map.
if unsorted, O(n) time and space.
If it’s sorted you can use two pointers,
for O(n) time O(1) space.
Sorting costs O(n log n) time
"""
Two pass method
Time complexity: O(n)
Space Complexity: O(n)


def twosum(num, target):
   
    seen = {}

    for i, num in enumerate(nums):
       seen[num] = I

    for i, num in enumerate(nums):
        compliment = tartget - num

        if compliment in seen and seen[compliment] != i:
           return [seen[compliment], i]










Time: O(nlogn)
space: O(N)
def hasDuplicates(nums):
  nums.sort()

  for i in range(1, len(nums):
      if nums[i] == nums[i - 1]:
         return True
  return False

## Two pointer approach
Time Complexity: Sorting: O(nlogn), Traversal: O(n), Total = O(nlogn)
Space: Sorting takes O(1)


def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True 
    
    return False 

## Hashing
Time: O(n)
space: O(n)
def hasDuplicates(nums):
   seen = set()

   for num in nums:
       if num in seen:
          return True
       seen.add(num)
   return False

OR
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

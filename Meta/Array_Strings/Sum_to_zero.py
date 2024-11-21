def three_sum(nums):
  """
  Finds all unique triplets in the array that sum to zero.

  Args:
    nums: A list of integers.

  Returns:
    A list of triplets.
  """

Explanation:

"""
Sorting: Sorting the array allows us to efficiently use the two-pointer technique.
Iterating and Two-Pointer Approach:

- We iterate through the array with a i pointer.
- For each i, we initialize two pointers, left and right, to the positions after i and at the end of the array, respectively.
- We calculate the sum of the elements at i, left, and right.
- If the sum is zero, we found a triplet. We add it to the triplets list and move both left and right pointers to skip duplicates.
- If the sum is less than zero, we increment left to increase the sum.
- If the sum is greater than zero, we decrement right to decrease the sum.
This approach ensures that we find all unique triplets efficiently.
"""

def three_sum(nums):
  """
  Finds all unique triplets in the array that sum to zero.

  Args:
    nums: A list of integers.

  Returns:
    A list of triplets.
  """

  nums.sort()  # Sort the array for efficient two-pointer approach
  triplets = []

  for i in range(len(nums) - 2):
    # Skip duplicates to avoid redundant triplets
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    left, right = i + 1, len(nums) - 1
    while left < right:
      total = nums[i] + nums[left] + nums[right]
      if total == 0:
        triplets.append([nums[i], nums[left], nums[right]])
        # # Skip duplicates to avoid redundant triplets
        # while left < right and nums[left] == nums[left + 1]:
        #   left += 1
        # while left < right and nums[right] == nums[right - 1]:
        #   right -= 1
        left += 1
        right -= 1
      elif total < 0:
        left += 1
      else:
        right -= 1

  return triplets

# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # Output: [[-1, 0, 1], [-1, -1, 2]]
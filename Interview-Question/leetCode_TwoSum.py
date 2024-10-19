# ------------------------------------question

# Given an array of integers nums and an integer target, return indices of the two numbers such that
#  they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same 
# element twice.


# -----------------------------------solution

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
sol = Solution()
result = sol.twoSum([2, 7, 11, 15], 9)
print(result)



# ------------------------or with best(time and space complexity)


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         # Dictionary to store the number and its index
#         lookup = {}
        
#         # Iterate over the list with both index and value
#         for i, num in enumerate(nums):
#             # Calculate the complement that would add up to the target
#             complement = target - num
            
#             # If complement is in the lookup, we have our solution
#             if complement in lookup:
#                 return [lookup[complement], i]
            
#             # Otherwise, add the number and its index to the lookup
#             lookup[num] = i

# # Example usage
# sol = Solution()
# result = sol.twoSum([2, 7, 11, 15], 9)
# print(result)  # Output: [0, 1]
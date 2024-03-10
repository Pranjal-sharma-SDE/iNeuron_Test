def fourSum(nums, target):
    nums.sort()
    result = []

     # Handle empty array or array with less than 4 elements
    if len(nums) < 4:
        return results

    for i in range(len(nums) - 3):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 2):
            # Skip duplicate values for the second element
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicate values for the third element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate values for the fourth element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

    return result

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)

nums2=[1,2,3,45,76,23]
target2 = 0
result2 = fourSum(nums2, target2)
print(result2)
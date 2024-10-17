
# If the number is the same as the number before, we have used it as a target already, continue.
# We always start the left pointer from i+1 because the combination of 0~ i has already been tried.
# Now we calculate the total:
# If the total is less than zero, we need it to be larger, so we move the left pointer.
# If the total is greater than zero, we need it to be smaller, so we move the right pointer.
# If the total is zero, then add it to our result
# We need to move the left and right pointers to the next different numbers, so we do not get repeating result.
# We do not need to consider i after arr[i] > 0 , since the sum of 3 positive will be always greater than zero.
# We do not need to try the last two since there are no rooms for l and r pointers.
# You can think of it as the last two have been tried by all others.

def three_sum(nums):
    index = 0
    nums.sort()
    result = []
    for index in range(len(nums) - 2):
        if nums[index] > 0:
             break
        if index > 0 and nums[index] == nums[index-1]:
            continue

        left, right = index + 1, len(nums) - 1
        while left < right:
            total = nums[index] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[index], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
    return result
               

            

if __name__ == "__main__":
    nums = [0, -1, 2, -3, 1]
    result = three_sum(nums)
    print(result)
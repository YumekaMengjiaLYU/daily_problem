import collections

def longest_consecutive(nums):
    # Declare longest_streak and initialize to 0.
    # Create a Hash Table of size n and add elements of the array in it.
    # Linearly iterate over the array and check if A[i] -1 exists
    #  If it does not exist, then it is the first element of its corresponding sequence. Check for consecutive numbers greater than A[i] in the hash table and keep on increasing curr_streak.
    #  If it does, then it is not the first element of its corresponding sequence. So, we can move to the next iteration.
    # Update longest_streak if curr_streak is bigger than it.
    # Return longest_streak. 
    nums_set = set(nums)
    longest_streak = 0
    for num in nums:
        if num - 1 in nums_set:
            continue
        else:
            j, current_streak = 1, 1
            while num + j in nums_set:
                current_streak += 1
                j += 1
        longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    result = longest_consecutive([100,4,200,1,3,2])
    print(result)
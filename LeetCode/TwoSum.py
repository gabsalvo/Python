def twoSum(nums, target):
    num_dict = {}

    for index, num in enumerate(nums):
        comple = target - num

        if comple in num_dict :
            return [num_dict[comple], index]
        num_dict[num] = index
    return None


# Test the function
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print("Indices:", result)  # Output should be [0, 1] or [1, 0]

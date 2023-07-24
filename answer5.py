def check_duplicates(nums):
    return len(nums) != len(set(nums))


print(check_duplicates([5,3,6,2]))

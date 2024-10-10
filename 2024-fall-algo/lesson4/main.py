def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    
    return -1

nums = [2, 5, 8, 13, 21, 27, 35]
print(binary_search(nums, 29))
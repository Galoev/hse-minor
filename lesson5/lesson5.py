def merge(nums1, nums2):
    result = []

    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    if i < len(nums1):
        result += nums1[i:]
    
    if j < len(nums2):
        result += nums2[j:]

    return result

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    
    m = len(nums) // 2
    
    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])

    return merge(left, right)

def quick_sort(nums):
    less = []
    equal = []
    greater = []

    if len(nums) > 1:
        middle = len(nums) // 2
        pivot = nums[middle]
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        
        left = quick_sort(less)
        right = quick_sort(greater)

        return left + equal + right
    else:
        return nums
    

if __name__ == "__main__":
    nums = [7, 3, 5, 4, 1, 2, 6, 8]
    print(nums)
    print(quick_sort(nums))
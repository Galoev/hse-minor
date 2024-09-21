def permutations(nums):

    if len(nums) == 1: # [3]
        return [nums] # [ [3] ]

    res = []

    for i in range(len(nums)):
        cur_num = nums[i] # 2

        left_nums = nums[:i] + nums[i+1:] # 1 3
        
        left_nums_permutations = permutations(left_nums) # permutations(1, 3) -> [[1, 3], [3, 1]]

        for permutation in left_nums_permutations: 
            res.append([cur_num] + permutation) # [ [2] + [1, 3] = [2, 1, 3],  [2] + [3, 1] = [2, 3, 1] ]

    return res

# n! 

def placements(some_nums, k):

    def backtrack(path, nums): 
        if len(path) == k:
            res.append(path.copy())
            return
        
        for i in range(len(nums)): # 2 3
            path.append(nums[i]) # 1
            left_nums = nums[:i] + nums[i+1:] # 3
            backtrack(path, left_nums) # [1, 2] [2, 3]
            path.pop() #
    
    res = [] # [1, 2]
    backtrack([], some_nums)
    return res

def combinations(nums, k):
    def backtrack(path, start):
        if len(path) == k:
            res.append(path.copy())
            return
        
        for i in range(start, len(nums)): # 1 2 3
            path.append(nums[i]) # 1
            backtrack(path, i+1) # 
            path.pop()

    res = []
    backtrack([], 0)
    return res

# n!/(n-k)!k!
# k = n
# n!/0!=n!


res = combinations([1, 2, 3], 2)
print(res)

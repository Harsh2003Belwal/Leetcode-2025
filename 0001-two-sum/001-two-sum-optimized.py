def two_sum(nums, target):
    mapping={}
    n = len(nums)
    for i,num in enumerate(nums):
        complement=target-num
        if complement in mapping:
            return[mapping[complement], i]
        mapping[num]=i
        
print(two_sum([1, 2, 4], 6)) 

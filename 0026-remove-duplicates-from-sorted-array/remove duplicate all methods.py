#method 1 using set()
num= [0,0,1,1,1,2,2,3,3,4]
unique=set(num)
x=list(unique)
x.sort()
print(len(x))

#method 2 using pop()

nums= [0,0,1,1,1,2,2,3,3,4]
i = 1
nums.sort()
while i < len(nums):
    if (nums[i] == nums[i - 1]):
        x=nums.pop(i)
    else:
        i += 1
print(len(nums))

#method 3 using 2 pointer

nums= [0,0,1,1,1,2,2,3,3,4]
nums.sort()
i,j=0,1
while i<=j and j<len(nums):
    if nums[i]==nums[j]:
        nums.pop(j)
        j+=1
    else:
        nums[i+1]=nums[j]
        i+=1
print(len(nums))
        
















def threeSum(nums):
        st = []
        n=len(nums)
        for i in range(n-1):
            for j in range(i + 1, n-1):
                for k in range(j + 1, n-1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        st.append(list(temp))
                        
        ans = [list(item) for item in st]
        return ans

z=threeSum([-1,0,1,2,-1,-4])
print(z)

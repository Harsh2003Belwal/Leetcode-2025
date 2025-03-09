def findMedianSortedArrays(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i = 0
    j = 0
    merged = []

    while i < n and j < m:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < n:
        merged.append(nums1[i])
        i += 1
    
    while j < m:
        merged.append(nums2[j])
        j += 1
    
    total_len = len(merged)
    
    if total_len % 2 == 1:
        return float(merged[total_len // 2])
    else:
        mid1 = total_len // 2
        mid2 = mid1 - 1
        return (merged[mid1] + merged[mid2]) / 2.0

result = findMedianSortedArrays([1, 3], [2])
print(result)

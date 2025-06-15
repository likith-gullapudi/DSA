def bisect_left(nums, target):
    # check is lessthan target
    lo, hi = 0, len(nums) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            ans = mid
            hi = mid - 1
    if ans==-1:
        return ans
    if nums[ans]==target:
        return ans
    return -1

def bisect_right(nums, target):
    # check is lessthan target
    lo, hi = 0, len(nums) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
            ans = mid
        else:

            hi = mid - 1
    if ans==-1:
        return ans
    if nums[ans]==target:
        return ans
    return -1
print(bisect_right([1,1,1,1],0))
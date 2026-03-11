def minimumPenalty(nums,maxOperations):
    left=1
    right=max(nums)
    while left<right:
        mid=(left+right)//2
        ops=0
        for x in nums:
            ops+=(x-1)//mid
        if ops>maxOperations:
            left=mid+1
        else:
            right=mid
    return left
nums=list(map(int,input().split()))
maxOperations=int(input())
print(minimumPenalty(nums,maxOperations))

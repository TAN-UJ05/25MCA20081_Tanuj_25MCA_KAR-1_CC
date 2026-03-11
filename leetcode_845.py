def longest_mountain(arr):
    n=len(arr)
    ans=0
    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            l=r=i
            while l>0 and arr[l]>arr[l-1]:
                l-=1
            while r<n-1 and arr[r]>arr[r+1]:
                r+=1
            ans=max(ans,r-l+1)
    return ans
arr=list(map(int,input().split()))
print(longest_mountain(arr))

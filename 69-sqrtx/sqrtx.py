class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        ans=0
        while l<=r:
            mid1=(l+r)//2
            if mid1*mid1<=x:
                ans=mid1
                l=mid1+1
            else:
                r=mid1-1 
        return int(ans)                      
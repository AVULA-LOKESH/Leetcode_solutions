class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        maxi=0
        while l<r:
            b=r-l
            c=min(height[l],height[r])
            maxi=max(maxi,b*c)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxi              
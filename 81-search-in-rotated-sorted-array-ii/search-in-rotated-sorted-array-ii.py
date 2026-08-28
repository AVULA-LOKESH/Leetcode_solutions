class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if target==nums[mid]:
                return True
            if nums[l]==nums[mid]:
                l+=1
                continue
            if nums[l]<nums[mid]:
                if target<=nums[mid] and target>=nums[l]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if target>=nums[mid]  and  target<=nums[h]:
                    l=mid+1
                else:
                    h=mid-1
        return False
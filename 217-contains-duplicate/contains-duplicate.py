class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        b={}
        for i in range(0,len(nums)):
            b[nums[i]]=b.get(nums[i],0)+1
            if b[nums[i]]>1:
                return True
        return False                           
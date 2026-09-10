class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map={0:-1}
        prefix=0
        for i,num in enumerate(nums):
            prefix+=num
            rem=prefix%k
            if rem in remainder_map:
                ind=i-remainder_map[rem]
                if ind>=2:
                    return True
            else:
                remainder_map[rem]=i        
        return False            
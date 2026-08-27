class Solution:
    def isPalindrome(self, x: int) -> bool:
        c=0
        b=0
        temp=x
        while(x>0):
            b=x%10
            c=c*10+b
            x=x//10
        if temp==c:
            return True
        else:
            return False         
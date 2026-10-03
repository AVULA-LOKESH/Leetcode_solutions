class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b={}
        c={}
        for ch in s:
            b[ch]=b.get(ch,0)+1
        for ch in t:
            c[ch]=c.get(ch,0)+1
        if b==c:
            return True
        else:
            return False                           
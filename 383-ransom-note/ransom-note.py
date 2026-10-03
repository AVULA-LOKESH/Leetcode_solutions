class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        b={}
        c={}
        for ch in magazine:
            b[ch]=b.get(ch,0)+1
        for ch in ransomNote:
            c[ch]=c.get(ch,0)+1
            if ch not in b or c[ch]>b[ch]:
                return False
        for i in c:
            if i not in b:
                return False
        return True                    
                              
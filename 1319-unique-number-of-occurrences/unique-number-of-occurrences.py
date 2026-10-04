class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        b={}
        for i in range(0,len(arr)):
            b[arr[i]]=b.get(arr[i],0)+1
        c=[]    
        for i in b:
            if b[i] in c:
                return False
            c.append(b[i])
        return True    
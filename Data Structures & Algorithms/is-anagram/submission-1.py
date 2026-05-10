class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s)==len(t):
            return False
        for i in range(len(s)):
            if s[i] in t:
                t = t.replace(s[i],"",1)
            else:
                return False
        
        if t=="":
            return True
        else:
            return False
            
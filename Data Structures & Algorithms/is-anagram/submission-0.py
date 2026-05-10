class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for letter in s:
            if letter in t:
                t=t.replace(letter,"",1)
        
        if t=="":
            return True
        else:
            return False
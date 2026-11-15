class Solution:
    def isPalindrome(self, s: str) -> bool:
        text ="".join(c for c in s if c.isalnum()).lower()
        i=0
        j=len(text)-1
        while i<=j:
            if text[i]!=text[j]:
                return False
            i+=1
            j-=1
        return True

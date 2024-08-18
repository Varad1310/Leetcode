import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        c=s.lower()
        new_string = "" 
        for char in c: 
            if char not in string.punctuation: 
                new_string += char 
        a=new_string.replace(' ','')
        b=a[::-1]
        return a==b

##A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers'''
##Given a string s, return true if it is a palindrome, or false otherwise.
class solution(object):
    def isapalindrome(self,s):
        left=0
        right=len(s)-1
        while (left<right):
            while (left<right) and not s[left].alnum():
                left=left+1
            while (left<right) and not s[right].alnum():
                right=right-1
            if s[left].lower()!=s[right].lower():
                return False
            right-=1
            left+=1
        return True
            
            
    
class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while(left<right):
            word=s[left]
            s[left]=s[right]
            s[right]=word
            left=left+1
            right=right-1
        
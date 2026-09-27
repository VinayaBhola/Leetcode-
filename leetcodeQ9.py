'''Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise'''
class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Reverse the number mathematically
        num, rev = x, 0
        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10   # integer division
        
        return rev == x

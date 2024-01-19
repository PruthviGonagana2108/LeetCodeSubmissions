class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        sum=0
        while x>0:
            k = x%10
            #print(k)
            sum = sum*10 + k
            x=x//10
        if sum == n:
            return True
        else:
            return False
        

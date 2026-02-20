class Solution:
    def isPalindrome(self,x: int) -> bool:
        
        if x < 0:
            return False

        digits = list(str(x))
        stack = []

        
        for d in digits:
            stack.append(d)

        
        for d in digits:
            if stack.pop() != d:
                return False

        return True

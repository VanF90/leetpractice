#Example 1:

#Input: s = "()"
#Output: true
#Example 2:

#Input: s = "()[]{}"
#Output: true
#Example 3:

#Input: s = "(]"
#Output: false


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    # Dictionary mapping opening brackets to closing brackets
        brackets = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in brackets:
                # Push the opening bracket onto the stack
                stack.append(c)
            else:
                # Check if the closing bracket is the correct one for the top element of the stack
                if not stack or brackets[stack.pop()] != c:
                    return False

            # Return True if the stack is empty (all brackets were paired correctly), False otherwise
        return not stack
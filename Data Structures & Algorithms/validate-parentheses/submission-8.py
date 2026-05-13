class Solution:
    def isValid(self, s: str) -> bool:
        
        # think
        # [](){}
        s = str(s)
        stack = []

        openBrackets={"]":"[",
              ")":"(",
              "}":"{"}

        # essentially we want to add all the open brackets to the stack. 
        # if we try to add a close bracket that doesn't match the TOP of the stack, it will return false
        # e.g. [(])
        if len(s)%2 != 0:  # if its odd it cant be true
            return False
        for i in range(len(s)):
            currentValue = s[i]
            if currentValue in openBrackets.values(): # if the value is an openBracket, then we can add it. 
                stack.append(currentValue)
            elif stack == [] and currentValue not in openBrackets.values(): # if stack is empty and tries to add ends
                return False
            elif stack[-1] == openBrackets[currentValue]: # if the top of the stack doesn't match the 
                stack.pop()
            else:
                return False
            """
            if i not in stack:
                stack.append(i)
            elif stack[-1] == values[s[i]]: #peak at top of stack
                return False
            """
        if stack != []: # stack SHOULD be empty by the time we're done with the algorithm
            return False
        else:
            return True

            
            
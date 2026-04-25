def removeSubstring(s: str, k: int)-> str:
    # Stack stores pairs of (character, count)
    stack = []
    
    for char in s:
        if char == '(':
            if stack and stack[-1][0] == '(':
                stack[-1] = (stack[-1][0], stack[-1][1] + 1)
            else:
                stack.append(['(', 1])
        else: # char == ')'
            if stack and stack[-1][0] == ')':
                stack[-1] = (stack[-1][0], stack[-1][1] + 1)
            else:
                stack.append([')', 1])
            
            # Check for and remove k-balanced pattern from the top
            if len(stack) >= 2 and stack[-1][0] == ')' and stack[-2][0] == '(' and stack[-2][1] >= k:
                stack.pop()
                stack[-1] = (stack[-1][0], stack[-1][1] - k)
                
                if stack[-1][1] == 0:
                    stack.pop()
            elif stack and stack[-1][0] == ')' and stack[-1][1] > k and stack[-2][0] == '(' and stack[-2][1] >= k:
                pass
    
    result = []
    for char, count in stack:
        result.append(char*count)
    return "".join(result)

s: str = str(input("Enter the value of s: "))
k: int = int(input("Enter the value of k: "))
print(removeSubstring(s=s, k=k))
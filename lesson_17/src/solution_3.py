def bracket_balance(skob: str) -> bool:
    stack = []
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]
    matching_brackets = {")": "(", "]": "[", "}": "{"}
    
    s = []
    for i in range(len(skob)):
        s.append(skob[i])

    for bracket in s:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or stack[-1] != matching_brackets[bracket]:
                return False
            stack.pop()
    
    return len(stack) == 0

print(bracket_balance('{)[][)}'))
print(bracket_balance('{([])}'))
print(bracket_balance('}'))
print(bracket_balance('[]['))
print(bracket_balance(')('))

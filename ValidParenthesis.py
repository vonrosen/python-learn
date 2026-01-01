def isValid(self, s: str) -> bool:
    stack = []
    valid_opening_chars = { '(': ')', '[': ']', '{': '}' }
    valid_closing_chars = { value: key for key, value in valid_opening_chars.items() }

    for i in range(0, len(s)):
        if s[i] in valid_opening_chars:
            stack.append(s[i])
        elif s[i] in valid_closing_chars:
            if len(stack) > 0 and stack[-1] == valid_closing_chars[s[i]]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
def generateParenthesis(n):
    result = []
    stack = []
    def recursion(left, right):
        if left == right == n:
            result.append("".join(stack))
            return
        if left < n:
            stack.append("(")
            recursion(left + 1, right)
            stack.pop()
        if right < left:
            stack.append(")")
            recursion(left, right + 1)
            stack.pop()
    recursion(0, 0)
    return result

print(len(generateParenthesis(6)))

expression = input("Digite uma expressão com parênteses: ")

stack = []

for char in expression:
    if char == '(':
        stack.append('(')
    elif char == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")
from Stack import Stack, StackEmptyError

input = input()
stack = Stack()
isBalanced = True

for char in input:
    if(char == '[' or char == '('):
        stack.push(char)
    elif(char == ']' or char == ')'):
        try:
            initial = stack.pop()
            if((initial == '[' and char == ')') or (initial == '(' and char == ']')):
                isBalanced = False
                break
        except StackEmptyError:
            isBalanced = False
            break

print(1 if(isBalanced and stack.isEmpty()) else 0)
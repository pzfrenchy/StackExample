#Python implementation of a stack data structure.
#Stack works on a last in first out order using push and pop commands.

def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item) 
    #stack has maximum size, exceeding causes stack overflow
    #logic for checking size would be included here but n/a in python

def pop(stack):
    if len(stack) > 0: #check stack has items, avoids stack underflow
        stack.pop()
    else:
        print('stack empty')

stack = createStack()
print(stack)
pop(stack)
push(stack, 'Bob')
push(stack, 'Dougie')
push(stack, 'Sue')
print(stack)
pop(stack)
print(stack)

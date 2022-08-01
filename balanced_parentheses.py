#Program to verify if an expression contaning parentheses ["(","{","[",")","}","]"] is valid.
#Pass an input string and check if the string has balanced parentheses.
# ({[]}) => Balanced
# ([)]{} => Unbalanced
# (){}[] => Balanced
# [(){[]}] => Balanced
# {[](} => Unbalanced

#Using Stack

op = ["[", "(", "{"]
cl = ["]", ")", "}"]

#Function to check balance using Stack
def stack_check(pstr):
    stack = []
    popped = []
    for i in pstr:
        #print("Checking: ", i)
        if i in op:         #If opening parentheses, push to stack.
            stack.append(i)
            #print("Pushed: ", i)
            #print("Stack: ", stack)
        elif i in cl:       #If closing parentheses, stack must not be empty and
            pos = cl.index(i)   #the closing parentheses should match it's opening parenthesis.
            if (len(stack) > 0) and (op[pos] == stack[-1]):
                popped.append(stack.pop())
                #print("Popped: ", popped[-1])
                #print("Stack: ", stack)
            else:
                break
    if len(stack) == 0:     #If stack == empty, then string = balanced.
        print("Balanced")
    else:
        print("Unbalanced")

pstr = "{()([])}"
#pstr = "[{}{})(]"
#pstr = "((()"
#pstr = "[{}{}]"
print("Original String: " + pstr)

stack_check(pstr)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)
    
/// Second  Approach
def simplifyPath(self, path):
    stack = []
    for p in path.split('/'):
        if stack and p == '..':
            stack.pop()
        elif p not in ['.', '', '..']:
            stack.append(p)
    return '/' + '/'.join(stack)
/// Third Approach
def simplifyPath(self, path):
    stack = []
    for p in path.split('/'):
        if p == '..':
            if stack:
                stack.pop()
        elif p and p != '.':
            stack.append(p)
    return '/' + '/'.join(stack)

/// Fourth Approach
def simplifyPath(self, path: str) => str:
    stack = []
    cur = ''
    
    for c in path + "/":
        if c == "/":
            if cur == "..":
                if stack: stack.pop()        
            elif cur !="" and cur != ".":
                stack.append(cur)
            cur = ""
        else:
            cur += c
    return "/" + "/".join(stack)

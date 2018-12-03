# Create a Stack (s)
# TOS : Top Of Stack
# Two operations: Push, pop
# Push(s,item) : (Check Overflow) s[++TOS] = item  
# Pop(s) : (Check Underflow) item = s[TOS--]

def push(vstack,item):
    vstack.append(item)
    
def pop(vstack):
    item = vstack[len(vstack) - 1]
    del vstack[len(vstack) - 1]
    return item

s=[]
push(s,'Pen')
push(s,'Pencil')
push(s,'Eraser')
print s
print pop(s)
push(s,'Marker')
print s
print pop(s)

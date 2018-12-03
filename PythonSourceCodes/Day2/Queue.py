# Queue
# Insertion occurs at the rear end
# Deletion occurs at the frond end

def insert(vqueue,item):
    vqueue.insert(0,item)
    
def delete(vqueue):
    return vqueue.pop()
    
    
q=[]
insert(q,'Television')
insert(q,'VCR')
insert(q,'Smartphone')
print q
print delete(q)
print q
insert(q,'Tablet')
print q
print delete(q)
print q

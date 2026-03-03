def h_index(citation):
    n = len(citation)
    count = [0] * (n + 1)
    
    for c in citation:
        if c >= n:
            count[n] += 1
        else:
            count[c] += 1
            
    total = 0
    for h in range(n, -1, -1):
        total += count[h]
        if total >= h:
            return h
        
    return 0


print(h_index([3,0,6,1,5]))                     #3
print(h_index([1,3,1]))                         #1
print(h_index([0,0,0,0]))                       #0
print(h_index([100,200,300,400,500]))           #5
print(h_index([4,4,0,0]))                       #2        
print(h_index([2,2,2,2]))                       #2
print(h_index([1,2,100]))                       #2
print(h_index([0,1,2,5,6]))                     #2
print(h_index([11,15,17,20]))                   #4
print(h_index([0,1,4,4,4,5,7]))                 #4
print(h_index([1,1,1,1,1,1]))                   #1
print(h_index([5,5,5,5,1]))                     #4
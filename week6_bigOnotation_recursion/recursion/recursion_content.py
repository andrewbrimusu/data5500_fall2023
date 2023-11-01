################### 
# Recursion example - print numbers 1 to 1000

pi = [3,1,4,1,5,9,2,6,5,8] # 9 items

i = 0
    
def function1(pi, i):
    
    print(pi[i]) # one item in the loop
    i += 1
    
    if i == len(pi):
        return
    
    function1(pi, i)
    
    
function1(pi, i)


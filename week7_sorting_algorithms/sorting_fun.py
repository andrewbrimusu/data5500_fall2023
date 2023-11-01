lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# print(lst.sort())

# awesome code

# swap the 3 and the 1

print(lst[0])
print(lst[1])

# braden jessie betsy swapping algorithm
tmp = lst[0]
lst[0] = lst[1]
lst[1] = tmp

(lst[0], lst[1]) = (lst[1], lst[0])




print(lst) # everything is now sorted
# 1,1,2,3,4,5,6,9
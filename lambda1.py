# def quad(a,b,c):
#     return lambda x:a*x**2 + b*x + c

# f = quad(2,3,-9)

# print(f(0))
# print(f(4))
# print(f(3))


#=======================================================

# Map 
a=[1,2,3,4,5,6,7,8,9]

newList = list(map(lambda x:x+5, a))  #this will print a new list with 5 added to each ele

print(newList) # output --[6, 7, 8, 9, 10, 11, 12, 13, 14]


#filter
newList1 = list(filter(lambda x:x%2 == 0, a)) #filters out even values
print(newList1) #output - [2, 4, 6, 8]

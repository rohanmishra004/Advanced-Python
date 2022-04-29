#we are finding iter, iterators and others
nums =[1,2,3]

i_nums = iter(nums)

while True:
    try:
        item = next(i_nums)
        print(item)

    except StopIteration:
        break


#the above code will work exactly how a for loop works beneath 

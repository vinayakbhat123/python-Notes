# List comprahension

# synatax => 
# [expression for value in iterable if condition]

# [print(x*2 ,end=" ") for x in range(1,10)]
# numbers= [1,-3,4,5,-1,-4,-1,-3]
# [print(num) for num in numbers if num>0]


#if else condition
# result = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]
# print(result)


# nested list 
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

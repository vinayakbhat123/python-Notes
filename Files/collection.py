#collections   => single variable to used to store multiple values
#List = [] ordered and changable. Dublicates OK
#set = {}  unordered and immutable.but ADD/REMOVE OK.No dublicates 
#tuple = () ordered and unchangle Dublicates OK  FASTER then List



         #List =[]

#fruits =["apple","banana","mango","orange"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print(fruits[0:3])
# fruits[0] = "Grapes"
# fruits.append("grapes")  =>   # ['apple', 'banana', 'mango', 'orange', 'grapes']
# fruits.remove("orange") 
# fruits.insert(3,"apple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("orange"))
# print(fruits.count("orange"))
# print(fruits)
# for i in fruits:
#   print(i)


        #set = {}
# fruits ={"apple","banana","mango","orange","banana"}        #cannot use indexing in set
# fruits.add("grapes")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# print(fruits)

        #tuple()  
fruits =("apple","banana","mango","orange","banana" )
print(fruits)
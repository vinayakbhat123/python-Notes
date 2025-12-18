import time 

#default arguments
def count(start=1,end=5):
  for i in range(start,end+1):
    print(i)
    time.sleep(1)

count()


#positional Args
def count(start,end):
  for i in range(start,end+1):
    print(i)
    time.sleep(1)

count(1,5)
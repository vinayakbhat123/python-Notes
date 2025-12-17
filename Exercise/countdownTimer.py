#count down timer
import time
timer = int(input("Enter the Time"))
 
for a in range(timer,0,-1):
   seconds = a % 60
   minutes = int(a/60)%60
   hours = int(a/3600)
   print(f"{hours}:{minutes}:{seconds}")
   time.sleep(1)
   

print("Times Up")
temps = [[0.0 for h in range(24)] for d in range(31)] # Hourly matrix in a month filled with zero degrees

# determine the monthly average noon temperature⬇️⬇️

temps=[[0.0 for h in range(24)] for d in range(31)]
# 
# the list filled with degrees that measured during days or hours here
# 

total=0.0

for day in temps:
  total+=temps[11] #temps[11] indicates the noon value
average=total/31

print("Average temperature at noon:", average)

# highest temperature during the whole month⬇️⬇️

temps=[[0.0 for h in range(24)]for d in range(31)]
# 
# the list filled with degrees that measured during days or hours here
# 
highest=-100.0

for d in temps:
  for temp in day:
    if temp>highest:
      highest=temp
print("The highest temperature was:", highest) 

# count the days when the temperature at noon was at least 20 degrees⬇️⬇️

temps=[[0.0 for h in range(24)]for d in range(31)]
# 
# the list filled with degrees that measured during days or hours here
# 
hot_days=0
for day in temps:
  if day[11]>20.0:
    hot_days+=1
print(hot_days, "days were hot.")    
    
    






       

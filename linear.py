hours=[0,1,2,3,3,5,5,5,6,7,7,10]
marks=[96,85,82,74,95,68,76,84,58,65,75,50]
# total no. of observation
n=len(hours)
sum_xy=0
sum_x=0
sum_y=0
sq_x=0

for i in range(0,len(hours)):
    sum_xy+=hours[i]*marks[i]
    sum_x+=hours[i]    
    sum_y+=marks[i]   
    sq_x+=hours[i]**2
  
neum=(n*sum_xy)-(sum_x*sum_y)
deno=(n*sq_x)-(sum_x**2)
m=neum/deno
print(m)


c=(sum_y/12)-m*(sum_x/12)


print("9 hours of watching tv",m*9+c)




  







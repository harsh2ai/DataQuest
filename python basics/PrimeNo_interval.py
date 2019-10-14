startRange = 11
endRange = 25
  
for val in range(startRange, endRange + 1): 
 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 

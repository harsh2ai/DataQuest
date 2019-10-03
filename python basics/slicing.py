# lst contains all number from 1 to 10 
lst = range(1, 11) 
print lst 
#Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
#  below list has numbers from 2 to 5 
lst1_5 = lst[1 : 5] 
print lst1_5 
#Output : [2, 3, 4, 5]
  
#  below list has numbers from 6 to 8 
lst5_8 = lst[5 : 8] 
print lst5_8 
#Output : [6, 7, 8]
  
#  below list has numbers from 2 to 10 
lst1_ = lst[1 : ] 
print lst1_ 
#Output : [2, 3, 4, 5, 6, 7, 8, 9, 10]
  
#  below list has numbers from 1 to 5 
lst_5 = lst[: 5] 
print lst_5 
#Output : [1, 2, 3, 4, 5]
  
#  below list has numbers from 2 to 8 in step 2 
lst1_8_2 = lst[1 : 8 : 2] 
print lst1_8_2 
#Output : [2, 4, 6, 8]
  
#  below list has numbers from 10 to 1 
lst_rev = lst[ : : -1] 
print lst_rev 
#Output : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  
#  below list has numbers from 10 to 6 in step 2 
lst_rev_9_5_2 = lst[9 : 4 : -2] 
print lst_rev_9_5_2 
#Output : [10, 8, 6]

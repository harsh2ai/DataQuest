def shellSort(arr): 
  

    n = len(arr) 
    gap = n/2
  
 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap /= 2
  
  

arr = [ 12, 34, 54, 2, 3] 
  
n = len(arr) 
print ("Array before sorting:") 
for i in range(n): 
    print(arr[i]), 

'''
pattern

*
**
***
****
*****
'''
i=1
while i<=5:
	print('*'*i)
	i+=1

#for space in between the programs
print("\n \n")

'''
pattern

*****
****
***
**
*
'''
i=5
while i>=1:
	print('*'*i)
	i-=1

'''
pattern

    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
print('\n \n ')
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("* ", end=' ')
    print(" ")


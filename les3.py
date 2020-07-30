#EX4
#a=0
#for i in range(1000, 2300 , 1):
   #if (i % 5 == 0) and (i % 7 == 0):
       # a +=i
     
#print(a)


#EX5
a=("Viorel 13 4 pavel")

length = len(a)
digit = 0
letters = 0
others = 0
for i in a:
    if i.isalpha():
        letters += 1
    elif i.isnumeric():
        digit += 1
    else:
        others += 1
    
print("Number of string character is", letters)
print("Numbers of Int is ", digit)
print("Others", others)
print(length, "Lenth ")
 
 
  
          
  
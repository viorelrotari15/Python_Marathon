
#EX1
#def farinhate(cels ,far):
  # return cels/5 , far-32/9
  
#a = farinhate(100 , 100)
#print(a)
#EX2
def polidrome(mystr): 
  
      
    for i in range(0, int(len(mystr)/2)):  
        if mystr[i] != mystr[len(mystr)-i-1]:
            
            return False
    return True
  

s = "maam"
ans = polidrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No") 



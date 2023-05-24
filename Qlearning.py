import random
def reward(value):
    return -1*(value**2)

n=int(random.randint(0,100))
minvalue=0
valueOfVariables=[]
vOVariable=1
while 0<n:
 value=[]
 value.append(int(random.randint(-100,100)))
 state=[]
 i=0
 a=True
 
 while a :
  if(reward(value[i])<reward(value[i]+1)):
      state.append("arttır")
      value.append(value[i]+1)
      i+=1
  elif(reward(value[i])<reward(value[i]-1)):
      state.append("azalt")
      value.append(value[i]-1)
      i+=1
  else:
     state.append("Min Değer")
     a=False

 x=0
 print("x",vOVariable,"^2",sep="",end="")
 print("minimize edilmiş halinin Q-tablosu\n")
 vOVariable+=1
 print("Değer          Aksiyon \n")
 
 while x<(i+1):
     print(value[x], "          " ,state[x])
     x+=1
 print("")
 valueOfVariables.append(value[i])
 minvalue+=value[i]
 n-=1

vOVariable=1
i=0

while i<len(valueOfVariables):
   print("x",vOVariable,"^2",sep="",end=" = ")
   print(valueOfVariables[i])
   vOVariable+=1
   i+=1

print("x1^2+x2^2+x3^2+…….+xn^2 fonksiyonunu minimize etmemiz sonucunda ",minvalue," değerini elde ederiz.")





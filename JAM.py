"""def loop_forfun():
    get_string= input("entervalue:,")
    return list(get_string)


#get_string= input("entervalue:,")

k=loop_forfun()
print(k)"""


""""
rows=5
for i in range(rows+1):
      for j in range(i):
            print(i,end="")
      print("")
"""""






""""
def Alphabet(n):
      num = 65
      for i in range(0,n):
          for j in range(0,i+1):
               ch=chr(num)
               print(ch,end="")
               j+=j
          num+=1
          print("\r")

      #num+=1
      #j=0


print(Alphabet(5))


"""


#a=2007/7

#print(a)



#a= list[for i in range(2000,3201):if(i%7==0)and(i%5!=0): print(i,end=",")]

l=[]

for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        l.append(i)
print(len(l))
print(l)

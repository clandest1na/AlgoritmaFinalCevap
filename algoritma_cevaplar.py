#Github bağlantısı ----> https://gist.github.com/clandest1na/9e152ecb369be43550b79808b4674fb2

#SORU1
c=input ("Bir tarih girin:")
e=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
m = (c.split("-"))
i= 1
while i<=12:
    if(i>=10):
        if(m[1] == str(i)):
            print (m[0]+" "+e[i-1]+" "+m[2])
    else:
         if(m[1] == "0"+str(i)):
            print (m[0]+" "+e[i-1]+" "+m[2])
    i=i+1

#SORU2
def firstCase(e):
    m=0
    for i in range(0,e):
         m=m+(i+1)*2
    return m
def factorial (t):
    a = 1
    for i in range(1,t+1):
        a = a*i
    return 3*a

c=int(input("N DEĞERİNİ GİRİN : "))
if c>=9 and c<16:
    print(firstCase(c))
if c>=0 and c<9:
    print(factorial(c))
else:
    print("HATALI GİRİŞ..")

#SORU3
matris={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

x = [[1,2,-1],  
       [2,5,2],  
       [-1,-2,2]]  
 
y = [[3,5,13],  #cemtatlic
      [20,1,20],  
      [12,9,3]]
 
deger = [[0,0,0],
               [0,0,0],  
              [0,0,0]]
 
for c in range(len(x)):  
   for e in range(len(y[0])):
       for m in range(len(y)):  
           deger[c][e] += x[c][m] * y[m][e]
for t in deger:
   print(t)

#SORU4
c=[] #Boş bir liste tanımladım.
for e in range(1,10): 
   if e > 1:  
       for m in range(2,e):  
           if (e % m) == 0:  
               break  
       else:
           c.append(e)
print(c)
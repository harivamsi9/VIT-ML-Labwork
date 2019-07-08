#This Code for multiple Regression is authored by 17BCE0525
X1=[45,50,55,70,75,75,85]
X2=[25,35,45,55,65,75,85]
X3=[31,28,32,32,29,27,31]
#ASSUMED_MEANS
X1bar=65
X2bar=55
X3bar=30
U1=[];U2=[];U3=[]
U1U2=[];U1U3=[];U2U3=[]
U1sq=[];U2sq=[];U3sq=[]
for i in range(len(X1)):
    U1.append(X1[i]-X1bar)
    U2.append(X2[i]-X2bar)
    U3.append(X3[i]-X3bar)
    U1U2.append(U1[i]*U2[i])
    U1U3.append(U1[i]*U3[i])
    U2U3.append(U2[i]*U3[i])
    U1sq.append(U1[i]**2)
    U2sq.append(U2[i]**2)
    U3sq.append(U3[i]**2)
d=sum(U2sq)*sum(U3sq)-(sum(U2U3)**2)
b12_3=round(((sum(U1U2)*sum(U3sq)-sum(U1U3)*sum(U2U3))/d),3)
b13_2=round(((sum(U2sq)*sum(U1U3)-sum(U2U3)*sum(U1U2))/d),3)
print("\nThe values of b12_3 and b13_2 are: ")
print("b12_3: "+str(b12_3) + "\t"+"b13_2: "+ str(b13_2))
a1_23=round(X1bar-(b12_3*X2bar+b13_2*X3bar),3)
print("\nTHE MULTIPLE LINEAR REGRESSION EQUATION IS: ")
print("X1bar= "+str(a1_23)+" + "+str(b12_3)+"*X2bar + " +str(b13_2)+"*X3bar")
print("\nFor X2= 60 and X3= 25: \nThe value of Yield is: ")
print(a1_23+b12_3*60+b13_2*25)
print("Rg. No: 17BCE0525")

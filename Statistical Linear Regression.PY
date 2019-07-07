X=[12,15,15,23,24,38,42,48]
Y=[5,5.6,5.8,7,7.2,8.8,9.2,9.3]
XY=[]
X2=[]
sumX=0
sumXY=0
sumY=0
sumX2=0
n=len(X)
if len(X)!=len(Y):
    print("ENTER EQUAL NO. OF VALUES FOR BOTH X AND Y.")
else:
    for i in range(len(X)):
        pd=float(X[i])*float(Y[i])
        XY.append(pd)
        sumX+=float(X[i])
        sumY+=float(Y[i])
        sumXY+=pd
        X2.append((float(X[i])**2))
        sumX2+=(float(X[i])**2)
numerator=((sumXY/n)-(sumX/n)*(sumY/n))
denominator=((sumX2/n)-(sumX/n)**2)
bYX=round(numerator/denominator,3)
print(XY)
print(X2)

print("\nbYX= "+ str(bYX))
c=round((sumY/n)-bYX*(sumX/n),3)
print("C= "+str(c))
print("THE FINAL EQUATION IS: ")
print("Y= "+str(bYX)+"X + "+str(c))
print("RG.NO 17BCE0525")
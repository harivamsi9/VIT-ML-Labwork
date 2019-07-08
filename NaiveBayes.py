print("RG.NO: 17BCE0525")
Age=['<=30','<=30','31-40','>40','>40','>40','31-40','<=30','<=30','>40','<=30','31-40','31-40','>40']
Income=['High','High','High','Medium','Low','Low','Low','Medium','Low','Medium','Medium','Medium','High','Medium']
Student=['No','No','No','No','Yes','Yes','Yes','No','Yes','Yes','Yes','No','Yes','No']
Credit_Score=['Fair','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Fair','Fair','Excellent','Excellent','Fair','Excellent']
Buying_Decision=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
T=input("ENTER THE TUPLE(SEPARTING EACH COLUMN BY COMMA): \n").split(",")
p_of_c1=Buying_Decision.count("Yes")
p_of_c2=Buying_Decision.count("No")
#print(p_of_c1)
#print(p_of_c2)
print(T)
cnt1=0
cnt2=0
cnt3=0
cnt4=0
cnt11=0
cnt22=0
cnt33=0
cnt44=0
for i in range(len(Age)):
    if( Age[i]==T[0] and Buying_Decision[i]=='Yes'):
        cnt1+=1
    if( Income[i]==T[1] and Buying_Decision[i]=='Yes'):
        cnt2+=1
    if( Student[i]==T[2] and Buying_Decision[i]=='Yes'):
        cnt3+=1
    if( Credit_Score[i]==T[3] and Buying_Decision[i]=='Yes'):
        cnt4+=1
    if( Age[i]==T[0] and Buying_Decision=='No'):
        cnt11+=1
    if( Income[i]==T[1] and Buying_Decision[i]=='No'):
        cnt22+=1
    if( Student[i]==T[2] and Buying_Decision[i]=='No'):
        cnt33+=1
    if( Credit_Score[i]==T[3] and Buying_Decision[i]=='No'):
        cnt44+=1
if(cnt1==0):
    cnt1=1
if(cnt11==0):
    cnt11=1
if(cnt2==0):
    cnt2=1
if(cnt3==0):
    cnt3=1
if(cnt4==0):
    cnt4=1
if(cnt22==0):
    cnt22=1
if(cnt33==0):
    cnt33=1
if(cnt44==0):
    cnt44=1
#print(str(cnt1)+' '+str(cnt11)+' '+str(cnt2)+' '+str(cnt22)+' '+str(cnt3)+' '+str(cnt33)+' '+str(cnt4)+' '+str(cnt44))
p_of_Tdivc1=(cnt1*cnt2*cnt3*cnt4)/(p_of_c1**4)
p_of_Tdivc2=(cnt11*cnt22*cnt33*cnt44)/(p_of_c2**4)
p_of_c1divT=p_of_Tdivc1*p_of_c1
p_of_c2divT=p_of_Tdivc2*p_of_c2
print(round(p_of_c1divT,3))
print(round(p_of_c2divT,3))
if(p_of_c1divT>p_of_c2divT):
    print("THE DECISION IS YES!")
else:
    print("THE DECISION IS NO!")
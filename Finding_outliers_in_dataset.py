#let the column we want to check the outlier for is: age (2nd column in X)

a=x[:,1]
a=np.array(a)
a=np.sort(a)
q1=int((len(a)+1)/4)
q3=int(0.75*(len(a)+1))
iqr=0
count=0
lower_limit=0
higher_limit=0
for i in a:
    count=count+1
    if count==q3:
        iqr=count
        higher_limit=i
    elif count==q1:
        iqr=iqr-count
        lower_limit=i    
higher_limit=higher_limit+1.5*iqr
lower_limit=lower_limit-1.5*iqr
print("data should lie within: ",higher_limit)
print("data should lie above: ",lower_limit)
count=0
for i in a:
    if i>higher_limit:
        count=count+1
print("so, no. of outliers found are: ",count)

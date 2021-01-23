
def letter(str):
    #dstr=str()
    #print(type(dstr))
    dstr=""
    for i in str:
        if((i>='a') and (i<='z')):
            #i=chr(ord(i)+1)
            i=chr(ord(i)+1)
            dstr=dstr+i
            if(dstr=='a' or dstr=='e' or dstr=='i' or dstr=='o' or dstr=='u'):
                dstr=dstr.upper()
        elif((int(i)>=0) and (int(i)<=9)):
            dstr=dstr+i
    print("incremented string: ",dstr)
a=input("Enter a string: ")
letter(a)


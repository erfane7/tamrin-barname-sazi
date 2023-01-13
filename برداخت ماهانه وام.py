#mohasebe pardakht vam
#erfan eslami kahriz
#kelas sunday 7:45

vam=eval(input("mablagh vam : "))
sood=eval(input("sood vam : "))
sal=int(input("sal : "))

def mounthly(a,b,c):
    if b==0:
        mo=a/c
        
    else:
        mo=(a*(b*(1+b)**c))/(((1+b)**c)-1)
    return mo


        
print (mounthly(vam,sood,sal))
    

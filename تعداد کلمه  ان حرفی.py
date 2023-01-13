#tedad kalame n harfi
#erfan eslami kahriz
#kelas sunday 7:45

c=0

def word_count(str,a):
    c=0
    counts = dict()
    words = str.split()
    

    for word in words:
        if len(word)==a:
           c += 1
       

    return c


erfan=input("enter sentence : ")
a=int(input("enter number : "))


print( word_count(erfan,a))

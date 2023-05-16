import pyperclip
n=int(input("\nenter the length : "))
loop=True
while(loop==True):
    c=str(input("\nenter the comment: "))
    m=n/2
    m=m-(len(c)/2)
    m=m-1
    comment="#"
    i=0
    while(i<n):
        if i<m:
            comment=comment+"-"
            i=i+1
        elif i<(m+len(c)):
            comment=comment+c
            i=m+len(c)
        else:
            comment=comment+"-"
            i=i+1
    comment="\n"+comment+"\n"
    print(comment)
    pyperclip.copy(comment)
    boolean=input("\nanother comment ? (y/n) ")
    if boolean=="n" or boolean=="N":
        loop=False

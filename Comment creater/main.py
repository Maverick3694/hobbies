
"""
The program generates comment template for commenting python programs.
By taking comment values and length of comment template.
eg: 
#----------------------------------------------comment------------------------------------------------
Here comment length is 100 characters and value is "comment".
Subsequently the comment is copied to clipboard.
"""
#-----------------------------------------------START-------------------------------------------------

import pyperclip

n=int(input("\nenter the length : "))
loop=True
while(loop==True):
    c=str(input("\nenter the comment: "))
    if len(c)>(n-2):
        print("\n ! The length of comment value is larger than the template Value")
        n=int(input("\nenter new length : "))
        continue
    m=n/2
    m=m-(len(c)/2)
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

#-----------------------------------------Copy to clipboard-------------------------------------------

    pyperclip.copy(comment)

#---------------------------------------------Loop Bool-----------------------------------------------

    boolean=input("\nanother comment ? (y/n) ")
    if boolean=="n" or boolean=="N":
        loop=False

#------------------------------------------------END--------------------------------------------------


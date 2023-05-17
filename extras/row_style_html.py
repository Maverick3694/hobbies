"""
Function to style the html table of dataframe with alternative row colors
"""
import pandas as pd
def color_alternating_rows(val):
            temp=""
            i=0
            b=True
            while(i<len(val)):
                if val[i]=="<" and val[i+1]=="t" and val[i+2]=="r": 
                    if b==True:
                        color="#EEEEEE"
                        b=False 
                    else:
                        color="#FFFFFF"
                        b=True                  
                    temp=temp+"<tr"+" "+'style="background-color:'+color+'"'+" "
                    i=i+3             
                else:
                    temp=temp+val[i]
                    i=i+1
            return temp


df = pd.DataFrame({'Name': ['John', 'Jane', 'Alice'],
        'Age': [25, 30, 28],
        'City': ['New York', 'Paris', 'London']})
color_alternating_rows(df.to_html(index=False))

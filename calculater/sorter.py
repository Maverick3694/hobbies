def fn(data):
    newlis=[]
    num=['1','2','3','4','5','6','7','8','9','0','.']
    i=0
    while(i<len(data)):
        
        if data[i] in num:
            
            j=i
            n=""
            while(j<len(data)):
                if data[j] in num:
                    n=n+str(data[j])
                                                                    
                    j=j+1
                    if j==len(data):
                        newlis.append(float(n))
                        
                        return newlis
                if data[j] not in num:
                    newlis.append(float(n))
                    i=j
                    break
                                
        
        elif data[i] not in num:
            if i+1==len(data):
                    newlis.append(data[i])
                    return newlis
            newlis.append(data[i])
            i=i+1
            

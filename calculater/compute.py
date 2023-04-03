from math import sqrt
def fn(data,operands):
    for i in range(0,len(data)):
        if i==0 and data[i]!="√":
            last=float(data[i])
            result=last
        if data[i] in operands:
            if data[i]=="+":
                result=last+float(data[i+1])
            elif data[i]=="-":
                result=last-float(data[i+1])
            elif data[i]=="*":
                result=last*float(data[i+1])
            elif data[i]=="/":
                result=last/float(data[i+1])
        if data[i] in ["(",")","√"]:
            if data[i]=="√":
                sq=sqrt(float(data[i+1]))
                if i!=0:
                    if data[i-1] in operands:
                        if data[i]=="+":
                            result=last+float(sq)
                        elif data[i]=="-":
                            result=last-float(sq)
                        elif data[i]=="*":
                            result=last*float(sq)
                        elif data[i]=="/":
                            result=last/float(sq)
                    else:
                        result=last*sq
                else:
                    result=sq
            if data[i]=="(":
                temp=[]
                x=i
                i=i+1
                while(data[i]!=")"):
                    temp.append(data[i])
                    i=i+1
                for j in range(0,len(temp)):
                    if j==0 and temp[j]!="√":
                        l=float(temp[j])
                        result=l
                    if temp[j] in operands:
                        if temp[j]=="+":
                            result=l+float(temp[j+1])
                        elif temp[j]=="-":
                            result=l-float(temp[j+1])
                        elif temp[j]=="*":
                            result=l*float(temp[j+1])
                        elif temp[j]=="/":
                            result=l/float(temp[j+1])
                    if temp[j]=="√":
                        sq=sqrt(float(temp[j+1]))
                        if j!=0:
                            if temp[j-1] in operands:
                                if temp[i]=="+":
                                    result=l+float(sq)
                                elif temp[j]=="-":
                                    result=l-float(sq)
                                elif temp[j]=="*":
                                    result=l*float(sq)
                                elif temp[j]=="/":
                                    result=l/float(sq)
                            else:
                                result=l*sq
                        else:
                            result=sq

                if data[x] in operands:
                    if data[i]=="+":
                        result=last+float(result)
                    elif data[i]=="-":
                        result=last-float(result)
                    elif data[i]=="*":
                        result=last*float(result)
                    elif data[i]=="/":
                        result=last/float(result)

                elif data[x]=="√":
                    sq=sqrt(float(result))
                    if x!=0:
                        if data[x-1] in operands:
                            if data[i]=="+":
                                result=last+float(sq)
                            elif data[x]=="-":
                                result=last-float(sq)
                            elif data[x]=="*":
                                result=last*float(sq)
                            elif data[x]=="/":
                                result=last/float(sq)
                        else:
                            result=last*sq
                    else:
                        result=sq
                else:
                    result=last*float(result)
        last=result
    return result


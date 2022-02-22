b=[]
ValueString = ""


def ListBinaryToInt(b):
    ValueString = ''.join(str(elem) for elem in b)
    ValueString.replace(" ", "")
    a = int(ValueString, 2)
    return(a)

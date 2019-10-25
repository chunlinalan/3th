def print_string(*arg1,sep=" ",end="\n"):
    _str=str()
    for i in range(len(arg1)-1):
        _str+=str(arg1[i])+sep
    _str+=str(arg1[len(arg1)-1])
    return _str+end
    
        
print(print_string("this","is","a","test"))

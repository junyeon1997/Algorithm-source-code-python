def solution(dartResult):
    num=''
    array=[]
    for i in dartResult:
        if i.isdigit(): 
            num+=i
        if i.isalpha():
            array.append(int(num))
            num=''    
        if i == 'S':
            pass
        elif i=='D':
            array[-1]**=2
        elif i=='T':
            array[-1]**=3
        elif i=='*':
            if len(array)==1:
                array[-1]*=2
            else:
                array[-2]*=2
                array[-1]*=2
        elif i=='#':
            array[-1]*=(-1)
        
    return sum(array)
def is_harshad(n):
    temp=n
    val=0
    while  temp > 0:
        val+=temp%10
        temp=temp//10
        
    if(n%val==0):
        return True
    else:
        return False

if __name__=='__main__':
    print(is_harshad(12))
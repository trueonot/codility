

def solution(N):
    result = 0
    cnt = -1
    
    while N>0:
        x = int(N%2)
        if(x == 1):
            #stat count
            if result < cnt:
                result = cnt
            cnt = 0
        else:
            if cnt != -1:
                cnt+=1
        N = int(N/2)
            
    return result



if __name__ == '__main__':
    N = 2048
    res = solution(N)
    print("result is " , res)
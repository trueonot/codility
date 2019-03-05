def solution(A):
    result = 1
    net = set()

    for n in A:
        if n>=0:
            net.add(n)
        
    for idx in range(len(net)):
        if (idx+1 in net):
            result+=1
        else:            
            break
    
    return result



if __name__ == "__main__":
    print("-----------------------------------")
    print(solution([1, 3, 6, 4, 1, 2]  )) 
    print("-----------------------------------")
    print(solution([1, 2, 3]   )) 
    print("-----------------------------------")
    print(solution([-1, -3]  )) 
    print("-----------------------------------")
    print(solution([1]  )) 
    print("-----------------------------------")
    print(solution([0]  )) 
    print("-----------------------------------")
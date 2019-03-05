def solution(A):
    result = 1
    net = set()

    for n in A:
        net.add(n)
    
    for idx in range(len(A)):
        
        if not(idx+1 in net):
            result = 0
            break

    

    return result



if __name__ == "__main__":
    print(solution([4, 1, 3, 2]  )) 
    print(solution([4, 1, 3]  )) 
    print(solution([1, 1]))
def solution(A):
    result = 1
    ln = len(A)
    lr = [0] * ln
    rl = [0] * ln
    optimal = 999999

    for idx in range(ln):
        lr[idx] = lr[idx-1]+A[idx]
        rl[ln-idx-1] = rl[(ln-idx)%ln]+A[ln-idx-1]
    
    for idx in range(ln-1):
        print(idx, lr[idx], rl[idx+1])
        if(abs(lr[idx] - rl[idx+1]) < optimal):
            optimal = abs(lr[idx] - rl[idx+1])

    result = optimal

    return result



if __name__ == "__main__":
    print(solution([3, 1, 2, 4, 3] )) 
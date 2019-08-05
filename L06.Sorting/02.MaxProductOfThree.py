def solution(A):
    # write your code in Python 3.6
    result = 0
    ln = len(A)
    net = sorted(A, key=lambda x: abs(x), reverse=True)
    
    cnt = 0
    res1 = 1
    res2 = 1
    for a in net:
        if a < 0:
            cnt += 1
        
        res2 *= a
        res1 *= a
        
            

        
    result = res1
    return result


if __name__ == "__main__":
    print(solution([-3, 7, 2, 8, 6, 6] ))
    print(solution([-5, 5, -5, 4]  ))
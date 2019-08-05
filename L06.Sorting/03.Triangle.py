def solution(A):
    result = 0


    n = len(A)

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                a = A[i]
                b = A[j]
                c = A[k]
                if c<a+b and b<a+c and a<b+c:
                    result = 1
                    break
            if result == 1:
                break
        if result == 1:
            break
        
            

    return result


if __name__ == "__main__":
    print(solution([10, 2, 5, 1, 8, 20]))
    # print(solution([10, 50, 5, 1]))
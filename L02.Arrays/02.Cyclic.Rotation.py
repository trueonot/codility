def solution(A, K):
    n = len(A)
    result = [0] * n
    for i in range(0, n):
        j = (i + (n-K) % n)% n
        result[i] = A[j]
    return result



if __name__ == "__main__":
    A = [1, 2, 3, 4]
    K = 4
    print(solution([3, 8, 9, 7, 6],0))
    print(solution([3, 8, 9, 7, 6],1))
    print(solution([3, 8, 9, 7, 6],2))
    print(solution([3, 8, 9, 7, 6],3))
    print(solution([3, 8, 9, 7, 6],4))
    # print(solution([0, 0, 0],1))
    # print(solution([1, 2, 3, 4],0))
    # print(solution([1, 2, 3, 4],1))
    # print(solution([1, 2, 3, 4],2))
    # print(solution([1, 2, 3, 4],3))
    # print(solution([1, 2, 3, 4],4))
    # print(solution([1, 2, 3, 4],5))
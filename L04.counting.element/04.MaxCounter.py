


def solution(N, A):
    result = [0] * N
    max = 0
    for step in A:
        if step > N:
            result = [max] * N
        else:
            result[step-1] = result[step-1]+1
            if max < result[step-1]:
                max = result[step-1]
    
    return result


if __name__ == "__main__":
    A = [0] * 7
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
    N = 5
    result = solution(N, A)
    print(result)
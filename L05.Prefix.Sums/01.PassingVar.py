
def solution(A):
    # write your code in Python 3.6
    result = 0
    ln = len(A)
    net = [0] * ln

    cnt = 0
    for idx, a in enumerate(A[: : -1]):
        if a == 1:
            cnt+=1
        net[(ln-idx-1)%ln] = cnt

    cnt = 0
    for idx, a in enumerate(A):
        if a == 0:
            cnt += net[idx]

    if cnt > 1000000000 :
        result = -1
    else:
        result = cnt
    return result


if __name__ == "__main__":
    print(solution([0, 1, 0, 1, 1] ))
    print(solution([0] ))
    print(solution([1] ))
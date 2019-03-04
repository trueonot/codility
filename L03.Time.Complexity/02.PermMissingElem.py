def solution(A):
    result = 1
    net = set()
    for n in A:
        net.add(n)

    for n in net:
        if result == n:
            result+=1
        else:
            break

    return result



if __name__ == "__main__":
    print(solution([2, 3, 1, 5])) 
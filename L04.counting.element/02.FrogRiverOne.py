def solution(X, A):
    result = -1
    net = set()
    time = -1
    for idx, n in enumerate(A):
        print(idx, n, X, net)
        if n <= X:
            net.add(n)
            time = idx
        if X == len(net):
            break
    if X == len(net):
        result = time

    return result



if __name__ == "__main__":
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]  )) 
    print(solution(2, [1]  )) 
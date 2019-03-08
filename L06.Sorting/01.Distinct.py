# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    result = 0
    net = set()

    for a in A:
        if not(a in net):
            net.add(a)

    result = len(net)
    return result


if __name__ == "__main__":
    print(solution(  [2, 1, 1, 2, 3, 1] ))
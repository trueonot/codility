# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    result = 0

    for i in range(0,n):
        for j in range(i+1, n):
            if A[i] + A[j] >= j-i:
                print(i, j, A[i], A[j])
                result += 1
    return result

if __name__ == "__main__":
    print(solution([1, 5, 2, 1, 4, 0] ))
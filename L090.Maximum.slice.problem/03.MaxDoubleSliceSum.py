import sys

def solution(A):
    RES1 = [0] * len(A)
    RES2 = [0] * len(A)

    for idx, a in enumerate(A):
        a = a+ RES1[idx-1]
        RES1[idx] = a
    
    for idx, a in enumerate(A[::-1]):
        a = a + RES2[idx-1]
        RES2[idx] = a
    slice_max = -sys.maxsize-1
    RES2.reverse()
    
    for idx in range(1, len(RES2)-1):
        print(idx, RES1[idx-1], RES2[idx+1])
        cv = RES1[idx-1] + RES2[idx+1]
        slice_max = max(cv, slice_max)
    print(slice_max)
    print(float('-inf') > -sys.maxsize)
    print(-sys.maxsize - sys.maxsize- sys.maxsize)
    return 0


if __name__ == '__main__':
    A = [3, 2, 6, -1, 4, 5, -1, 2] 
    print(A)
    print(solution(A))
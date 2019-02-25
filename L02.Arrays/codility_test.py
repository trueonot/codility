# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    answer = 1
    map = set([])
    
    for n in A:
        if n > 0:
           map.add(n)
           
    pn = 0   
    for cn in map:
        if cn == pn +1 :
            pn = cn
        else:
            break



    return answer


if __name__ == "__main__":
    A = [1, 2, 3]
    A = [1, 3, 6, 4, 1, 2] 
    answer = solution(A)
    print("answer is : ", answer)
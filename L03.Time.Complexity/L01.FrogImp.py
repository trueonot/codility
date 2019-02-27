def solution(X, Y, D):
    result =((Y-X) // D)
    if(Y-X) % D > 0 :
        result += 1
    return result



if __name__ == "__main__":
    print(solution(0, 60, 30)) 
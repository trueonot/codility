

def solution(A):
    result = 0
    map = {}

    for n in A:
        try:
            if map[n] == n:
                #map[n] = 0
                map.pop(n)
            else:
                map[n] = n
        except KeyError:
            map[n] = n
            
            
    _, result = map.popitem()
    return result


if __name__ == "__main__":
    A = [9,9,3,9,3,9,7]
    print(solution(A))
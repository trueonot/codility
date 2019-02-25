def solution(S, P, Q):
    # write your code in Python 3.6
    result = [99] * len(P)
    letter = {'A':1, 'C':2, 'G':3, 'T':4}

    step = 0
    for p, q in zip(P, Q):
        string = S[p:q+1]
        for ch in letter:
            if ch in string:
                result[step] = letter[ch]
                break
        step += 1

    return result


if __name__ == '__main__':
    S = 'CAGCCTA'
    P = [2, 5, 0]
    Q = [4, 5, 6]
    result = solution(S, P, Q)
    print(result)
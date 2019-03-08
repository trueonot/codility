def solution(A):
    result = 0
    ln = len(A)
    netSum = [0] * (ln+1)
    netAvg = [999999999999] * ln
    netMin = 99999999999
    idxMin = 0

    cnt = 0
    for idx, a in enumerate(A):
        netSum[idx+1] += (netSum[idx] + a)
    
    for idxP in range(ln):
        sumP = netSum[idxP]
        for idxQ in range(idxP+2, ln, 1):
            sumQ = netSum[idxQ]
            tempAvg = (sumQ - sumP) / (idxQ - idxP+1)
            
            #print(idxP, idxQ, sumP, sumQ, tempAvg)
            if(netAvg[idxP] > tempAvg):
                netAvg[idxP] = tempAvg
    
    
    for idxP, a in enumerate(netAvg):
        if( a < netMin):
            netMin = netAvg[idxP]
            idxMin = idxP

    # print(A) 
    # print(netSum)
    # print(netAvg)
    # print(netMin)
    result = idxMin
    return result

if __name__ == "__main__":
    print(solution([4, 2, 2, 5, 1, 5, 8] ))
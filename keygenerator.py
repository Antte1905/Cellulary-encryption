import Binary
import copy

def GenerateKey(LongMax): #please use odd numbers
    Long = [0]*LongMax
    Long[LongMax//2] = 1
    Long2 = copy.deepcopy(Long)

    for x in range((LongMax // 2)-4):
        for i in range(LongMax):
            if i > 0 and i < LongMax-1:
                if Long[i-1] + Long[i] + Long[i+1] == 0 or Long[i-1] + Long[i] + Long[i+1] == 3 or Long[i-1] + Long[i] == 2 or Long[i-1] + Long[i+1] == 2:
                    Long2[i] = 0
                else :
                    Long2[i] = 1
        Long = copy.deepcopy(Long2)
    return(Binary.ListBinaryToInt(Long))

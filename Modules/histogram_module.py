def makeHistogramFromList(input: list) -> dict:
    ret = {}
    for i in input:
        if i not in ret.keys():
            ret[i] = 1
        else:
            ret[i] += 1
    return ret

def getHistogramSize(histogram: dict) -> int:
    return len(dict.keys())
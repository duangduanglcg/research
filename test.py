from clu.HClustering import hierarchicalClustering
from clu.metrics import *
from clu.REI import *

def compute_wordColumnSum(file):
    '''
    计算word中表格一列数字之和
    :param file:
    :return:
    '''
    with open(file) as f:
        lines = f.readlines()
        sum = 0
        cnt = 0
        for line in lines:
            line = line.strip('\t')
            line = float(line)
            cnt += 1
            sum += line
    return round(sum/cnt, 2)




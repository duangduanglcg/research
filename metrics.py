import sys
from tqdm import tqdm
import  numpy as np


def sequences_process(file):
    '''
        将源文件转为序列列表
        去掉长度为1的序列
        去掉重复的序列
        :param file:
        :return: sequences list
        '''
    with open(file) as f:
        lines = f.readlines()
        sequence_calls = []
        for line in lines[6:]:
            line = line.strip('\n').split(',')[1].strip('\'').split(' ')
            for i in range(len(line)-1, 0, -1):
                if line[i] == line[i - 1]:
                    del line[i]
            if len(line) > 1:
                res = ' '.join(line)
                if res not in sequence_calls:
                    sequence_calls.append(res)
    return sequence_calls



def creat_ngram(seq):
    '''
    构造序列的3-grams列表
    :param seq:
    :return:3-grams列表
    '''
    n2_grams = []
    n3_grams = []
    seq_split = seq.split(' ')
    n1_grams = seq_split
    for i in range(len(n1_grams) + 1):
        j = i + 1
        if j > len(n1_grams) - 1:
            break
        else:
            n2_grams.append(' '.join((seq_split[i], seq_split[j])))
    for i in range(len(n1_grams) + 1):
        j = i + 2
        if j >len(n1_grams) - 1:
            break
        else:
            n3_grams.append(' '.join(((seq_split[i], seq_split[i + 1], seq_split[j]))))
    n_grams = n1_grams + n2_grams + n3_grams
    return n_grams


def sequence_sim(x, y):
    '''
    计算两序列间的相似度
    :param x: sequence x
    :param y: sequence y
    :return: similarity
    '''
    grams_x = creat_ngram(x)
    grams_y = creat_ngram(y)
    cnt = 0
    for i in range(len(grams_x)):
        if grams_x[i] in grams_y:
            cnt += 1
    similarity = round((2 * cnt)/(len(grams_x) + len(grams_y)), 4)
    # distance = round(sqrt(1 - similarity**2), 4)
    distance = round(1 - similarity, 4)
    return abs(distance)



def distance_list(sequence_list):
    '''
    生成距离列表（暂时不用该方法）
    :param sequence_list:
    :return:distance
    '''
    dis = []
    for i in range(len(sequence_list)):
        for j in range(i+1, len(sequence_list)):
            dis.append(sequence_sim(sequence_list[i], sequence_list[j]))
    return dis


def compute_similarity(data_file):
    '''
    生成相似度矩阵
    :param data_file:
    :return:
    '''
    sequence_calls = sequences_process(data_file)
    dist_mat = np.zeros((len(sequence_calls), len(sequence_calls)))
    for i in range(len(sequence_calls)):
    # for i in tqdm(range(len(sequence_calls))):
        for j in range(i + 1):
            dist_mat[i][j] = sequence_sim(sequence_calls[i], sequence_calls[j])
            dist_mat[j][i] = dist_mat[i][j]
    # return np.triu(dist_mat)
    return dist_mat


def compute_averageLinkage(l1, l2):
    cnt = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            cnt += sequence_sim(l1[i], l2[j])
    dis = cnt / (len(l1) * len(l2))
    return round(dis, 4)


def compute_singleLinkage(l1, l2):
    dis = 1
    for i in range(len(l1)):
        for j in range(len(l2)):
            if sequence_sim(l1[i], l2[j]) < dis:
                dis = sequence_sim(l1[i], l2[j])
    return round(dis, 4)

def compute_completeLinkage(l1, l2):
    dis = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if sequence_sim(l1[i], l2[j]) > dis:
                dis = sequence_sim(l1[i], l2[j])
    return round(dis, 4)


def result_create(name):
    '''
    将print结果保存到文本中
    :param name:
    :return:
    '''
    result_path = 'D:/develop/python_workspace/clu/'
    full_path = result_path + name + '.arff'
    file = open(full_path, 'w')

# file_name = 'weld'
# result_create(file_name)
# output = sys.stdout
# output_file = open('D:/develop/python_workspace/clu/preprocessing-api/' + file_name + '.arff', 'w')
# sys.stdout = output_file
# data = 'api-file/weld.arff'
# api = sequences_process(data)
# for i in range(len(api)):
#     print(api[i], file=output_file)
# output_file.close()















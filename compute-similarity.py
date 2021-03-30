from clu.metrics import *


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

def compute_averageLinkage(l1, l2):
    cnt = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            cnt += sequence_sim(l1[i], l2[j])
    dis = cnt / (len(l1) * len(l2))
    return round(dis, 4)


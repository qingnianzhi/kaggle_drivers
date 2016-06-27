#!/usr/bin/env python2
#coding:utf-8


import numpy as np


def merge_several_folds_mean(data, nfolds):
    a = np.array(data[0])
    for i in range(1, nfolds):
        a += np.array(data[i])
    a /= nfolds
    return a.tolist()


def merge_several_folds_geom(data, nfolds):
    a = np.array(data[0])
    for i in range(1, nfolds):
        a *= np.array(data[i])
    a = np.power(a, 1/nfolds)
    return a.tolist()

def read_csv(path =None):
    f = open(path)
    data_in = f.readlines()
    data_out = []
    labels = []
    for i in range(1,len(data_in)):
        tmp = []
        for j in range(10):
            tmp.append(float(data_in[i].split(',')[j]))
        #tmp.append(data_in[i].split(',')[10][:-1])
        labels.append(data_in[i].split(',')[10][:-1])
        data_out.append(tmp)
    return data_out,labels

def read_N_csv(path = None,nfolds=None):
    data_out = []
    labels_out = []
    for i in range(nfolds):
        data,labels = read_csv(path[i])
        data_out.append(data)
        labels_out = labels
    return data_out,labels_out


if __name__ == '__main__':
    path = ['1.csv','2.csv','3.csv','4.csv']
    data,labels = read_N_csv(path,len(path))
    #new_data = merge_several_folds_mean(data,len(path))
    new_data = merge_several_folds_geom(data, len(path))

    f = open('out.csv','w')
    f.write('c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,img\n')
    for i in range(len(new_data)):
        for j in new_data[i]:
            f.write(str(j))
            f.write(',')
        f.write(labels[i])
        f.write('\n')
    f.close()

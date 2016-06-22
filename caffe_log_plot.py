#!/usr/bin/env python2
#coding:utf-8


import re
import matplotlib.pyplot as plt

if __name__ == '__main__':

    re_iteration = re.compile('Iteration.+,')
    re_loss = re.compile('loss.+')
    train_iter = []
    train_loss = []

    #trian data
    f = open('./caffe.log')
    log = f.readlines()
    for i in log:
        if i.find('Iteration')>0 and i.find('loss')>0:
            train_iter.append(re.findall(re_iteration,i)[0][10:-1])
            train_loss.append(re.findall(re_loss,i)[0][7:])

    #test data
    flag = 0
    test_iter = []
    test_loss1 = []
    test_loss2 = []
    test_loss3 = []
    re_loss1 = re.compile('loss1/loss1.+\(')
    re_loss2 = re.compile('loss2/loss1.+\(')
    re_loss3 = re.compile('loss3/loss3.+\(')
    for i in log:
        if flag == 0 and i.find('Iteration') > 0 and i.find('Testing') > 0:
            flag = 1
            test_iter.append(re.findall(re_iteration,i)[0][10:-1])
        if flag == 1 and i.find('loss1/loss1') > 0:
            test_loss1.append(re.findall(re_loss1,i)[0][14:-2])
        if flag == 1 and i.find('loss2/loss1') > 0:
            test_loss2.append(re.findall(re_loss2, i)[0][14:-2])
        if flag == 1 and i.find('loss3/loss3') > 0:
            flag = 0
            test_loss3.append(re.findall(re_loss3, i)[0][14:-2])

    #plot curve
    plt.plot(train_iter[5:], train_loss[5:], 'k')
    plt.plot(test_iter, test_loss1, 'r')  # valid
    #plt.plot(test_iter, test_loss2, 'g')
    #plt.plot(test_iter, test_loss3, 'b')
    plt.show()


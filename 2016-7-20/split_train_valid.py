#!/usr/bin/env python2
#coding:utf-8

import sys
import os
import random

if __name__ == '__main__':

  boundary = int(sys.argv[1])
  f = open('./all.txt')
  data = f.readlines()
  f.close()
  
  a = int(boundary*len(data)*0.125)
  b = int((boundary+1)*len(data)*0.125)
  print 'Boundary:',a,',',b
  
  f = open('./valid.txt','w')
  for i in data[a:b]:
    f.write(i)
  f.close()
  
  f = open('./train.txt','w')
  for i in data[0:a]:
    f.write(i)
  for i in data[b:]:
    f.write(i)
  f.close()
  print 'OK'  
  
  
import os

if __name__ == '__main__':
    f0 = open('./test.txt','w')
    f1 = open('./test_label.txt','w')
    file = os.listdir("./test/")
    for i in file:
      path0 = i
      path1 = './test/' + i
      f0.write(path0)
      f0.write('\n')
      
      f1.write(path1)
      f1.write('\t')
      f1.write('0')
      f1.write('\n')
    f0.close()
    f1.close()
    print 'OK'

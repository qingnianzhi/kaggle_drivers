#!/usr/bin/env sh
# train with imagenet pretrain model
python get_driver_train_valid_label.py 2
for x in 0 1 2 3 4 5 6 7  
do
  python split_train_valid.py $x
  mkdir ./model/log/log$x
  ~/caffe/build/tools/caffe train --gpu=0 --solver=./model/solver.prototxt --log_dir=./model/log$x --weights=./model/bvlc_googlenet.caffemodel
  mkdir ./model/model$x
  cp -rf ./model/googlenet/* ./model/model$x/
done
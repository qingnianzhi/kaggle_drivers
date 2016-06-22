#!/usr/bin/env sh
./get_features ./model/test.prototxt ./model/googlenet/_iter_50000.caffemodel prob1,prob2,prob3 test.txt

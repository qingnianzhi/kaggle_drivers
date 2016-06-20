2016/6/20
1:修改训练集合交叉验证集，按照不同人物来分割（通过get_driver_train_valid_label.py实现）
//TODO
2：修该特征提取代码，读取googleNet三层输出，根据多输出获取结果（方法有待考虑）
3：测试resize和crop的方法，之前是resize成方形再crop，这里对图像的长宽比例做了修改，对图像的平移性有不好的影响。
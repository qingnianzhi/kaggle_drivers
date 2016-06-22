#include <caffe/caffe.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <algorithm>
#include <iosfwd>
#include <memory>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <fstream>
#include "boost/algorithm/string.hpp"

using namespace caffe;  // NOLINT(build/namespaces)
using std::string;


int main(int argc, char** argv) {

	const int num_required_args = 5;
	if (argc < num_required_args) {
		LOG(ERROR) <<
			"This program takes in a trained network and then extract features of the net.\n"
			"Usage: get_features XXX.prototxt XXX.caffemodel XXXfeature_blob,YYYfeatre_blob XXX.txt\n"
			"Note: the last parameter is the txt save image names.\n";
		return 1;
	}
	string model_file = argv[1];	//prototxt
	string trained_file = argv[2];	//caffemodel
	//
	const int num_mini_batches = 312;    //�ܶ��ٴ�,����batch_sizeѡ���������
	boost::shared_ptr<Net<float> > feature_extraction_net(new Net<float>(model_file, caffe::TEST));
	Caffe::set_mode(Caffe::GPU);
	feature_extraction_net->CopyTrainedLayersFrom(trained_file);
	std::string extract_feature_blob_names(argv[3]);	//fc7,prob �������
	std::vector<std::string> blob_names;
	boost::split(blob_names, extract_feature_blob_names, boost::is_any_of(","));
	const int num_features = blob_names.size();			//��ȡ���ٸ�������֮ǰ�������һ����ȡ�����������
	// Check if the feature blob exist
	for (size_t i = 0; i < blob_names.size(); i++) {
	CHECK(feature_extraction_net->has_blob(blob_names[i]))
		<< "Unknown feature blob name " << blob_names[i]
		<< " in the network " << model_file;
	}
	std::cout << "Extracting Features";

	std::vector<std::vector<std::vector<float> > > output(num_features);
	std::vector<float> tmp;	
	for (int batch_index = 0; batch_index < num_mini_batches; ++batch_index) {
		std::cout<<batch_index<<std::endl;	//������е��ڼ���batch

		feature_extraction_net->Forward();
		for (int i = 0; i < num_features; ++i) {    //num_features ��ȡ��������ĸ���
			const boost::shared_ptr<Blob<float> > feature_blob = feature_extraction_net->blob_by_name(blob_names[i]);//���Ҫ��ȡ�������ָ��
			int batch_size = feature_blob->num();					//
			int dim_features = feature_blob->count() / batch_size;  //ÿ�����������ά��

			const float* feature_blob_data; //ָ��
			for (int n = 0; n < batch_size; ++n) {
				feature_blob_data = feature_blob->cpu_data() + feature_blob->offset(n);  //ÿ��batchƫ��һ��ָ��  ƫ����Ϊbatch_size*dim_feature
				tmp.clear();
				for(int d = 0;d<dim_features;++d){
					tmp.push_back(feature_blob_data[d]);
				}
				output[i].push_back(tmp);
			}  
		}  
	}  
	std::cout<< "Successfully extracted the features!";
	std::cout<<"output size:"<<output[0].size()<<std::endl;

	//д���ȡ������ֵ
	string img_name = argv[4];
	std::ifstream f(img_name.data(), ios::in);
	std::vector<string> imgs;
	string img;
	while (getline(f, img)){
		imgs.push_back(img);	
	}
	f.close();
	std::cout<<"imgs:"<<imgs.size()<<std::endl;
	for (int m = 0; m < num_features; ++m){
		string output_name = "./out_" + blob_names[m] + ".csv";
		std::ofstream out(output_name.data(), ios::out);
		out << "c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,img" << "\n";
		for (int i = 0; i<imgs.size(); ++i){
			for (int j = 0; j<output[m][i].size(); ++j){
				out << output[m][i][j] << ",";
			}
			out << imgs[i] << "\n";
		}
		out.close();
	}
	
	return 0;
}



#! /bin/bash

echo "hello bash"


basic_path = 'home/con/mmdetection'

echo $basic_path

file_name = "cascade_rcnn_r101_fpn_fp16_2x_thyroid_1215_4"

directory1 = $basic_path+"/tools/dist_test.sh configs/_used_/"
path = $directory+file_name+".py"
directory2 = $basic_path+"/work_dirs/"

values = 24 23 22 21




for v in values
do
path2 = $basic_path+file_name+"/epoch_"+$v+".pth"
# python .py /home/con/mmdetection/work_dirs/cascade_rcnn_r101_fpn_fp16_2x_thyroid_1215_4/epoch_22.pth 2 --out ./data/thyroid/outfile.json
python ${path} ${path2} $2 --out ./data/thyroid/outfile.json
done

python3 1_train-0819.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 20 --batch 128 --workers 4 --data_num 0
cp /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best.pth /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best_0.pth
python3 2_test_calc-0901.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 32 --batch 128 --workers 4 --data_num 0

python3 1_train-0819.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 20 --batch 128 --workers 4 --data_num 1
cp /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best.pth /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best_1.pth
python3 2_test_calc-0901.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 32 --batch 128 --workers 4 --data_num 1

python3 1_train-0819.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 20 --batch 128 --workers 4 --data_num 2
cp /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best.pth /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best_2.pth
python3 2_test_calc-0901.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 32 --batch 128 --workers 4 --data_num 2

python3 1_train-0819.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 20 --batch 128 --workers 4 --data_num 3
cp /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best.pth /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best_3.pth
python3 2_test_calc-0901.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 32 --batch 128 --workers 4 --data_num 3

python3 1_train-0819.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 20 --batch 128 --workers 4 --data_num 4
cp /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best.pth /home/ubuntu/con/code/BiT/runs/burn_R152x2_add1/best_4.pth
python3 2_test_calc-0901.py --name burn_R152x2_add1 --logdir runs --model BiT-M-R152x2 --datadir ./data/labels/ --imagedir ./data/images/ --batch_split 32 --batch 128 --workers 4 --data_num 4
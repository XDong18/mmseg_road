export CUDA_VISIBLE_DEVICES=0,1,2,3
PORT=29507 ./tools/dist_train.sh \
configs/dla/dla34up_road_80k.py 4 \
--work-dir ./out/dla34up_road_80k
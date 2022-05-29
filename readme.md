
# Hello

## Transforming Waymo to Coco

`python3 convert_waymo_to_yolo.py --tfrecord_dir ../waymo_sample/tfrecords --work_dir \
 ../waymo_sample --version_name sample --ann_filename sample.json --frame_index_ones_place 1`

## Testing
`python3 test.py --work_dir ../waymo_sample --version_name sample --id 2 --out_dir out`
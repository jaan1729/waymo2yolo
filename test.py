import os
import numpy as np 
import cv2
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--work_dir', required=True, type=str)
    parser.add_argument('--version_name', default=None, type=str)
    parser.add_argument('--id', required=True, type=int)
    parser.add_argument('--out_dir', default=None, type=str)
    
    args = parser.parse_args()
    
    
    text_file = os.path.join(args.work_dir, 'val2020.txt')
    os.makedirs(args.out_dir, exist_ok=True)
    with open(text_file) as f:
        image_list = f.readlines()
        image_list = [line.rstrip() for line in image_list]

    target = image_list[args.id]
    image = cv2.imread(os.path.join(args.work_dir, target[2:]))
    labels = np.loadtxt(os.path.join(args.work_dir, target[2:-3].replace('images', 'labels')+'txt'))
    height, width, _ = image.shape
    
    classes =['TYPE_VEHICLE', 'TYPE_PEDESTRIAN', 'TYPE_CYCLIST']   
    
    for label in labels:
        label*=[1,width,height,width,height]
        x1,y1,x2,y2 = int(label[1]-label[3]//2), int(label[2]-label[4]//2), int(label[1]+label[3]//2), int(label[2]+label[4]//2)
        cls = classes[0]
        image = cv2.rectangle(image, (x1,y1), (x2,y2), (36,255,12), 1)
        cv2.putText(image, cls, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    cv2.imwrite(args.out_dir +'/'+ target.split('/')[3], image)

    
if __name__ == "__main__":
    main()
import cv2
import numpy as np
from time import sleep
from tqdm import tqdm

sleep(10)
cap=cv2.VideoCapture(0)
cap.set(3, 1440)
cap.set(4, 1440)
print(0)
save_dir="/home/3M/test/dataset/"
for i in tqdm(range(101, 201)):
	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)
	cv2.imwrite(save_dir+'test'+str(i)+'.jpeg', frame)
	sleep(1)
cap.release()

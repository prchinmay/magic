# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 01:37:28 2022

@author: prchi
"""
import numpy as np
import cv2
from sklearn.cluster import KMeans
import pickle
import mediapipe as mp
from utils import Wave
import params

#Intialize mediapose objects
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

#Initialize params
param = params.get_general_params()
wave = Wave()

#Obtain pose data from Video feed 
cap = cv2.VideoCapture(param['vid_train'])
if cap.isOpened() == False:
    print("Error opening video stream or file") 
    #raise TypeError    
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
data = np.empty((frames, 33, 3)) 
frame_num = 0
while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break
    results= wave.get_pose(image, pose)
    landmarks = results.pose_world_landmarks.landmark
    for i in range(len(landmarks)):
        data[frame_num, i, :] = (landmarks[i].x, landmarks[i].y, landmarks[i].z)
    frame_num += 1
    
#K-Means Clustering to define intermediate steps in Wave action    
action = data.reshape(data.shape[0], data.shape[1]*data.shape[2])
kmeans = KMeans(n_clusters=param['n_clusters'], init ='k-means++',random_state=param['random_state'])
y_kmeans = kmeans.fit_predict(action)

#Save trained model using pickle
with open(param['model'], 'wb') as f:
    pickle.dump(kmeans, f)
print('Wave action reference saved at ' + param['model'])

pose.close()
cap.release()
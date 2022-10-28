# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 11:46:45 2022

@author: prchi
"""
import cv2
import pickle
import mediapipe as mp
from utils import get_thresh, annotate_vid, Wave
import params

#Intialize mediapose class
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

#Initialize params
param = params.get_general_params()
wave = Wave()

#Initialize videocapture and videowriter
cap = cv2.VideoCapture(param['vid_test'])
if cap.isOpened() == False:
    print("Error opening video stream or file")
    #raise TypeError
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
out = cv2.VideoWriter(param['vid_annotated'], 
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 
                      fps, (frame_width, frame_height))

#Load pickled K-Means model
with open(param['model'], 'rb') as f:
    kmeans = pickle.load(f)
threshold = get_thresh(kmeans)
    
#Start processing video
while cap.isOpened():
    ret, image = cap.read()
    if not ret:
        break
    results = wave.get_pose(image, pose)
    completion, reps = wave.get_status(results, kmeans, param, image, threshold)
    #annotate_vid(image, results, mp_pose, mp_drawing, out)
    
pose.close()
cap.release()
out.release()
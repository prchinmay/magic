# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:09:42 2022

@author: prchi
"""
import numpy as np
from numpy import dot
from numpy.linalg import norm
import cv2

def cosine_sim(a,b):
    """ 
    Get cosine similarity between two vectors .
    
    Args:
        a: array of dim (99,).
        b: array of dim (99,).
    Returns:
        Scalar value between [0,100]. 0=similar, 100=dissimilar. 
    """
    return np.sqrt(1 - np.abs(dot(a, b)/(norm(a)*norm(b))))*100

def get_thresh(kmeans):
    """ 
    Get threshold for deciding if current state has deviated reference action trajectory.
    
    Args:
        kmeans: trained clustering model object.
    Returns:
        Scalar value between [0,100].
    """
    a = kmeans.cluster_centers_[0]
    b = kmeans.cluster_centers_[1]
    return cosine_sim(a,b)
    
def annotate_vid(image, results, mp_pose, mp_drawing, out):
    """ 
    Get threshold for deciding if current state has deviated reference action trajectory.
    
    Args:
        image: input image dim (frame width, frame height).
        results: mediapipe pose results object.
        mp_pose: mediapipe object.
        mp_drawing: mediapipe object.
        out: cv2 video writer object.
        
    Returns:
        Scalar value between [0,100] 
    """
    image.flags.writeable = True
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    out.write(image)

class Wave(object):
    """
    A class to represent a Wave action.
    
    Attributes
    ----------
    reps : int
        counter to keep track of "Wave" action reps.
    arr : array(str)
        counter to keep track of percentage completion of current "Wave" action.
        
    Methods
    -------
    get_pose(image, pose): 
        Get pose data from image using MediaPipe.
    get_status(results, kmeans, param, image, threshold): 
        Get status of Wave action in video compared to reference action.
    
    """
    def __init__(self):
        self.reps = 0
        self.arr = []

    def get_pose(self,image, pose):
        """ 
        Get pose data from image using MediaPipe. 
    
        Args:
            image: input image dim (frame width, frame height).
            pose: mediapipe object.
        Returns:
            results: mediapipe pose results object.
            
        """
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        return pose.process(image)

    def get_status(self, results, kmeans, param, image, threshold):
        """ 
        Get status of Wave action in video compared to reference action. 
        
        Args:
            results: mediapipe pose results object.
            kmeans: trained clustering model.
            param: set of parameters defined in params.py.
            image: input image dim (frame width, frame height).
            threshold: threshold obtained from get_thresh().
        Returns:
            completion: int
                The % completion of the current ‘wave’ action.
            reps: int 
                The number of times a ‘wave’ has been completed.
                           
        """
        landmarks = results.pose_world_landmarks.landmark
        data=np.empty((len(landmarks), 3))
        
        for i in range(len(landmarks)):
            data[i, :] = (landmarks[i].x, landmarks[i].y, landmarks[i].z)  
            
        data = data.reshape(1, data.shape[0]*data.shape[1])
        clust = kmeans.predict(data)[0]
        sim_to_clust = cosine_sim(data, kmeans.cluster_centers_[clust])[0]
        
        if sim_to_clust>threshold:
            self.arr = []
            cv2.putText(image, "Action Incorrect!", (70, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, param['red'], 2)
        else:
            state = param['map'][clust]
            if len(self.arr)==len(param['seq']):
                self.reps+=1
                self.arr = []
            elif len(self.arr) == 0 or (self.arr[-1]!=state and state==param['seq'][len(self.arr)]):
                self.arr.append(state)
            else:
                pass
            cv2.putText(image, "Action Correctness : " + str(int(100-sim_to_clust)) + "%", 
                        (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, param['blue'], 2)
            
        completion = np.clip(((len(self.arr)-1)/(len(param['seq'])-1)),0,1)*100
        string = "Total Reps : " + str(self.reps) + "     " + "Curret Rep : " + str(completion) + "%"
        cv2.putText(image, string, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, param['green'], 4)
        print(string)    
        return completion,self.reps
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:47:53 2022

@author: prchi
"""

def get_general_params():
    """Input ouput paths for video files and other parameters
    
    """
    param = {}
    
    # Input and ouput paths 
    param['vid_train'] = "data/A.mp4"
    param['vid_test'] = "data/B.mp4"
    param['vid_annotated'] = "data/B_annotated.mp4"
    param['model'] = 'data/kmeans.pickle'
    
    # Other parameters
    param['map'] = {1:'start', 2:'mid', 0:'end'} # Mapping from k-means cluters to intermediate steps in action
    param['seq'] = ['start','mid','end','mid','start'] # Sequence of steps that constitute one full action

    # Select display colors for annotated video.
    param['red'] = (50, 50, 255)
    param['green'] = (127, 255, 0)
    param['blue']  = (255, 127, 0)
    
    # K-Means hyperparameters
    param['random_state'] = 0 
    param['n_clusters']= 3 # Translates to intermediate steps in an action  
    
    return param
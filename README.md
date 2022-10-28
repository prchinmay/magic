magic
=================

## Overview
This repository contains code for analyzing a user's pose to a given reference pose. These are the following Sections:

1. [File] - Details of files and directories in this repository)\
2. [Usage] - Step by step instructions to execute this code)\
3. [Explanation] - Reasoning behind the code)\

## 1. Files
`data/` - Folder containing reference and test videos. Also saves annotated video and clustering model here. \
`params.py` - Edit this file for changing paths. It also declares values of all parameters used in this solution. \
`define_action.py` - Code for defining "Wave" action based on reference Video. \
`monitor_action.py` - Process User provided Video and compare action with pre defined action. \
`console_output.mp4` - Screen recording of console output for `monitor_action.py`. \
`utils.py` - Wave action Class and member functions.
`requirements.txt` - Contains all package dependencies.
`README.md` - Readme file for this repository.

## 2. Usage

### Step 1: Clone repository
Open a linux terminal and clone this repository to your workspace using(copy paste entire thing):
```
git clone https://github.com/prchinmay/magic.git &
cd magic/

```

### Step 2: Create new virtual environment
Before intalling dependencies, let us first create a new virtual environment using(copy paste the entire thing):
```
python3 -m pip install --user virtualenv &
python3 -m virtualenv env &
source env/bin/activate
```

### Step 3: Install Dependencies
Install dependiencies using:
```
pip install -r requirements.txt

```

### Step 4: Run Codes

After dependencies are installed, run `define_action.py` to define "Wave" action from Video A. 
Run `monitor_action.py` to analyse frames from Video B and compare it with defined action in Video A.
```
python3 define_action.py &
python3 monitor_action.py

```
### Results
Total "Wave" action reps and percentage completion of current Wave action are printed to the console frame by frame. 
If `annotate_vid()` is enabled in `monitor_action.py`, then annotations of Video B is saved inside the `data` folder.
 

## 3. Explanation
This Section provides the reasoning behind the code utilised in this solution. 

### Defining the Wave action from Video A
This is performed in `define_action.py`. Pose data from all frames in Video A are extracted and stored in in variable `action` using `get_pose()` method. 
A simple K-Means clustering is performed on this data to define the action and identify the intermediate steps. The `n_clusters` hyperparameter gives the number of steps in the Wave action.
In this solution 3 steps are identified— 1)start, 2)mid, 3)end. "start" and "end" are extreme positions and mid is the intermediate position. If more intermediate steps are required, 
`n_clusters` can be defined appropriately. K-Means clustering was chosen for the following reasons:\

* speed: K-Means is one of the fastest ML algorithms especially for unsupervised data. This should work well for real time processing.\
* scalablity: K-Means scales well for large datasets for less number of clusters. It is expected that intermediate steps is less than 10 for any action.\
* data driven: Does not need manual supervision/ feature engineering. Intermediate steps is diveded into clusters without explicitly defining. 
Although it does allow a user to input priors(if required).\
* application: The intuition behind using clustering was the context provided by the assignment document. The fitness app guides a user to follow a reference action. 
An action typically should have intermediate "steps" which have to be achieved with a certain "accuracy". This is particularly the case for Yoga, weightlifting, pilates etc,. 
K-Means clustering identifies these steps as clusters of points having a cluster center. The cluster center corresponds to the ideal pose(that of the top athlete).\

Figure below shows a 2D PCA(Principal Component Analysis) projection of the poses in Wave action from Video A.\
![cluster](pics/cluster.png) 
![cosine](pics/cosine.png)
![thresh](pics/thresh.png)
![correct](pics/correct.png) 
![incorrect](pics/incorrect.png)   


  

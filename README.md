magic
=================

## Overview
This repository contains code for analyzing a user's pose to a given reference pose. The section Usage provides step by step instructions to execute this code. 
The Section Explanation provides the reasoning behind the code utilised in this solution.

## Files
`data/` - Folder containing reference and test videos. Also saves annotated video and clustering model here. \
`params.py` - Edit this file for changing paths. It also declares values of all parameters used in this solution. \
`define_action.py` - Code for defining "Wave" action based on reference Video. \
`monitor_action.py` - Process User provided Video and compare action with pre defined action. \
`console_output.mp4` - Screen recording of console output for `monitor_action.py`. \
`utils.py` - Wave action Class and member functions.
`requirements.txt` - Contains all package dependencies.
`README.md` - Readme file for this repository.

## Usage

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
If `annotate_vid()` is enabled in `define_action.py`, then annotations of Video B is saved inside the `data` folder.
 

## Explanation
This Section provides the reasoning behind the code utilised in this solution. 

### Defining the Wave action from Video A



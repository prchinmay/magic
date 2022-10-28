magic
=================

## Overview
This repository contains code for analyzing a user's pose to a given reference pose. The section Usage provides step by step instructions to execute this code. 
The Section Explanation provides the reasoning behind the code utilised in this solution.

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

After dependencies are installed, run `define_action.py` to define "Wave" action from video A. 
Run `monitor_action.py` to analyse frames from video B and compare it with defined action in A.
```
python3 define_action.py &
python3 monitor_action.py

```

## Explanation
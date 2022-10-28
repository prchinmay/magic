magic
=================

## Overview
This repository contains code for downloading 2000 non-person images from Google open image V6 dataset for object detection applications (https://storage.googleapis.com/openimages/web/index.html).

## Usage

### Step 1: Clone repository
Open a linux terminal and clone this repository to your workspace using(copy paste entire thing):
```
git clone https://github.com/prchinmay/nonpersons_data.git &
cd nonpersons_data

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

### Step 4: Run Code

After dependencies are installed, run this command in you linux terminal to generate non-persons ImageIDs, download those Images and generate labels in YOLOv3 format.
 
```
bash script.sh

```
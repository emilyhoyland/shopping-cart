# shopping-cart

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/emilyhoyland/shopping-cart) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd shopping-cart
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-cart":

```sh
conda create -n shopping-cart python=3.8
conda activate shopping-cart
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).


## Usage

Run the Python script:

```py
python shopping_cart.py

Follow commands as instructed.



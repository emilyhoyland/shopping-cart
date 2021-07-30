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

## Setup

In order to use the application in your local I.H.O.G., we will need to set up an environment to calculate local sales tax during the checkout process. In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your Location and Local Tax Rate (in decimal form). Make sure to SAVE the ".env" file aftwards:

    LOCATION=NY
    TAX_RATE=0.08875


## Usage

Run the Python script:

```py
python shopping_cart.py

Follow commands as instructed.



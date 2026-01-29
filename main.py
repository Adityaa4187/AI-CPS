# main.py
# Entry point of the whole project.
# Step 1: download raw dataset from GitHub using scrapping.py
# Step 2: Preprocessing the dataset removing the columns with less importance
# Step 3: Splitting the dataset into train, test, and activation dataset
# Step 4: Making the data ready for model training.

import os
import sys

from code.scrapping import download_dataset
from code.preprocessing import run_step1_preprocessing
from code.splitting import split_dataset
from code.load_and_process import load_and_preprocess

def main():
    # Step 1
    download_dataset()
    
    # Step 2
    run_step1_preprocessing()

        # Step 3
    split_dataset()

    # Step 4
    X_train, y_train, X_test, y_test, X_activation = load_and_preprocess()

    

if __name__ == "__main__":
    main()

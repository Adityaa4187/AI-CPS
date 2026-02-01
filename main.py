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
from scenarios.train_ann import train_ann, evaluate_ann
from scenarios.train_logreg import train_logreg, evaluate_logreg
from scenarios.train_ols import train_ols, evaluate_ols
from scenarios.train_rf import train_rf, evaluate_rf
from code.activation_inference import run_activation_inference

def main():
    # Step 1
    download_dataset()
    
    # Step 2
    run_step1_preprocessing()

        # Step 3
    split_dataset()

    # Step 4
    X_train, y_train, X_test, y_test, X_activation = load_and_preprocess()

    # Step 5 - Train + Evaluate Models (with plots)
    print("\n================ TRAINING MODELS ================\n")

    # OLS
    ols_model = train_ols(X_train, y_train)
    evaluate_ols(ols_model, X_test, y_test, threshold=0.5)

    rf_model = train_rf(X_train, y_train)
    evaluate_rf(rf_model, X_test, y_test, threshold=0.5)

    logreg_model = train_logreg(X_train, y_train)
    evaluate_logreg(logreg_model, X_test, y_test, threshold=0.5)

    ann_model = train_ann(X_train, y_train, epochs=25, batch_size=32)
    evaluate_ann(ann_model, X_test, y_test, threshold=0.5)

    # Step 6 - Activation Blind Testing
    print("\n\n\n ACTIVATION BLIND TEST \n")
    run_activation_inference()
    

if __name__ == "__main__":
    main()

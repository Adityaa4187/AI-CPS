# AI-CPS Course Project

#### Course: M. Grum – Advanced AI-based Application Systems
This repository is a fork of MarcusGrum/AI-CPS and contains our project implementation using the same repository structure.

### Current Stage

1. Dataset acquisition module that downloads the IBM HR Employee Attrition dataset for later pipeline steps.
2. Step 1 preprocessing to clean and prepare the dataset
3. Dataset splitting into training, test, and activation sets
4. Feature preprocessing and transformation pipeline
5. Basic visualizations generated from the processed data

#### Implemented Files
 1. main.py – Runs the download process
 2. code/scrapping.py – Downloads and saves the dataset
 3. code/preprocessing.py – Performs initial data preprocessing
 3. code/splitting.py – Splits data into training, test, and activation sets
 4. code/load_and_process.py – Applies feature preprocessing and saves transformation artifacts
 5. code/plots.py – Generates basic visualizations from the dataset
 6. requirements.txt – Project dependencies

#### Output

1. Raw Dataset

       data/scrapped/WA_Fn-UseC_-HR-Employee-Attrition.csv

2. Step 1 Cleaned Dataset

       data/step1/step1_cleaned_dataset.csv

3. Split Datasets

        data/split data/training_data.csv  
        data/split data/test_data.csv  
        data/split data/activation_data.csv
   
3. Generated Plots

       reports/step1_plots/




#### Run the Project
        git clone https://github.com/Adityaa4187/AI-CPS.git
        cd AI-CPS
        pip install -r requirements.txt
        python main.py

This project will continue to expand with further preprocessing, modeling, and evaluation stages.

# AI-CPS Course Project

#### Course: M. Grum – Advanced AI-based Application Systems
This repository is a fork of MarcusGrum/AI-CPS and contains our project implementation using the same repository structure.

### Current Stage

1. Dataset acquisition module that downloads the IBM HR Employee Attrition dataset for later pipeline steps.
2. Step 1 preprocessing to clean and prepare the dataset
3. Dataset splitting into training, test, and activation sets
4. Feature preprocessing and transformation pipeline
5. Basic visualizations generated from the processed data
6. Model training using OLS, Random Forest and Logistic Regression and Artificial Neural Networks
7. Model evaluation with performance plots

#### Implemented Files
 1. main.py – Runs the download process
 2. code/scrapping.py – Downloads and saves the dataset
 3. code/preprocessing.py – Performs initial data preprocessing
 3. code/splitting.py – Splits data into training, test, and activation sets
 4. code/load_and_process.py – Applies feature preprocessing and saves transformation artifacts
 5. code/plots.py – Generates basic visualizations from the dataset
 6. scenarios/train_ann.py – Trains an Artificial Neural Network model
 7. scenarios/train_logreg.py – Trains a Logistic Regression model
 8. scenarios/train_ols.py – Trains a OLS model
 9. scenarios/train_rf.py – Trains a Random Forest model
 10. requirements.txt – Project dependencies

#### Output

1. Raw Dataset

       data/scrapped/WA_Fn-UseC_-HR-Employee-Attrition.csv

2. Step 1 Cleaned Dataset

       data/step1/step1_cleaned_dataset.csv

3. Split Datasets

        data/split data/training_data.csv  
        data/split data/test_data.csv  
        data/split data/activation_data.csv

4. Preprocessing Artifacts

        artifacts/preprocessor.pkl

   
3. Generated Plots

       reports/step1_plots/


### Model Outputs
#### Saved Models

       documentation/Saved_models/ols_model.pkl
       documentation/Saved_models/rf_model.pkl
       documentation/Saved_models/logreg_model.pkl
       documentation/Saved_models/ann_models.h5

1. OLS plots:

       reports/model_plots/ols/

2. Random Forest plots:

       reports/model_plots/rf/

3. Logistic Regression plots:

       reports/model_plots/logreg/

4. ANN plots:

       reports/model_plots/ann/


#### Run the Project
        git clone https://github.com/Adityaa4187/AI-CPS.git
        cd AI-CPS
        pip install -r requirements.txt
        python main.py

This project will continue to expand with further preprocessing, modeling, and evaluation stages.

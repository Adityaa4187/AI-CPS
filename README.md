9# AI-CPS Course Project

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
8. Activation inference module for blind testing on unseen employee data
9. Early attrition risk scoring using rule-based heuristics

#### Implemented Files
 1. main.py – Runs the download process
 2. code/scrapping.py – Downloads and saves the dataset
 3. code/preprocessing.py – Performs initial data preprocessing
 4. code/splitting.py – Splits data into training, test, and activation sets
 5. code/load_and_process.py – Applies feature preprocessing and saves transformation artifacts
 6. code/plots.py – Generates basic visualizations from the dataset
 7. scenarios/train_ann.py – Trains an Artificial Neural Network model
 8. scenarios/train_logreg.py – Trains a Logistic Regression model
 9. scenarios/train_ols.py – Trains a OLS model
 10. scenarios/train_rf.py – Trains a Random Forest model
 11. code/early_risk.py – Rule-based early attrition risk scoring logic
 12. code/activation_inference.py – Runs blind-test inference on activation dataset using all trained models and generates risk report
 13. requirements.txt – Project dependencies

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


Each model folder contains:
1. Confusion Matrix
2. ROC Curve
3. Precision–Recall Curve
4. Learning Curve (Train vs Test)

#### Activation Inference Output
Blind-test predictions on unseen employee data:

       reports/activation_risk_report.csv

#### Run the Project
        git clone https://github.com/Adityaa4187/AI-CPS.git
        cd AI-CPS
        pip install -r requirements.txt
        python main.py

This project will continue to expand with further preprocessing, modeling, and evaluation stages.

# 🐳 Docker Execution (Pre-Built Images)
This project can be executed using pre-built Docker images hosted on Docker Hub.
No local Python setup is required.

All Docker orchestration files are located in:
```bash
dockerPipeline/
```
A detailed step-by-step guide is available in:
```bash
dockerPipeline/README_docker.md
```

### Available Docker Images
|Purpose	|Docker Image
|---------|--------------|
| **Model Training Pipeline**  |	adityaa0403/aibas_main_train|
|**Activation & Risk Inference**	|adityaa0403/aibas_main_activation|

### These images already contain:
1. All dependencies
2. Project code
3. Preconfigured runtime environments

### Pull the Required Images
```bash
docker pull adityaa0403/aibas_main_train
docker pull adityaa0403/aibas_main_activation
```

### Run the Training Pipeline
```bash
docker compose up
```
This commad runs the full pipeline:
1. Data preprocessing
2. Dataset splitting
3. Feature engineering
4. Model training
5. Evaluation and plot generation

### Run Activation & Early Risk Inference
```bash
docker compose -f docker-compose_activation.yml up
```

This runs:
1. Activation dataset inference
2. Early attrition risk scoring
3. Risk report generation

#### Important Notes
1. Docker ensures a reproducible, dependency-safe environment.
2. No Python or library installation is needed locally.
3. Compose files handle container configuration automatically.
4. For volume mounting, rebuilding images, or advanced usage, see:
```bash
   dockerPipeline/README_docker.md
```



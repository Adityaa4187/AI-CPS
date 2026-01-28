# main.py
# Entry point of the whole project.
# Step 1: download raw dataset from GitHub using scrapping.py
import os
import sys

from code.scrapping import download_dataset
from code.preprocessing import run_step1_preprocessing

def main():
    # Step 1
    download_dataset()
    
    # Step 2
    run_step1_preprocessing()

if __name__ == "__main__":
    main()

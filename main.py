# main.py
# Entry point of the whole project.
# Step 1: download raw dataset from GitHub using scrapping.py
import os
import sys

from code.scrapping import download_dataset

def main():
    # Step 1
    download_dataset()

if __name__ == "__main__":
    main()

"""
Description:
    This file will read the Iris.csv data set and print off every line. 
    It is the first homework of class DS-5110.
Author: Ruobing Wang
Date: 01/20/2025
"""
import os

def read_csv(file_path: str):
    """
    Reads a CSV file and prints each line.

    Parameters:
    file_path (str): The path to the CSV file to be read.   
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                print(line)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == '__main__':
    BASE_PATH = os.path.abspath('./data/') # file path, use abs path
    FILENAME = 'Iris.csv' # file name

    read_csv(os.path.join(BASE_PATH, FILENAME))

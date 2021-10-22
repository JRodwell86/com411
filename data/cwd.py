print("Processing...")
import os
path = os.getcwd()
print(f"The current working directory is: {path}")

for file in os.listdir(path):
    print("The directory contains the following files:")
    print(file)
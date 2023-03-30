import os

# Define the file paths relative to the project root directory
PROJECT_ROOT = '/home/kunal/plantidentifier/plantidentifier'
MODEL_FILE_PATH = os.path.join(PROJECT_ROOT, 'my_model.h5')
PREPROCESSED_FILE_PATH = os.path.join(PROJECT_ROOT, 'preprocessed_features.npy')
PLANT_DETAILS_FILE_PATH = os.path.join(PROJECT_ROOT, 'Plant name and properties.xlsx')

import zipfile
import os
import shutil

# Requires Alzheimer_Data.zip from https://www.kaggle.com/datasets/tourist55/alzheimers-dataset-4-class-of-images
# Requires MRI_Data.zip from https://www.kaggle.com/datasets/sachinkumar413/alzheimer-mri-dataset
# Must be put into Kaggle_Data/Alzheimer_Data and Kaggle_Data/MRI_Data folders respectively

def alzheimer_collect_data():
    # Put all mild demented Alzheimer data together
    mild_dem_path = os.path.join(os.getcwd(), "Kaggle_Data/Alzheimer_Data/Mild")
    if not os.path.exists(mild_dem_path):
        os.makedirs(mild_dem_path)

    # Path 1
    path1 = os.path.join(alzheimer_data_path, "Alzheimer_s Dataset/test/VeryMildDemented")
    for i in os.listdir(path1):
        shutil.copy(os.path.join(path1, i), mild_dem_path)

    # Path 2
    path2 = os.path.join(alzheimer_data_path, "Alzheimer_s Dataset/train/VeryMildDemented")
    for i in os.listdir(path2):
        shutil.copy(os.path.join(path2, i), mild_dem_path)

    # Path 3
    path3 = os.path.join(alzheimer_data_path, "Alzheimer_s Dataset/test/MildDemented")
    for i in os.listdir(path3):
        shutil.copy(os.path.join(path3, i), mild_dem_path)

    # Path 4
    path4 = os.path.join(alzheimer_data_path, "Alzheimer_s Dataset/train/MildDemented")
    for i in os.listdir(path4):
        shutil.copy(os.path.join(path4, i), mild_dem_path)
    

    # Put all non demented Alzheimer data together
    non_dem_path = os.path.join(os.getcwd(), "Kaggle_Data/Alzheimer_Data/NonDemented")
    if not os.path.exists(non_dem_path):
        os.makedirs(non_dem_path)

    # Path 1
    path1 = os.path.join(alzheimer_data_path, "Alzheimer_s Dataset/test/NonDemented")
    for i in os.listdir(path1):
        shutil.copy(os.path.join(path1, i), non_dem_path)

    # Path 2
    path2 = os.path.join(alzheimer_data_path, "Alzheimer_s Dataset/train/NonDemented")
    for i in os.listdir(path2):
        shutil.copy(os.path.join(path2, i), non_dem_path)

def mri_collect_data():
    # Put all mild demented Alzheimer data together
    mild_dem_path = os.path.join(os.getcwd(), "Kaggle_Data/MRI_Data/Mild")
    if not os.path.exists(mild_dem_path):
        os.makedirs(mild_dem_path)

    # Path 1
    path1 = os.path.join(mri_data_path, "Dataset/Mild_Demented")
    for i in os.listdir(path1):
        shutil.copy(os.path.join(path1, i), mild_dem_path)

    # Path 2
    path2 = os.path.join(mri_data_path, "Dataset/Very_Mild_Demented")
    for i in os.listdir(path2):
        shutil.copy(os.path.join(path2, i), mild_dem_path)

    # Move non demented to another folder that is easier to access
    non_dem_path = os.path.join(os.getcwd(), "Kaggle_Data/MRI_Data/NonDemented")
    if not os.path.exists(non_dem_path):
        os.makedirs(non_dem_path)

    # Path 1
    path1 = os.path.join(mri_data_path, "Dataset/Non_Demented")
    for i in os.listdir(path1):
        shutil.copy(os.path.join(path1, i), non_dem_path)
        
def move_data(path):
    # Setup mild and non-demented paths
    mild_path = os.path.join(path, "Mild")
    non_dem_path = os.path.join(path, "NonDemented")

    # Get lists of both directories
    mild = os.listdir(mild_path)
    non_dem = os.listdir(non_dem_path)

    # Check which there is more of
    if len(mild) > len(non_dem):
        more_mild = True
    else:
        more_mild = False

    # Loop through and add equal amounts of mild and non-demented training data
    if more_mild == True:
        for i in range(len(non_dem)):
            shutil.copy(os.path.join(mild_path, mild[i]), mild_train_path)
            shutil.copy(os.path.join(non_dem_path, non_dem[i]), non_dem_train_path)
    else:
        for i in range(len(mild)):
            shutil.copy(os.path.join(mild_path, mild[i]), mild_train_path)
            shutil.copy(os.path.join(non_dem_path, non_dem[i]), non_dem_train_path)


if __name__ == "__main__":
    # Set up path to unzip data
    alzheimer_data_path = os.path.join(os.getcwd(), "Kaggle_Data/Alzheimer_Data")
    mri_data_path = os.path.join(os.getcwd(), "Kaggle_Data/MRI_Data")

    # Paths of zip files
    alzheimer_datazip_path = os.path.join(alzheimer_data_path, "Alzheimer_Data.zip")
    mri_datazip_path = os.path.join(mri_data_path, "MRI_Data.zip")

    # Unzip Alzheimer's Data
    with zipfile.ZipFile(alzheimer_datazip_path, 'r') as zip_ref:
        zip_ref.extractall(alzheimer_data_path)

    # Unzip MRI Data
    with zipfile.ZipFile(mri_datazip_path, 'r') as zip_ref:
        zip_ref.extractall(mri_data_path)

    # Group Alzheimer data together
    alzheimer_collect_data()

    # Group MRI data together
    mri_collect_data()

    # Create directories to place data to be augmented
    mild_train_path = os.path.join(os.getcwd(), "NeedtoAugmentData/Mild-Demented")
    non_dem_train_path = os.path.join(os.getcwd(), "NeedtoAugmentData/Non-Demented")
    if not os.path.exists(mild_train_path):
        os.makedirs(mild_train_path)
    if not os.path.exists(non_dem_train_path):
        os.makedirs(non_dem_train_path)

    # Separate data to be augmented
    move_data(alzheimer_data_path)
    move_data(mri_data_path)
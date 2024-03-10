from PIL import Image, ImageFilter, ImageEnhance
import os
import numpy as np

''' 

Please note that the input to the function must be the folder name
# of the respected image classes

# Example: 

# original_dir = 'original_images/'

# '''

# # Directory name for original non-dementia files
# no_dem = os.path.join(os.getcwd(), "NeedtoAugmentData/Non-Demented")

# # Directory name for origianl non-dementia files
# mild_dem = os.path.join(os.getcwd(), "NeedtoAugmentData/Mild-Demented")

no_dem = '/Users/matthew/Desktop/APS_360/Alzheimer_s Dataset/test/MildDemented'
mild_dem = '/Users/matthew/Desktop/APS_360/Alzheimer_s Dataset/test/MildDemented'

def find_dim(path): 
    
    for filename in os.listdir(path):
        width_max = 0
        height_max = 0
        width, height = filename.size

        if width > width_max: 
            width_max = width
        if height > height_max: 
            hieght_max = height
    
    dim = max(width, height)
    return dim

def augment(original_dir, specifics):

    # Create folder for augmented photos
    os.makedirs(f'augmented/{specifics}')
    augmented_dir = os.path.abspath(f'augmented/{specifics}')
    
    dim = find_dim(original_dir)
    # Dictionary with augmentation methods
    augmentation_params = [
        {'name': 'rotate'},
        {'name': 'gaussian_blur'},
        {'name': 'brightness_enhancer', 
         'name': 'original'}
    ]
    # Iterate through each image
    for filename in os.listdir(original_dir):
        
        # Check to see if it actually is an image 
        # and then assign the image to a variable 
        if filename.endswith('.jpg') or filename.endswith('.png'):
            original_image = Image.open(os.path.join(original_dir, filename))

            # Apply a rotation of 90 degrees
            for params in augmentation_params:
                if params['name'] == 'rotate':
                    augmented_image = original_image.rotate(90)
                    swapped = np.swapaxes(original_image, 0, 1)
                    augmented_image = augmented_image.resize(swapped.size)
                    
                # apply a slight blur
                elif params['name'] == 'gaussian_blur':
                    augmented_image = original_image.filter(ImageFilter.GaussianBlur(radius=1.5))
                    augmented_image = augmented_image.resize(original_image.size)

                # apply a 40% increase in brightness
                elif params['name'] == 'brightness_enhancer': 
                    # Create a brightness enhancer object
                    brightness_enhancer = ImageEnhance.Brightness(original_image)
                    # Enhance the brightness by a factor of 8 (dramatically increases brightness)
                    augmented_image = brightness_enhancer.enhance(1.4)
                    augmented_image = augmented_image.resize(original_image.size)
                    
                elif params['name'] == 'original':
                    augmented_image = original_image
                    augmented_image = augmented_image.resize(original_image.size)

                width, height = augmented_image.size
    
                # Calculate the padding sizes
                pad_width = max(dim - width, 0)
                pad_height = max(dim - height, 0)
                
                # Calculate the padding parameters (left, top, right, bottom)
                padding = (0, 0, pad_width, pad_height)
                
                # Add padding to the image
                padded_image = Image.new(augmented_image.mode, [dim, dim], color='white')  # You can set the color as you want
                padded_image.paste(augmented_image, padding)

                # Save the augmented image
                augmented_filename = os.path.splitext(filename)[0] + '_' + params['name'] + '.jpg'
                augmented_image.save(os.path.join(augmented_dir, augmented_filename))

    print("Augmentation complete.")
    

augment(no_dem, 'not_dementia')
augment(mild_dem, 'mild_dementia')
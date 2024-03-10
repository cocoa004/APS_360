from PIL import Image, ImageFilter, ImageEnhance
import os

''' 

Please note that the input to the function must be the folder name
# of the respected image classes

# Example: 

# original_dir = 'original_images/'

# '''

# Directory name for original non-dementia files
no_dem = os.path.join(os.getcwd(), "NeedtoAugmentData/Non-Demented")

# Directory name for origianl non-dementia files
mild_dem = os.path.join(os.getcwd(), "NeedtoAugmentData/Mild-Demented")



def augment(original_dir, specifics):

    # Create folder for augmented photos
    os.makedirs(f'augmented/{specifics}')
    augmented_dir = os.path.abspath(f'augmented/{specifics}')
    

    # Dictionary with augmentation methods
    augmentation_params = [
        {'name': 'rotate'},
        {'name': 'gaussian_blur'},
        {'name': 'brightness_enhancer'}
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
                    
                # apply a slight blur
                elif params['name'] == 'gaussian_blur':
                    augmented_image = original_image.filter(ImageFilter.GaussianBlur(radius=1.5))

                # apply a 40% increase in brightness
                elif params['name'] == 'brightness_enhancer': 
                    # Create a brightness enhancer object
                    brightness_enhancer = ImageEnhance.Brightness(original_image)
                    # Enhance the brightness by a factor of 8 (dramatically increases brightness)
                    augmented_image = brightness_enhancer.enhance(1.4)

                # Save the augmented image
                augmented_filename = os.path.splitext(filename)[0] + '_' + params['name'] + '.jpg'
                augmented_image.save(os.path.join(augmented_dir, augmented_filename))

    print("Augmentation complete.")
    

augment(no_dem, 'not_dementia')
augment(mild_dem, 'mild_dementia')
from PIL import Image, ImageFilter, ImageEnhance
import os
import numpy as np

# Directory name for original non-dementia files
no_dem = os.path.join(os.getcwd(), "NeedtoAugmentData/Non-Demented")

# Directory name for original non-dementia files
mild_dem = os.path.join(os.getcwd(), "NeedtoAugmentData/Mild-Demented")


def find_dim(path): 
    
    for filename in os.listdir(path):
        image = Image.open(os.path.join(path, filename))
        width_max = 0
        height_max = 0
        width, height = image.size

        if width > width_max: 
            width_max = width
        if height > height_max: 
            height_max = height
    
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
        original_image = Image.open(os.path.join(original_dir, filename))
        
        # Check to see if it actually is an image 
        # and then assign the image to a variable 
        if filename.endswith('.jpg') or filename.endswith('.png'):
          
            # First make all the input images the sime dimension by
            # adding a padding layer around the edges and make them all 
            # squares
            
            # find dim of image
            width, height = original_image.size
    
            # Determine padding sizes
            pad_width = max(dim - width, 0)
            pad_height = max(dim - height, 0)
            
            
            # Create blank image with just the padding
            padded_image = Image.new(original_image.mode, (dim, dim), color='white') # Here Might change to black if yields better training results
            
            # Paste the original image onto the padded image
            padded_image.paste(original_image, (pad_width//2//2,pad_height//2))


            # Now that all images are of the same sizes without distorting
            
            
            # Apply a rotation of 90 degrees
            for params in augmentation_params:
                if params['name'] == 'rotate':
                    augmented_image = padded_image.rotate(90)

                    
                # apply a slight blur
                elif params['name'] == 'gaussian_blur':
                    augmented_image = padded_image.filter(ImageFilter.GaussianBlur(radius=1.5))
                    augmented_image = augmented_image.resize(padded_image.size)

                # apply a 40% increase in brightness
                elif params['name'] == 'brightness_enhancer': 
                    # Create a brightness enhancer object
                    brightness_enhancer = ImageEnhance.Brightness(padded_image)
                    # Enhance the brightness by a factor of 8 (dramatically increases brightness)
                    augmented_image = brightness_enhancer.enhance(1.4)
                    augmented_image = augmented_image.resize(padded_image.size)
                    
                elif params['name'] == 'original':
                    augmented_image = padded_image
                    augmented_image = augmented_image.resize(padded_image.size)

        
                # Save the augmented image
                augmented_filename = os.path.splitext(filename)[0] + '_' + params['name'] + '.jpg'
                augmented_image.save(os.path.join(augmented_dir, augmented_filename))

    print("Augmentation complete.")
    

augment(no_dem, 'not_dementia')
augment(mild_dem, 'mild_dementia')
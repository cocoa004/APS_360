from PIL import Image, ImageFilter, ImageEnhance
import os

# Image Locations/folders
original_dir = 'original_images/'
augmented_dir = 'augmented_images/'

# Stating the different ways of augmneting the data
augmentation_params = [
    {'name': 'rotate'},
    {'name': 'gaussian_blur'},
    {'name': 'brightness_enhancer'}
]

# Go through each image and apply the filters to obtain 3 new images
for filename in os.listdir(original_dir):
    # check to make sur it is actually an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # set original_image equal to the iterated image
        original_image = Image.open(os.path.join(original_dir, filename))

        # Apply the augmnetations
        for params in augmentation_params:
            
            # Rotate the image 90 degrees
            if params['name'] == 'rotate':
                augmented_image = original_image.rotate(90)
                
            # slightly blurs image
            elif params['name'] == 'gaussian_blur':
                augmented_image = original_image.filter(ImageFilter.GaussianBlur(radius=1.4))

            # Makes image 40% brighter
            elif params['name'] == 'brightness_enhancer':
                brightness_enhancer = ImageEnhance.Brightness(original_image)
                augmented_image = brightness_enhancer.enhance(1.4)

            # Save the augmented images
            augmented_filename = os.path.splitext(filename)[0] + '_' + params['name'] + '.jpg'
            augmented_image.save(os.path.join(augmented_dir, augmented_filename))

print("Augmentation complete.")
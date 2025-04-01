from PIL import Image
import os

def convert_image_to_webp(input_image_path):
    # Open the image file
    with Image.open(input_image_path) as img:
        # Generate output filename
        output_filename = os.path.splitext(os.path.basename(input_image_path))[0] + '.webp'
        output_path = os.path.join(os.path.dirname(input_image_path), output_filename)

        # Save the image as WebP
        img.save(output_path, 'WEBP')
        return output_filename

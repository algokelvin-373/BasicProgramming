import io
import os
import time as time
import glob
import concurrent.futures
from PIL import Image
from rembg import remove  # Library for remove background

def process_single_image(input_path, output_path):
    """Proses single image: remove background + resize"""
    try:
        # Validation input
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")

        # Read image
        with open(input_path, 'rb') as f:
            input_image = f.read()

        # Remove background
        output_image = remove(input_image)  # use rembg

        # Proses resize
        with io.BytesIO(output_image) as img_buffer:
            foreground = Image.open(img_buffer).convert("RGBA")
            background = Image.open('background.jpg').convert("RGBA")

            # Hitung resize ratio
            bg_width, bg_height = background.size
            fg_width, fg_height = foreground.size

            # Resize proporsional
            ratio = bg_height / fg_height
            new_width = int(fg_width * ratio)
            new_height = bg_height

            # Resize dan posisi tengah
            foreground = foreground.resize((new_width, new_height), Image.LANCZOS)
            position = ((bg_width - new_width) // 2, 0)

            # Gabungkan dengan background
            background.paste(foreground, position, foreground)

            # Simpan hasil
            background.convert("RGB").save(
                output_path,
                quality=85,
                optimize=True,
                progressive=True
            )

    except Exception as e:
        print(f"Error processing {input_path} to {output_path}: {str(e)}")
        raise

times = time.time()
input_path = 'D:/output_no_bg_1745824718.9640653.jpg'
output_path = f'D:/result_resize_optimize_{times}.jpg'
process_single_image(input_path, output_path)
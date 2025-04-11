from PIL import Image
import os

def convert_webp_to_jpg(input_path, output_path=None, quality=85):
    with Image.open(input_path) as img:
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.jpg'

        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])  # Paste using alpha channel as mask
            img = background

        img.save(output_path, 'JPEG', quality=quality)
        print(f"Converted {input_path} to {output_path}")

input_image = 'D:/INA17Group/0S_ServerIna17/photos_custom/photos8.webp'
output_image = 'D:/INA17Group/0S_ServerIna17/photos_result/photo8.jpg'
convert_webp_to_jpg(input_image, output_image)
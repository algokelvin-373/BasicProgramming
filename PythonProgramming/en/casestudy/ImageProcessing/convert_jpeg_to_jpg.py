from PIL import Image

def convert_jpeg_to_jpg(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        rgb_img = img.convert('RGB')  # make sure it's in RGB
        rgb_img.save(output_path, 'JPEG', quality=quality)

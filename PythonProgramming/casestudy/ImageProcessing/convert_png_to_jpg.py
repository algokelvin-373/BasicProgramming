from PIL import Image

def convert_png_to_jpg(input_path, output_path, quality=85):
    with Image.open(input_path) as img:
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])
            background.save(output_path, 'JPEG', quality=quality)
        else:
            rgb_img = img.convert('RGB')
            rgb_img.save(output_path, 'JPEG', quality=quality)

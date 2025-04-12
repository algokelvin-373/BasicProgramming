import time

from rembg import remove
from PIL import Image

def processing_resize(path_output):
    fg = Image.open(path_output).convert("RGBA")
    bg = Image.open(background).convert("RGBA")

    # Calculate ratio is needed
    bg_width, bg_height = bg.size
    fg_width, fg_height = fg.size

    # Skala berdasarkan tinggi (biar proporsional kayak hasil Figma)
    height_ratio = bg_height / fg_height
    new_width = int(fg_width * height_ratio)
    new_height = int(fg_height * height_ratio)

    # Resize gambar dengan mempertahankan aspect ratio
    fg = fg.resize((new_width, new_height), Image.LANCZOS)

    # Letakkan di tengah background (horizontal saja cukup karena tinggi sudah pas)
    position = ((bg_width - new_width) // 2, 0)

    # Gabungkan
    combined = bg.copy()
    combined.paste(fg, position, fg)

    # Simpan
    rgb_image = combined.convert("RGB")
    rgb_image.save(output_path)

def processing_remove_background(path_input, path_output):
    # Read Input Image and Remove Background
    with open(path_input, 'rb') as i:
        input_data = i.read()
        output_data = remove(input_data)

    # Write Data Image After Remove Background
    with open(path_output, 'wb') as o:
        o.write(output_data)

background = f'D:/INA17Group/0S_ServerIna17/photos_result/background.jpg'
start = int(time.time() * 1000)
index = 0
while index < 43:
    input_path = f'D:/INA17Group/0S_ServerIna17/photos_result/photos{index + 1}.jpg'
    output_path = f'D:/INA17Group/0S_ServerIna17/photos_result/'
    if index > 99:
        output_path += f'50{index}_00.jpg'
    elif 10 <= index <= 99:
        output_path += f'500{index}_00.jpg'
    else:
        output_path += f'5000{index}_00.jpg'

    processing_remove_background(input_path, output_path)
    processing_resize(output_path)

    index += 1
end = int(time.time() * 1000)

print(f'Done - Time: {end - start} ms') # milidetik
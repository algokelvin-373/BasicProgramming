import glob
import os

from casestudy.ImageProcessing.convert_webp_to_jpg import convert_webp_to_jpg

def multiple_convert_webp(input_dir, output_dir=None, quality=85):
    if output_dir is None:
        output_dir = input_dir
    elif not os.path.exists(output_dir):
        os.makedirs(output_dir)

    webp_files = glob.glob(os.path.join(input_dir, '*.webp'))

    for webp_file in webp_files:
        jpg_file = os.path.join(
            output_dir,
            os.path.splitext(os.path.basename(webp_file))[0] + '.jpg'
        )
        convert_webp_to_jpg(webp_file, jpg_file, quality)

input_directory = 'D:/INA17Group/0S_ServerIna17/photos_custom'
output_directory = 'D:/INA17Group/0S_ServerIna17/photos_result'
multiple_convert_webp(input_directory, output_directory)
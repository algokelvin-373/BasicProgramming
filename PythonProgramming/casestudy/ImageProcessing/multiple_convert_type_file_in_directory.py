import glob
import os
import argparse

from convert_jpeg_to_jpg import convert_jpeg_to_jpg
from convert_png_to_jpg import convert_png_to_jpg
from convert_webp_to_jpg import convert_webp_to_jpg

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

def multiple_convert_jpeg(input_dir, output_dir=None, quality=85):
    if output_dir is None:
        output_dir = input_dir
    elif not os.path.exists(output_dir):
        os.makedirs(output_dir)

    jpeg_files = glob.glob(os.path.join(input_dir, '*.jpeg'))

    for jpeg_file in jpeg_files:
        jpg_file = os.path.join(
            output_dir,
            os.path.splitext(os.path.basename(jpeg_file))[0] + '.jpg'
        )
        convert_jpeg_to_jpg(jpeg_file, jpg_file, quality)

def multiple_convert_png(input_dir, output_dir=None, quality=85):
    if output_dir is None:
        output_dir = input_dir
    elif not os.path.exists(output_dir):
        os.makedirs(output_dir)

    png_files = glob.glob(os.path.join(input_dir, '*.png'))

    for png_file in png_files:
        jpg_file = os.path.join(
            output_dir,
            os.path.splitext(os.path.basename(png_file))[0] + '.jpg'
        )
        convert_png_to_jpg(png_file, jpg_file, quality)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert multiple image formats to JPG')
    parser.add_argument('-i', '--input', required=True, help='Input directory containing images')
    parser.add_argument('-o', '--output', required=True, help='Output directory for converted JPGs')
    parser.add_argument('-q', '--quality', type=int, default=85,
                        help='JPEG quality (1-100), default is 85')

    args = parser.parse_args()

    # Validate quality value
    if args.quality < 1 or args.quality > 100:
        print("Error: Quality must be between 1 and 100")
        return

    # Validate directories
    if not os.path.exists(args.input):
        print(f"Error: Input directory does not exist: {args.input}")
        return

    # Run conversions
    print(f"Starting conversion from {args.input} to {args.output}...")
    multiple_convert_webp(args.input, args.output, args.quality)
    multiple_convert_jpeg(args.input, args.output, args.quality)
    multiple_convert_png(args.input, args.output, args.quality)
    print("Conversion completed!")

# Run in terminal
# python multiple_convert_type_file_in_directory.py -i "[input_path]" -o "[output_path]"

if __name__ == "__main__":
    main()

# input_directory = 'D:/INA17Group/0S_ServerIna17/photos_custom'
# output_directory = 'D:/INA17Group/0S_ServerIna17/photos_result'
# multiple_convert_webp(input_directory, output_directory)
# multiple_convert_jpeg(input_directory, output_directory)
# multiple_convert_png(input_directory, output_directory)
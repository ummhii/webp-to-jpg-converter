import os
import argparse
from PIL import Image

def convert_image(root, filename):
    if filename.lower().endswith('.webp'):
        webp_path = os.path.join(root, filename)
        jpg_filename = os.path.splitext(filename)[0] + '.jpg'
        jpg_path = os.path.join(root, jpg_filename)
        try:
            with Image.open(webp_path) as img:
                rgb_img = img.convert('RGB')
                rgb_img.save(jpg_path, 'JPEG')
                os.remove(webp_path)
            print(f'Converted {filename} to {jpg_filename} & deleted .webp')
        except Exception as e:
            print(f'Failed to convert {filename}: {e}')


def convert_webpg_to_jpg(directory, recursive=False):
    if recursive:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                convert_image(root, filename)
    else:
        for filename in os.listdir(directory):
            convert_image(directory, filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert .webp images to .jpg format.')
    parser.add_argument('directory', nargs='?', default=os.getcwd(),
                        help='Directory to search for .webp files.')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Recursively convert .webp files in all subdirectories.')

    args = parser.parse_args()
    convert_webpg_to_jpg(args.directory, args.recursive)
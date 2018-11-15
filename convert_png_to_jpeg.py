import glob
import os
from skimage.io import imread, imsave


path_to_png_photos = r'C:\NAIVE\datasets\shots\all_images'

png_paths = glob.glob(os.path.join(path_to_png_photos, '*.png'))
print(png_paths)

for png_path in png_paths:
    jpg_path = png_path.replace('.png', '.jpg')
    imsave(jpg_path, imread(png_path))

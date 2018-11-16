import glob
import os
from skimage.io import imread, imsave


src_dst = r'C:\NAIVE\datasets\good_frame\images'
dst_path = r'C:\NAIVE\datamarker-flask\data\dataset\all_images'

png_paths = glob.glob(os.path.join(src_dst, '*.png'))
print(png_paths)

for png_path in png_paths:
    file_name = os.path.basename(png_path)
    dst = os.path.join(dst_path, file_name.replace('.png', '.jpg'))
    imsave(dst, imread(png_path))

import glob
import os

path_to_videos = r'C:\NAIVE\datasets\good_frame\videos'
path_to_images = r'C:\NAIVE\datasets\good_frame\images'
if not os.path.exists(path_to_images):
    os.makedirs(path_to_images)

videos = glob.glob(os.path.join(path_to_videos, '**/**.mp4'), recursive=True)
print(videos)
for i, v in enumerate(videos):
    print(i, v)
    os.system('ffmpeg -i {} -r 0.5 {}_%04d.png'.format(v, os.path.join(path_to_images, str(i))))

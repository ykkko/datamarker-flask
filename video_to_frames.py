import glob
import os


def convert_from_directory(path_to_videos, path_to_images):
    if not os.path.exists(path_to_images):
        os.makedirs(path_to_images)

    videos = glob.glob(os.path.join(path_to_videos, '**/**.mp4'), recursive=True)
    print(videos)
    for i, v in enumerate(videos):
        print(i, v)
        os.system('ffmpeg -i {} -r 0.5 {}_%04d.png'.format(v, os.path.join(path_to_images, str(i))))


path_to_videos = r'C:\NAIVE\datasets\good_frame\new_videos'
path_to_images = r'C:\NAIVE\datasets\good_frame\test_images'

# convert_from_directory(path_to_videos, path_to_images)


path_to_video = r'C:\NAIVE\datasets\good_frame\new_videos\1014453610.mp4'
os.system('ffmpeg -i {} -r 0.5 {}_%04d.png'.format(path_to_video, os.path.join(path_to_images, str(3))))
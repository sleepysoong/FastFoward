import os
from moviepy.editor import VideoFileClip, vfx

input_folder = ""
output_folder = ""

SPEED = 2

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        mp4_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + "_x" + SPEED + ".mp4")
        clip = VideoFileClip(mp4_path)
        new_clip = clip.fx(vfx.speedx, SPEED)
        # 새로운 파일로 저장합니다
        new_clip.write_videofile(output _path, codec='libx264')
        clip.close()
        new_clip.close()

print("All MP4 files have been converted")

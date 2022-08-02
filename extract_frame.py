import cv2
import os
import shutil

duration = 30   # in frame

def extract_frame(video_url, out_path):

    cap = cv2.VideoCapture(video_url)
    frame = 0

    video_name = os.path.basename(video_url)

    while True:

        cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        ret, image = cap.read()

        if not ret:
            break

        image_name = video_name.replace('.mp4', f'_{frame:08d}.jpg')
        image_path = f'{out_path}/{image_name}'
        print(image_path, end='\r')

        cv2.imwrite(image_path, image)


        frame += duration 

    cap.release()


if __name__ == '__main__':
    video_file = '/Users/leeseunghak/data/video/test01.mp4'
    out_path = '/Users/leeseunghak/Downloads/ocr_frames'

    if os.path.exists(out_path):
        shutil.rmtree(out_path)
    os.mkdir(out_path)

    extract_frame(video_file, out_path)

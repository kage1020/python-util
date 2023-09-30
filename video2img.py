import cv2
import os
import glob

def video2img(video_path, output_path):
    if os.path.isdir(video_path):
        video_list = os.listdir(video_path)
        for video in video_list:
            video2img(os.path.join(video_path, video), os.path.join(output_path, video.split('.')[0]))
    else:
        if glob.glob(os.path.join(output_path, '*.jpg')):
            return
        print("Processing: ", video_path)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        count = 0
        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(f"{output_path}/{count:06d}.jpg", frame)
                count += 1
            else:
                break
        cap.release()
        print("Total frames: ", count)


if __name__ == '__main__':
    video_path = input("Please input the video path or video dir: ").replace('"', '')
    output_path = input("Please input the output path: ").replace('"', '')
    video2img(video_path, output_path)

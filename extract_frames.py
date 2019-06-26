import cv2
import argparse
import os


class Frame_extractor:
    def extract_frames(self, video_to_cut=None, output_dir=None, output_files=None):
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        vidcap = cv2.VideoCapture(video_to_cut)
        success, image = vidcap.read()
        count = 0
        imwrite_string = output_dir + '/' + output_files + '%d.png'
        print(imwrite_string)
        while success:
            # save frame as PNG file
            cv2.imwrite(imwrite_string % count, image)
            success, image = vidcap.read()
            print('Extracted frame: ', count)
            count += 1
        print("Extracted " + str(count) + " frames")

    def __init__(self, video_to_cut=None, output_dir=None, output_files=None):
        self.extract_frames(video_to_cut, output_dir, output_files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Tool for extracting frames from video')
    parser.add_argument('-f', '--file', default=None,
                        help='Video that will have the frames extracted', type=str)
    parser.add_argument('-o', '--output_dir', default='extracted',
                        help='Directory that will store the extracted frames', type=str)
    parser.add_argument('-n', '--name_of_files', default='frame',
                        help='What the extracted frames will be called', type=str)
    args = parser.parse_args()

    video_to_cut = args.file
    output_dir = args.output_dir
    output_files = args.name_of_files

    Frame_extractor(video_to_cut, output_dir, output_files)

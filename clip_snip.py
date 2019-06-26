from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip as extract_clip
from moviepy.editor import VideoFileClip
from math import floor as floor
import argparse


class Subclipper:
    def make_clip(self, start_time=None, end_time=None, file_name=None, output_file=None):
        if file_name is None:
            raise Exception('Must have a clip to extract a subclip from!')
        if start_time is None and end_time is None:
            raise Exception(
                'Must provide at least one start time or end time value!')
        clip = VideoFileClip(file_name)
        clip_length = floor(clip.duration)
        if output_file is None:
            output_file = 'output.mp4'
        if start_time is None and end_time is not None:
            extract_clip(file_name, 0, end_time, output_file)
        if start_time is not None and end_time is None:
            extract_clip(file_name, start_time, clip_length, output_file)
        if start_time is not None and end_time is not None:
            extract_clip(file_name, start_time, end_time, output_file)

    def __init__(self, start_time=None, end_time=None, file_name=None, output_file=None):
        self.make_clip(start_time, end_time, file_name, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Tool for snipping video clips')
    parser.add_argument('-s', '--start_time', default=0,
                        help='The time in seconds to start the snip at', type=int)
    parser.add_argument('-e', '--end_time', default=None,
                        help='The time in seconds to stop to stop the snip', type=int)
    parser.add_argument('-f', '--file', default=None,
                        help='The file that one wants to snip', type=str)
    parser.add_argument('-o', '--output', default='output.mp4',
                        help='The name of the output file', type=str)
    args = parser.parse_args()

    start_time = args.start_time
    end_time = args.end_time
    file_name = args.file
    output_file = args.output

    if file_name is None:
        raise Exception('Must have a clip to extract a subclip from!')

    print("Snipping clip...")
    Subclipper(start_time, end_time, file_name, output_file)
    print("Clip succesfully snipped!")

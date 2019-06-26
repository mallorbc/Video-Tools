import moviepy.editor as mp
import argparse


class Resizer:
    def resize_vid(self, file_name=None, new_height=None, output_file=None):
        clip = mp.VideoFileClip(file_name)
        # According to moviePy documenation The width is then computed so that the width/height ratio is conserved
        clip_resized = clip.resize(height=new_height)
        clip_resized.write_videofile(output_file)

    def __init__(self, file_name=None, new_height=None, output_file=None):
        self.resize_vid(file_name, new_height, output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Tool for resizing video clips and preserving ration')
    parser.add_argument('-f', '--file', default=None,
                        help='Name of the file that you want to resize', type=str)
    parser.add_argument('-o', '--output', default=None,
                        help='Optional.  Name of the outputed resized file', type=str)
    parser.add_argument('-s', '--size', default=None,
                        help='New height that will be used for resizing', type=int)
    args = parser.parse_args()

    file_name = args.file
    output_file = args.output
    new_height = args.size

    if file_name is None:
        raise Exception('Must provide a file that needs resized')

    if new_height is None:
        raise Exception('Must provide a new height to resize to')

    if output_file is None:
        period_index = file_name.find('.')
        print(period_index)
        output_file = file_name[:period_index]
        output_file = output_file + '_resized_' + str(new_height) + '.mp4'

    Resizer(file_name, new_height, output_file)

import argparse
from video import Video
    
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
	help="path to input video file")
ap.add_argument("-r", "--regex", nargs="?", type=str,
	help="regex to find text in video frames")
ap.add_argument("-o", "--output", type=str, default="./output.txt",
	help="path to (optional) output video file")
ap.add_argument("-v", "--verbose", type=int, default=0,
	help="If 1(True) will be printed in output file the text used in regex")
args = vars(ap.parse_args())

video = Video(args['input'], args['regex']).process() 
generator = video

for frame in generator:
    newLine = f'frame: { frame["id"] } | second: { frame["second"] } | matches: { frame["matches"] }\n'
    if args['verbose']:
        newLine = f'{"-"*50} \n\n text: { frame["text"] } \n' + newLine
    with open(args['output'],"a+") as f:
        f.write(newLine)







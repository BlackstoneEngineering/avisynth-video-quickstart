#!/usr/bin/env python 

import argparse
from os.path import isfile
import re
from subprocess import call


parser = argparse.ArgumentParser(description="video maker, to do all the stuff i'm too lazy to do!", 
								epilog="Example: video-maker.py ./test.mov 'Title' 'subtitle\\nsubtitle' --banner='Partner Video' ")

# check video file exists on system
def argparse_filestring_type(string) :
    if isfile(string) :
        return string
    else :
		raise argparse.ArgumentTypeError("{0}"" : does not exist in the filesystem.".format(string))

# check title, allow words, no newlines, check length
def argparse_title(thing) :
	if len(thing) > 20:
		raise argparse.ArgumentTypeError("{0}"" : title is too long, needs to be <20 characters".format(thing))
	x = re.compile('[\w\s]*')
	if x.match(thing):
		return thing
	else :
		raise argparse.ArgumentTypeError("{0}"" : is not a valid title.".format(thing))

# chcek subtitle, allow words, spaces and newlines
def argparse_subtitle(thing) :
	x = re.compile("[\w\s\\n\\r]*")
	if x.match(thing):
		return thing
	else :
		raise argparse.ArgumentTypeError("{0}"" : is not a valid subtitle.".format(thing))


# Required Arguments
parser.add_argument("video", type=argparse_filestring_type,
					help="Path to video, Absolute or Relative")
parser.add_argument("-t","--title", type=argparse_title, required=True,
					help="Title on title slide, <20char")
parser.add_argument("-s","--subtitle", type=argparse_subtitle, required=True,
					help="Subtitle for title slide, multiline, <20char per line")

# Optional Arguments
parser.add_argument("--color", choices=('grey','blue'), 
					help="color of title / ending slide, blue/grey")
parser.add_argument("-b","--banner", type=argparse_title,
					help="text in red banner across bottom of title slide" )


args = parser.parse_args()
options = parser.parse_args()

# main Logic
# write config options to config.avs
f = open('config.avs','w+')
f.write('t="{0}"\ns="{1}"\nname="{2}"'.format(options.title, options.subtitle, options.video))
f.close()
print("File config-test.avs written, calling ffmpeg")
# call ffmpeg to transcode the file for us
call(['ffmpeg','-i','main.avs','-vcodec', 'mpeg4','-b', '5000K', options.video+'.mp4'])
print("ffmpeg call finished, find movie at {0}.mp4 ".format(options.video))


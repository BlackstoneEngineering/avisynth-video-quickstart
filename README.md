##Summary
This tool is a simple AVISynth script that takes a video file as input and then sticks a title on the front of the video and a ending on the end of the video. The python utility allows for extra settings like adding a Title and Subtitle ontop of the title screen.

## Why?
I found myself having to make a bunch of simple videos with a title and ending legal credits, so I decided to mostly automate the process.

## Requirements
- [ffmpeg](http://ffmpeg.org/download.html)
- [Python > 2.7.9](https://www.python.org/downloads/)

## How to use
There is a python interface for this script setup. Run `video-maker.py` and provide it the video file and any optional arguments you wish. Make sure you replace `title.png` and `end.png` with your desired title and ending slides respectively. 

## Example

```shell
videomaker.py ./test.mov --title="my awesome title" --subtitle="subtitle line1 \nSubtitle line 2"
```
The above code will take the `test.mov` file and generate `test.mp4` which will have a title slide of 100 frames with the `title` and `subtitle` text put on the `title.png` image, in addition `end.png` will be appended to the end for 100 frames. 

## License
Apache 2.0, feel free to reuse for personal or professional work. I hope you can leverage this to keep yourself from going insane with mundane tasks. Credit to the Author is always nice but not required. 
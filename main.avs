# import config
Import("config.avs")

# get video to modify, assumes .mov currently
video = QTInput(name, color=2, audio=1).BicubicResize(1280,720).ConvertToRGB32()

# create settings
n = 100
blank = BlankClip(video, length=n)

# put everything together
begin = ImageSource("title.png").BicubicResize(1280,720).AssumeFps(video).ConvertToRGB32().Trim(0,n).AudioDub(blank).subtitle(t,x=125,y=300,font="GillAltOneMT-Bold" ,size=110,text_color=$2200769B,halo_color=$FFFFFFFF).subtitle(s,x=140,y=400,font="GillAltOneMT-Bold",size=90,text_color=$66555A5A, halo_color=$FFFFFFFF,lsp=1).subtitle(t,x=400,y=690,font="GillAltOneMT-Bold" ,size=110,text_color=$00000000,halo_color=$FFFFFFFF)
end = ImageSource("end.png").BicubicResize(1280,720).AssumeFps(video).ConvertToRGB32().Trim(0,n).AudioDub(blank)
begin.FadeOut(5)+video.FadeIO(5)+end.FadeIn(5)

# A command similar to this must be run to finish the creation of the video
#ffmpeg -i main.avs -vcodec mpeg4 -b 5000K output.mp4
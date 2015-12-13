#pip3 install moviepy
from moviepy.editor import ImageSequenceClip

frames = []

for i in range(180):
	frames.append("./globeframes/frame{0}.png".format((str(i).rjust(3, "0"))))


clip = ImageSequenceClip(frames, fps=20)


clip.write_videofile("SpinningGlobe.mp4", fps=20) # export as video
#clip.speedx(0.5).write_gif("SpinningGlobe.gif", fps=20) # export as GIF (slow)


from vapoursynth import core
import vapoursynth as vs
import havsfunc as haf
import adjust
import weighting
video = core.ffms2.Source(source="C:/Users/hamey.DESKTOP-MULCHGK/Desktop/lastportfolio/TESTRENDER-4x-RIFE-RIFE4.0-239.76fps.mp4", cache=False)
video = haf.InterFrame(video, GPU=False, NewNum=480, Preset="medium", Tuning="smooth", OverrideAlgo=13)
frame_gap = int(video.fps / 60)
blended_frames = int(frame_gap * 1.0)
if blended_frames > 0:
	if blended_frames % 2 == 0:
		blended_frames += 1
	weights = weighting.equal(blended_frames)
	video = core.frameblender.FrameBlend(video, weights, True)
video = haf.ChangeFPS(video, 60)
video.set_output()

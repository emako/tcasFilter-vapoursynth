import vapoursynth as vs

core = vs.core
src = core.lsmas.LibavSMASHSource(u'example.mp4')
src = core.tcax.TcasSub(src, file=u'example.tcas')
src.set_output()
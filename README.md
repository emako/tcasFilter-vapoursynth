# tcasFilter-vapoursynth
Rendering TCAS, a subtitle fx file ported from TCAX/Avisynth.

This is a submodule from https://github.com/emako/TCAX/tree/master/src/tcasFilter

Example script for VapourSynth
---
import vapoursynth as vs  
  
core = vs.get_core()  
src = core.lsmas.LibavSMASHSource(u'example.mp4')  
src = core.tcax.TcasSub(src, file=u'example.tcas')  
src.set_output()  

Example script for AviSynth
---
LoadPlugin("LSMASHSource.dll")  
LoadPlugin("tcasFilter.dll")  
  
LSMASHVideoSource("example.mp4")  
TcasSub("example.tcas")  
  
How to create a TCAS file
---
TCAX forum for more information.
  
**[TCAX Homepage]**  
http://tcax.org/
  
**[TCAS special effects tutorial]**  
http://tcax.org/forum.php?mod=viewthread&tid=220
  
**[Convert the image file to TCAS]**  
http://tcax.org/forum.php?mod=viewthread&tid=135

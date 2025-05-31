# Usage example script 
# Rights@
# Karlo Severinski 
# {University of Rijeka, Faculty of Maritime Studies}
# {The Center for Artificial Intelligence and Cybersecurity, University of Rijeka}
# -----------------------------------------------------------------------------
# This software is open access and may be used, modified, and distributed freely. 
# Please credit **Karlo Severinski** and the **University of Rijeka, Faculty of Maritime Studies** 
# as well as **The Center for Artificial Intelligence and Cybersecurity, University of Rijeka** as in 
# any derivative works or publications.
# -----------------------------------------------------------------------------

from VideoProcessor import VideoCutterLinear, VideoCutterSection, VideoCutterLinearFrame, VideoCutterSectionFrame, BatchVideoLoader, BatchVideoCutterLinear
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()
basepathLoad = os.getenv('BASEPATHLOAD')
videoName = os.getenv('VIDEONAME')
basepathSave = os.getenv('BASEPATHSAVE')
fileName = os.getenv('FILENAME')

"""
result = VideoCutterLinear(basepathLoad=basepathLoad,
                           videoName=videoName,
                           basepathSave=basepathSave,
                           fileName=fileName,
                           timeDiff=4,
                           )
"""
"""
result = VideoCutterSection(basepathLoad=basepathLoad,
                           videoName=videoName,
                           basepathSave=basepathSave,
                           fileName=fileName,
                           startTime=60,
                           endTime=120,
                           timeDiff=4,
                           )
"""
"""
result = VideoCutterLinearFrame(basepathLoad=basepathLoad,
                           videoName=videoName,
                           basepathSave=basepathSave,
                           fileName=fileName,
                           )

"""
"""
result = VideoCutterSectionFrame(basepathLoad=basepathLoad,
                           videoName=videoName,
                           basepathSave=basepathSave,
                           fileName=fileName,
                           startFrame=100,
                           endFrame=200
                           )
"""
"""
result = BatchVideoLoader(os.path.join(basepathLoad))
"""

result = BatchVideoCutterLinear(os.path.join(basepathLoad), os.path.join(basepathSave), timeDiff=20)

print(result)

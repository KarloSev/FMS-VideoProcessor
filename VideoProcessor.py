# -----------------------------------------------------------------------------
# This software is open access and may be used, modified, and distributed
# freely. Please credit Karlo Severinski and the University of Rijeka, Faculty
# of Maritime Studies, in any derivative works or publications.
# -----------------------------------------------------------------------------

import cv2
import os
import numpy as np

def VideoCutterLinear(basepathLoad, videoName, basepathSave, fileName, timeDiff = 2, Verbose = True):

    """
    Extracts frames from a video file at evenly spaced intervals and saves them as images.

    Parameters
    ----------
    basepathLoad : str
        The base path where the video file is located.
    videoName : str
        The name of the video file to be processed.
    basepathSave : str
        The base path where the extracted frames will be saved.
    fileName : str
        The name of the folder where the frames will be stored.
    timeDiff : int, optional
        The interval in seconds between consecutive frames to extract. Default is 2 seconds.
    Verbose : Bool, optional
        Iteration verbose printout, default is True.

    Returns
    -------
    str
        A message indicating the directory where the extracted frames have been saved.

    Raises
    ------
    ImportError
        If the video file could not be opened, an ImportError is raised with a detailed message.
    
    Example
    -------
    >>> VideoCutterLinear('/path/to/video', 'video.mp4', '/path/to/save', 'frames_folder', timeDiff=2)
    'Images saved at /path/to/save/frames_folder/99.jpg'
    """

    filepath = os.path.join(basepathLoad, videoName)
    fileSavePath = os.path.join(basepathSave, fileName)
    os.makedirs(fileSavePath, exist_ok=True)
    video = cv2.VideoCapture(filepath)
    if not video.isOpened():
        print("\033[31mVideo processor error message!\033[0m Error: Could not open video.")
        return ImportError(f"Error raised for processing video for path: \033[31m{filepath}\033[0m")
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    seconds = round(total_frames / fps)
    N = round(seconds / timeDiff)
    indices = np.linspace(0, total_frames - 1, N, dtype=int)
    print("\033[32mVideo processor message!\033[0m Indices:", indices.size)
    print("\033[32mVideo processor message!\033[0m Number of images:", N)
    print("\033[32mVideo processor message!\033[0m Number of seconds:", seconds)
    for i, idx in enumerate(indices):
        print("Iteration:", i)
        video.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = video.read()
        if ret:
            save_path = os.path.join(fileSavePath, f"{i}.jpg")
            cv2.imwrite(save_path, frame)
            if Verbose: print(f"\033[32mSaved frame at\033[0m {save_path}")
    video.release()
    return f"Images saved at \033[32m{os.path.join(basepathSave, fileName)}\033[0m"


def VideoCutterSection(basepathLoad, videoName, basepathSave, fileName, startTime, endTime, timeDiff = 2, Verbose = True):

    """
    Extracts frames from a video file at evenly spaced intervals between start time and end time, saves them as images.

    Parameters
    ----------
    basepathLoad : str
        The base path where the video file is located.
    videoName : str
        The name of the video file to be processed.
    basepathSave : str
        The base path where the extracted frames will be saved.
    fileName : str
        The name of the folder where the frames will be stored.
    startTime : int
        The start time of video cutting, in seconds.
    endTime : int
        The ned time of video cutting, in seconds.
    timeDiff : int, optional
        The interval in seconds between consecutive frames to extract. Default is 2 seconds.
    Verbose : Bool, optional
        Iteration verbose printout, default is True.

    Returns
    -------
    str
        A message indicating the directory where the extracted frames have been saved.

    Raises
    ------
    ImportError
        If the video file could not be opened, an ImportError is raised with a detailed message.
    
    Example
    -------
    >>> VideoCutterLinear('/path/to/video', 'video.mp4', '/path/to/save', 'frames_folder', 100, 200, timeDiff=2, True)
    'Images saved at /path/to/save/frames_folder/99.jpg'
    """

    filepath = os.path.join(basepathLoad, videoName)
    fileSavePath = os.path.join(basepathSave, fileName)
    os.makedirs(fileSavePath, exist_ok=True)
    video = cv2.VideoCapture(filepath)
    if not video.isOpened():
        print("\033[31mVideo processor error message!\033[0m Error: Could not open video.")
        raise ImportError(f"Error raised for processing video for path: \033[31m{filepath}\033[0m")

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    seconds = round(total_frames / fps)

    startCut = int(startTime * fps)
    endCut = int(endTime * fps)
    N = round((endTime - startTime) / timeDiff)
    indices = np.linspace(startCut, endCut - 1, N, dtype=int)

    print("\033[32mVideo processor message!\033[0m Indices:", indices.size)
    print("\033[32mVideo processor message!\033[0m Number of images:", N)
    print("\033[32mVideo processor message!\033[0m Number of seconds:", seconds)
    
    for i, idx in enumerate(indices):
        print("Iteration:", i)
        video.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = video.read()
        if ret:
            save_path = os.path.join(fileSavePath, f"{i}.jpg")
            cv2.imwrite(save_path, frame)
            if Verbose: print(f"\033[32mSaved frame at\033[0m {save_path}")
    video.release()
    return f"Images saved at \033[32m{os.path.join(basepathSave, fileName)}\033[0m"

def VideoCutterLinearFrame(basepathLoad, videoName, basepathSave, fileName, Verbose = True):

    """
    Extracts all frames from a video file  and saves them as images.

    Parameters
    ----------
    basepathLoad : str
        The base path where the video file is located.
    videoName : str
        The name of the video file to be processed.
    basepathSave : str
        The base path where the extracted frames will be saved.
    fileName : str
        The name of the folder where the frames will be stored.
    Verbose : Bool, optional
        Iteration verbose printout, default is True.

    Returns
    -------
    str
        A message indicating the directory where the extracted frames have been saved.

    Raises
    ------
    ImportError
        If the video file could not be opened, an ImportError is raised with a detailed message.
    
    Example
    -------
    >>> VideoCutterLinear('/path/to/video', 'video.mp4', '/path/to/save', 'frames_folder')
    'Images saved at /path/to/save/frames_folder/99.jpg'
    """

    filepath = os.path.join(basepathLoad, videoName)
    fileSavePath = os.path.join(basepathSave, fileName)
    os.makedirs(fileSavePath, exist_ok=True)
    video = cv2.VideoCapture(filepath)
    if not video.isOpened():
        print("\033[31mVideo processor error message!\033[0m Error: Could not open video.")
        raise ImportError(f"Error raised for processing video for path: \033[31m{filepath}\033[0m")
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    seconds = round(total_frames / fps)
    
    indices = np.linspace(0, total_frames - 1, total_frames, dtype=int)
    print("\033[32mVideo processor message!\033[0m Total frames:", indices.size)
    print("\033[32mVideo processor message!\033[0m Indices:", indices.size)
    print("\033[32mVideo processor message!\033[0m Number of images:", total_frames)
    print("\033[32mVideo processor message!\033[0m Number of seconds:", seconds)
    for i, idx in enumerate(indices):
        print("Iteration:", i)
        video.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = video.read()
        if ret:
            save_path = os.path.join(fileSavePath, f"{i}.jpg")
            cv2.imwrite(save_path, frame)
            if Verbose: print(f"\033[32mSaved frame at\033[0m {save_path}")
    video.release()
    return f"Images saved at \033[32m{os.path.join(basepathSave, fileName)}\033[0m"

def VideoCutterSectionFrame(basepathLoad, videoName, basepathSave, fileName, startFrame, endFrame, Verbose = True):

    """
    Extracts selected range of frames from a video file and saves them as images.

    Parameters
    ----------
    basepathLoad : str
        The base path where the video file is located.
    videoName : str
        The name of the video file to be processed.
    basepathSave : str
        The base path where the extracted frames will be saved.
    fileName : str
        The name of the folder where the frames will be stored.
    startFrame : int
        Frame to start exporting from.
    endFrame : int
        Frame to stop exporting at.
    Verbose : Bool, optional
        Iteration verbose printout, default is True.

    Returns
    -------
    str
        A message indicating the directory where the extracted frames have been saved.

    Raises
    ------
    ImportError
        If the video file could not be opened, an ImportError is raised with a detailed message.
    ValuesError
        If the start and end frame values are not supported by the video.
    
    Example
    -------
    >>> VideoCutterLinear('/path/to/video', 'video.mp4', '/path/to/save', 'frames_folder', 100, 200)
    'Images saved at /path/to/save/frames_folder/99.jpg'
    """

    filepath = os.path.join(basepathLoad, videoName)
    fileSavePath = os.path.join(basepathSave, fileName)
    os.makedirs(fileSavePath, exist_ok=True)
    video = cv2.VideoCapture(filepath)
    if not video.isOpened():
        print("\033[31mVideo processor error message!\033[0m Error: Could not open video.")
        raise ImportError(f"Error raised for processing video for path: \033[31m{filepath}\033[0m")
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    seconds = round(total_frames / fps)

    N = endFrame - startFrame

    if endFrame < total_frames and startFrame < total_frames and endFrame >= 0 and startFrame >= 0: 
         indices = np.linspace(startFrame, endFrame, N, dtype=int)
    else:
        raise ValueError(f"Error raised for processing video for input: \033[31m{endFrame}\033[0m and \033[31m{startFrame}\033[0m") 
    
    print("\033[32mVideo processor message!\033[0m Total frames:", total_frames)
    print("\033[32mVideo processor message!\033[0m Indices:", indices.size)
    print("\033[32mVideo processor message!\033[0m Number of images:", N)
    print("\033[32mVideo processor message!\033[0m Number of seconds:", seconds)

    for i, idx in enumerate(indices):
        print("Iteration:", i)
        video.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = video.read()
        if ret:
            save_path = os.path.join(fileSavePath, f"{i}.jpg")
            cv2.imwrite(save_path, frame)
            if Verbose: print(f"\033[32mSaved frame at\033[0m {save_path}")
    video.release()
    return f"Images saved at \033[32m{os.path.join(basepathSave, fileName)}\033[0m"

def BatchVideoLoader(folderPath):
    """
    Loads and returns the absolute paths of all video files within a given folder.

    Parameters
    ----------
    folderPath : str
        The path to the folder containing the video files.

    Returns
    -------
    list of str
        A list containing the absolute paths of all video files found in the given folder.
    
    Example
    -------
    >>> BatchVideoLoader('/path/to/videos')
    ['/abs/path/to/videos/video1.mp4', '/abs/path/to/videos/video2.avi']
    """
    files = list(os.walk(folderPath))
    abs_paths = [os.path.abspath(os.path.join(folderPath, file)) for file in files[0][2]]
    return abs_paths

def BatchVideoCutterLinear (folderPathLoad, folderPathSave, timeDiff = 2, Verbose = True):

    """
    Extracts frames from multiple video files at evenly spaced intervals and saves them as images.

    Parameters
    ----------
    folderPathLoad : str
        The path where the video files is located.
    folderPathSave : str
        The path where the image files are going to be saved.
    timeDiff : int, optional
        The interval in seconds between consecutive frames to extract. Default is 2 seconds.
    Verbose : Bool, optional
        Iteration verbose printout, default is True.

    Returns
    -------
    str
        A message indicating the directories where the extracted frames have been saved.
    
    Example
    -------
    >>> BatchVideoCutterLinear('/path/to/video', '/path/to/save', timeDiff=2)
    'Images saved at /path/to/save/frames_folder1'
    'Images saved at /path/to/save/frames_folder2'
    'Images saved at /path/to/save/frames_folder3'
    """

    videos = BatchVideoLoader(folderPathLoad)

    directory = os.path.dirname(videos[0])
    videoNames = [os.path.basename(path) for path in videos]

    print(videoNames)
    print(directory)
    result = ''

    for videoName in videoNames:
        result = result + '\n' + VideoCutterLinear(directory, videoName, folderPathSave, videoName.rsplit('.', 1)[0], timeDiff, Verbose = True)

    return result

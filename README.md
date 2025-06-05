# VideoCutter Utility

This project provides several Python functions to extract frames from videos in different ways. This video cutter is made for use in computer vision research as a data science processing tool for faster and simpler image extraction from videos. It uses the OpenCV library to handle video processing and supports a variety of cutting options. The library will expand over time when the need for new functions appears.

---

## Functions Overview

### 1️⃣ VideoCutterLinear

Extracts frames at evenly spaced intervals throughout the entire video.

**Parameters:**

* `basepathLoad`: Path to the video file.
* `videoName`: Video file name.
* `basepathSave`: Path to save the extracted frames.
* `fileName`: Name of the folder for saving frames.
* `timeDiff`: Interval in seconds between frames (default: 2).
* `Verbose`: Verbose output (default: True).

**Example:**

```python
VideoCutterLinear('/path/to/video', 'video.mp4', '/path/to/save', 'frames_folder', timeDiff=2)
```

### 2️⃣ VideoCutterSection

Extracts frames at evenly spaced intervals between two timestamps.

**Parameters:**

* Same as above, plus:
* `startTime`: Start time in seconds.
* `endTime`: End time in seconds.

**Example:**

```python
VideoCutterSection('/path/to/video', 'video.mp4', '/path/to/save', 'frames_folder', 100, 200, timeDiff=2)
```

### 3️⃣ VideoCutterLinearFrame

Extracts **all** frames from the video.

**Example:**

```python
VideoCutterLinearFrame('/path/to/video', 'video.mp4', '/path/to/save', 'frames_folder')
```

### 4️⃣ VideoCutterSectionFrame

Extracts frames between two frame indices.

**Parameters:**

* Same as above, plus:
* `startFrame`: Starting frame index.
* `endFrame`: Ending frame index.

**Example:**

```python
VideoCutterSectionFrame('/path/to/video', 'video.mp4', '/path/to/save', 'frames_folder', 100, 200)
```

### 5️⃣ BatchVideoLoader

Loads and returns the absolute paths of all video files within a given folder.

**Parameters:**

* `folderPath`: Path to the folder containing video files.

**Returns:**

* A list of absolute paths to video files in the folder.

**Example:**

```python
BatchVideoLoader('/path/to/videos')
```

### 6️⃣ BatchVideoCutterLinear

Extracts frames from multiple video files at evenly spaced intervals and saves them as images.

**Parameters:**

* `folderPathLoad`: Path to the folder containing video files.
* `folderPathSave`: Path where the extracted images will be saved.
* `timeDiff`: Interval in seconds between consecutive frames to extract. Default is 2.
* `Verbose`: If True, prints progress during execution. Default is False.

**Returns:**

* A message string indicating the directories where images have been saved.

**Example:**

```python
BatchVideoCutterLinear('/path/to/videos', '/path/to/save', timeDiff=2, Verbose=True)
```

### 7️⃣ BatchImageRename

Renames all image files in a folder, optionally shuffling them, and saves them into a 'Renamed' subfolder with a sequential naming pattern.

**Parameters:**

* `folderPath`: Path to the folder containing image files to be renamed.
* `prefix`: A prefix to prepend to each new image file name. Default is an empty string.
* `shuffle`: If True, image files will be renamed in a shuffled order. Default is False.

**Returns:**

* A list of dictionaries with keys `'old'` and `'new_name'`, representing original absolute paths and their corresponding new file names.

**Example:**

```python
BatchImageRename('/path/to/images', prefix='img_', shuffle=True)
```

---

## License

This software is open access and may be used, modified, and distributed freely. Please credit **Karlo Severinski** and the **University of Rijeka, Faculty of Maritime Studies** as well as **The Center for Artificial Intelligence and Cybersecurity, University of Rijeka** as  in any derivative works or publications.

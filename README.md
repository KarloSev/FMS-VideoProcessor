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

---

## License

This software is open access and may be used, modified, and distributed freely. Please credit **Karlo Severinski** and the **University of Rijeka, Faculty of Maritime Studies** as well as **The Center for Artificial Intelligence and Cybersecurity, University of Rijeka** as  in any derivative works or publications.

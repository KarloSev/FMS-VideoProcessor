import os
import random
import re
import cv2

def BatchImageRename(folderPath, prefix='', shuffle = False):

    """
    Renames all image files in a folder, optionally shuffling them, and saves them into a 'Renamed' subfolder 
    with a sequential naming pattern.

    Parameters
    ----------
    folderPath : str
        The path to the folder containing image files to be renamed.
    prefix : str, optional
        A prefix to prepend to each new image file name (default is '').
    shuffle : bool, optional
        Whether to randomly shuffle the image files before renaming (default is False).

    Returns
    -------
    list of dict
        A list of dictionaries with keys 'old' and 'new_name', mapping each original file's absolute path to its new name.

    Example
    -------
    >>> BatchImageRename('/path/to/images', prefix='img_', shuffle=True)
    [{'old': '/path/to/images/image1.jpg', 'new_name': 'img_0.jpg'}, 
     {'old': '/path/to/images/image2.jpg', 'new_name': 'img_1.jpg'}, 
     ...]
    """

    files = list(os.walk(folderPath))
    imageNames = files[0][2]

    if(shuffle): 
        secure = random.SystemRandom()
        secure.shuffle(imageNames) # Shuffle names
    else:
        imageNames.sort(key=lambda x: (int(m.group()) if (m := re.search(r'\d+', x)) else float('inf'), x.lower())) # Sort by numbers and alphabetically

    renamed_dir = os.path.join(folderPath, "Renamed")
    os.makedirs(renamed_dir, exist_ok=True)  # Create the folder
    
    abs_paths = [os.path.abspath(os.path.join(folderPath, file)) for file in imageNames]
    mapped_paths = []
    for i, abs_path in enumerate(abs_paths):
        image = cv2.imread(abs_path)
        cv2.imwrite(os.path.join(os.path.dirname(abs_path), f"Renamed", f"{prefix}{i}.jpg"), image)
        mapped_paths.append({"old": abs_path, "new_name": f"{prefix}{i}.jpg"})

    return mapped_paths


def RandomSplit(folderPath, split):

    files = list(os.walk(folderPath))
    imageNames = files[0][2]

    secure = random.SystemRandom()
    secure.shuffle(imageNames)

    image_split_num = round(len(imageNames)*split)

    split_A = imageNames[:image_split_num]
    split_B = imageNames[image_split_num:]

    abs_paths_A = [os.path.abspath(os.path.join(folderPath, file)) for file in split_A]
    abs_paths_B = [os.path.abspath(os.path.join(folderPath, file)) for file in split_B]

    print(abs_paths_A)
    print(abs_paths_B)

    split_A_dir = os.path.join(folderPath, "Split_A")
    os.makedirs(split_A_dir, exist_ok=True)  # Create the folder

    split_B_dir = os.path.join(folderPath, "Split_B")
    os.makedirs(split_B_dir, exist_ok=True)  # Create the folder

    for i, abs_path_A in enumerate(abs_paths_A):
        image = cv2.imread(abs_path_A)
        cv2.imwrite(os.path.join(os.path.dirname(abs_path_A), f'Split_A', os.path.basename(abs_path_A)), image)

    for i, abs_path_B in enumerate(abs_paths_B):
        image = cv2.imread(abs_path_B)
        cv2.imwrite(os.path.join(os.path.dirname(abs_path_B), f'Split_B', os.path.basename(abs_path_B)), image)

    return 0
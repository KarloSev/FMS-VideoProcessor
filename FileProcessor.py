import os
import random
import re
import cv2

def BatchImageRename(folderPath, prefix='', shuffle = False):

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
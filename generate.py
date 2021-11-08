from sys import argv

import cv2
import numpy as np
import matplotlib.pyplot as plt

def to_hex(arr):
    return arr[0] * 0x000001 + arr[1] * 0x000100 + arr[2] * 0x010000


imArray = cv2.imread('laser.png')
color_data = []
frames = []
for frame in range(0, len(imArray), 8):
    colors = set()
    # actual frame open
    color_data.append([])
    frames.append([])
    for col in range(0, len(imArray[frame])):
        for row in range(frame, frame + 8):
            hex_val = to_hex(imArray[row][col])
            if hex_val:
                colors.add(hex_val)
    for color in colors:
        # color data open
        frames[-1].append([])
        color_data[-1].append(hex(color))
        for col in range(0, len(imArray[frame])):
            num_represent = 0
            for row in range(frame, frame + 8):
                hex_color = to_hex(imArray[row][col])
                num_represent += 2 ** (row - frame) if hex_color == color else 0
                frames[-1][-1].append(hex(num_represent))


with open("code.txt", "w") as f:
    def default_print(*args, **kwargs):
        print(*args, **kwargs)

    def print(value):
        default_print(value, file=f)

    
#     print(f'''
# vector<vector<vector<uint8_t>>> frameData {frames}
# vector<vector<int>> colorData {color_data}

# frame %= frameData.size()

# vector<*ColorData> colorDataVector;
# for(size_t i = 0; i < colorData[frame].size(); ++i) {{
#     ColorData cd;
#     colorArr = uint8_t[32];
#     std::copy(frameData[frame][i].begin(), frameData[frame][i].end(), colorArr);
#     ColorData_init(cd, colorData[frame][i], colorArr);
#     display_color_data(cd);
# }}
# ''', file=f)



    print(f'frame %= {len(frames)};')
    for frame in frames:
        for color in color_data:
            pass

import cv2
import numpy as np


def remember(path):
    img = cv2.imread(path, 0)
    mid_color = int(np.median(img) * 0.8)
    return ''.join(chr(row) for col in range(img.shape[1]) for row in range(img.shape[0]) if img[row][col] < mid_color)


if __name__ == '__main__':
    print(remember("C:/Users/user/Downloads/code.png"))

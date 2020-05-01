import cv2
import numpy as np
import os

def crop_and_resize(img, resize_size):
    w = img.shape[0]
    h = img.shape[1]
    crop_size = min(w, h)
    img = img[int(w/2-crop_size/2):int(w/2+crop_size/2), int(h/2-crop_size/2):int(h/2+crop_size/2)]

    img = cv2.resize(img, (resize_size, resize_size))
    cv2.imwrite("test.png", img)

    return img

def combine(target, inputs, inputs_size, per_pixel):
    w = target.shape[0]
    h = target.shape[1]

    print(inputs[0].shape)
    output = np.zeros((w * inputs_size // per_pixel, h * inputs_size // per_pixel, 3))
    inputs_len = len(inputs)
    r = 0
    t = 0
    for i in range(h // per_pixel):
        for j in range(w // per_pixel):
            output[r:r + inputs_size, t:t+inputs_size] = inputs[(i * h + w) % inputs_len]
            r += inputs_size
        t += inputs_size
        r = 0
    
    cv2.imwrite("test1.png", output)

    return output
    

target = cv2.imread("target.png")
print(target.shape)
combine(target, [crop_and_resize(cv2.imread("jayinnn.jpg"), 200)], 200, 40)
# inputs = []

# for path in os.listdir("input"):
#     inputs.append(cv2.imread(os.path.join("input", path))
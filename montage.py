import cv2
import numpy as np
import os
import random

def adjust_color(img, b, g, r):
    # print(b, g, r)
    tmp_img = img / 256
    tmp_img[:, :, 0] = tmp_img[:, :, 0] ** (1 - b / 255)
    tmp_img[:, :, 1] = tmp_img[:, :, 1] ** (1 - g / 255)
    tmp_img[:, :, 2] = tmp_img[:, :, 2] ** (1 - r / 255)
    

    tmp_img = tmp_img * 256

    return tmp_img.astype('int32')

def crop_and_resize(img, resize_size):
    w = img.shape[0]
    h = img.shape[1]
    crop_size = min(w, h)
    img = img[int(w/2-crop_size/2):int(w/2+crop_size/2), int(h/2-crop_size/2):int(h/2+crop_size/2)]

    img = cv2.resize(img, (resize_size, resize_size))

    return img

def combine(target, inputs, inputs_size, per_pixel):
    w = target.shape[0]
    h = target.shape[1]

    print(inputs[0].shape)
    output = np.zeros((w * inputs_size // per_pixel, h * inputs_size // per_pixel, 3))
    inputs_len = len(inputs)
    r = 0
    t = 0
    idx = 0
    for i in range(h // per_pixel):
        for j in range(w // per_pixel):
            output[r:r + inputs_size, t:t+inputs_size] = adjust_color(inputs[idx % inputs_len], 
            target[j * per_pixel,i * per_pixel,0], target[j * per_pixel,i * per_pixel,1], target[j * per_pixel,i * per_pixel,2])
            r += inputs_size
            idx += 1
        t += inputs_size
        r = 0
    
    return output


if __name__ == "__main__":

    # ========= PARAMETERS =========
    use_shuffle = True
    inputs_limit = -1 # -1 for not limited
    img_size = 200
    pixel_per_img = 5
    # ==============================

    inputs = []
    for item in os.listdir("input"):
        if(inputs_limit != -1 and len(inputs) >= inputs_limit):
            break
        try:
            print("load {} successfully.".format(item))
            inputs.append(crop_and_resize(cv2.imread(os.path.join("input", item)), img_size))
        except:
            print("{} is not an image.".format(item))
    if use_shuffle:
        random.shuffle(inputs)

    print("complete load inputs image.")
    target = cv2.imread("target.jpg")
    output = combine(target, inputs, img_size, pixel_per_img)

    cv2.imwrite("output.png", output)
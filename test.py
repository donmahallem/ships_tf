from os.path import isfile, join
from os import listdir
import numpy as np
import cv2 as cv


def show(img, wait=True):
    cv.imshow("JJ", img)
    cv.waitKey(0 if wait == True else 1)


def normalize(img):
    vmax = np.max(img)
    vmin = np.min(img)
    return (img-vmin)*1.0/(vmax-vmin)


def asdf5(img):
    ssize = 512
    # img = cv.resize(img, (ssize, ssize), interpolation=cv.INTER_CUBIC)
    hlsimg = cv.cvtColor(img, cv.COLOR_BGR2HLS)
    kernel_size = min(128, round(min(img.shape[0], img.shape[1])/50))
    # print(kernel_size)
    hlsimg = cv.blur(hlsimg, (kernel_size, kernel_size))  # .astype(np.float32)
    # show(hlsimg[:, :, 1])
    luminance_img = np.zeros((img.shape), dtype=np.uint8)
    exp_img = normalize((hlsimg[:, :, 1]/255.)**2)*-255+255  # *255  # +255
    # show(exp_img)
    exp_img = exp_img.astype(np.uint8)
    thresh1 = cv.adaptiveThreshold(exp_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv.THRESH_BINARY, 15, 0)
    #ret, thresh1 = cv.threshold(exp_img, 150, 255, cv.THRESH_BINARY)
    # print(np.max(thresh1), thresh1.dtype)
    # show(exp_img)
    # print(ret, thresh1.shape)
    # print(np.min(hlsimg[:, :, 1]), np.max(hlsimg[:, :, 1]))
    # show(thresh1)
    luminance_img[:, :, 0] = luminance_img[:,
                                           :, 1] = luminance_img[:, :, 2] = exp_img
    contours, hierarchy = cv.findContours(
        thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    ll = -1
    lls = -1
    for idx in range(0, len(contours)):
        c = contours[idx]
        #print("CC", len(c))
        if len(c) > lls:
            ll = idx
            lls = len(c)
    # luminance_img
    out = np.zeros(img.shape, dtype=np.uint8)
    # out += 255
    cv.fillPoly(out, pts=[contours[ll]], color=(255, 255, 255))

    # show(cv.resize(out, (ssize, ssize), interpolation=cv.INTER_CUBIC))
    # out = cv.blur(out, (kernel_size, kernel_size))
    out2 = np.zeros(img.shape, dtype=np.uint8)
    out2[:, :, :] += 255
    out2 = out2-out
    out2 = out2+(out/255.*img)
    # out2 += (img*(out/255.)).astype(np.uint8)  # np.add(img, out)  # +500
    #show(cv.resize(out2, (ssize, ssize), interpolation=cv.INTER_CUBIC))
    # print(np.max(out))
    # out2 += out*8
    out2 = np.clip(out2, 0, 255)
    # out2 = (img*(out*1./255.0)).astype(np.uint8)

    # cv.copyTo(img, out2, mask=out)
    # out2 = img
    # out2 += out
    # out2 = np.clip(out2, 0, 255)
    return out2.astype(np.uint8)


mypath = "./imgs"
onlyfiles = [f for f in listdir(mypath) if (
    isfile(join(mypath, f)) and f[-4:] == ".jpg")]

print(onlyfiles)
for testfile in onlyfiles:
    img = cv.imread(join(mypath, testfile))
    ssize = 512
    im3 = asdf5(img)
    im4 = cv.resize(im3, (ssize, ssize), interpolation=cv.INTER_CUBIC)

    # im3 = cv.resize(a, (ssize, ssize), interpolation=cv.INTER_CUBIC)
    # im3 = cv2.drawContours(im2, contours, -1, (0, 255, 255), 3)
    show(im4, False)
    cv.imwrite(join("./outimg", testfile), im3)

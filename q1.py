from skimage import io
import numpy as np


def increase_contrast(I, a, b, struct_elem_w, struct_elem_h):
    opening = morph_open(I, struct_elem_w, struct_elem_h)
    closing = morph_close(I, struct_elem_w, struct_elem_h)
    # I_contrast = I + a * (I-open) - b * (close - I)
    # how the equation given above increases the contrast of images.
    contrast_img = I.astype(int) + a * (I.astype(int) - opening.astype(int)) - b * (closing.astype(int) - I.astype(int))
    # return the result image
    return np.clip(contrast_img, 0, 255).astype(np.uint8)


def decrease_contrast(I, struct_elem_w, struct_elem_h):
    opening = morph_open(I, struct_elem_w, struct_elem_h)
    closing = morph_close(I, struct_elem_w, struct_elem_h)
    # I_contrast = I - (I-open) + (close - I)
    contrast_img = I.astype(int) - (I.astype(int) - opening.astype(int)) + (closing.astype(int) - I.astype(int))
    # return the result image
    return np.clip(contrast_img, 0, 255).astype(np.uint8)


def dilate(im, struct_elem_w, struct_elem_h):
    x, y, rgb = im.shape
    from_around_px_x = -(struct_elem_w - 1) // 2
    to_around_px_x = ((struct_elem_w - 1) // 2) + 1
    from_around_px_y = -(struct_elem_h - 1) // 2
    to_around_px_y = ((struct_elem_h - 1) // 2) + 1
    res_img = np.zeros((x, y, 3))
    for c in range(rgb):
        for i in range(x):
            for j in range(y):
                max_pixel = 0
                for k in range(from_around_px_x, to_around_px_x):
                    for l in range(from_around_px_y, to_around_px_y):
                        if 0 > i + k or i + k >= x or 0 > j + l or j + l >= y:
                            continue
                        test_pixel = float(im[i + k, j + l, c])
                        if max_pixel < test_pixel:
                            max_pixel = test_pixel
                res_img[i, j, c] = max_pixel
    return res_img


def erode(im, struct_elem_w, struct_elem_h):
    x, y, rgb = im.shape
    from_around_px_x = -(struct_elem_w - 1) // 2
    to_around_px_x = ((struct_elem_w - 1) // 2) + 1
    from_around_px_y = -(struct_elem_h - 1) // 2
    to_around_px_y = ((struct_elem_h - 1) // 2) + 1
    res_img = np.zeros((x, y, 3))
    for c in range(rgb):
        for i in range(x):
            for j in range(y):
                min_pixel = 255
                for k in range(from_around_px_x, to_around_px_x):
                    for l in range(from_around_px_y, to_around_px_y):
                        if 0 > i + k or i + k >= x or 0 > j + l or j + l >= y:
                            continue
                        test_pixel = float(im[i + k, j + l, c])
                        if min_pixel > test_pixel:
                            min_pixel = test_pixel
                res_img[i, j, c] = min_pixel
    return res_img


def morph_open(im, struct_elem_w, struct_elem_h):
    return dilate(erode(im, struct_elem_w, struct_elem_h), struct_elem_w, struct_elem_h)


def morph_close(im, struct_elem_w, struct_elem_h):
    return erode(dilate(im, struct_elem_w, struct_elem_h), struct_elem_w, struct_elem_h)


def show_img(im):
    io.imshow(im)
    io.show()


# question 1 tests
img = io.imread('Mars.jpg')
show_img(img)

# output image with a square structuring element of size 3 x 3 when a = 1 and b = 1
manipulated_img = increase_contrast(img, 1, 1, 3, 3)
show_img(manipulated_img)

# output image with a square structuring element of size 9 x 9 when a = 1 and b = 1
manipulated_img = increase_contrast(img, 1, 1, 9, 9)
show_img(manipulated_img)

# output image with a square structuring element of size 3 x 3 when a = 5 and b = 1
manipulated_img = increase_contrast(img, 5, 1, 3, 3)
show_img(manipulated_img)

# output image with a square structuring element of size 3 x 3 when a = 1 and b = 5
manipulated_img = increase_contrast(img, 1, 5, 3, 3)
show_img(manipulated_img)

manipulated_img = decrease_contrast(img, 3, 3)
show_img(manipulated_img)

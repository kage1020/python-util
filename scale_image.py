import cv2

img_path = 'sample.png'
out_path = 'out.png'
img = cv2.imread(img_path)
scale = 16

# scale image with nearest neighbor interpolation
out = cv2.resize(
        img,
        ( int(img.shape[1] * scale), int(img.shape[0] * scale) ),
        interpolation=cv2.INTER_NEAREST
    )

cv2.imwrite(out_path, out)

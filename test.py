import qrcode
from PIL import Image
import cv2 as cv


img = qrcode.make('hello my name is farai')
print(img)
# ######
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )
# ########
# qr.add_data('hello my name is farai')
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# img.save("sample2.png")


# im = cv.imread('sample2.png')
# det = cv.QRCodeDetector()
# retval, points, straight_qrcode = det.detectAndDecode(im)
# print(retval)
# print(points)
# print(straight_qrcode)
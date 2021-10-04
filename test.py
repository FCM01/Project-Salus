import qrcode
from PIL import Image
import cv2 as cv
from microfunction import tools

# img = qrcode.make('hello my name is farai')
# print(img)
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


data = {"name":"farai","surname":"matyukira"}
user_number  = 81291821 
qr = tools()
token = qr.generate_token(data,user_number)
create = token[1]
image = create.make_image(fill_color="black", back_color="white").convert('RGB')
image.save("QRcodes/test1.png")



im = cv.imread("QRcodes/test1.png")
det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)
message  = retval 

split_point = 0
split_point2 = 0
for i in range (0,len(message)):

    if message[i] == ",":
        split_point = i 
    if message[i] == ";":
        split_point2 = i 
## name
name  = ""
for i  in range (0,split_point):
    name = name + message[i] 
##user_number
user_number = ""
for i in range (split_point + 1,split_point2):
    user_number = user_number + message[i]
## date of creation
date_of_creation = ""
for i in range (split_point2 + 1,len(message)):
    date_of_creation = date_of_creation + message[i]

print(name)
print(user_number)
print(date_of_creation)

# print(straight_qrcode)
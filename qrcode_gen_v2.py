# Importing library
import qrcode

# Data to encode
data = "https://https://github.com/janicemv/"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = '#17345A',
                    back_color = 'white')

img.save('QRcode_Github_blue.svg')

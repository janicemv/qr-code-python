# Importing library
import qrcode

# Encoding data using make() function
img = qrcode.make("https://www.linkedin.com/in/janicevilela/")

# Saving as an image file
img.save('QRcode_LinkedIn.png')
# pip install pillow
# pip install qrcode

import qrcode

# link for website

link = "https://fabriziocominetti.github.io/"

# creating an instance of qrcode

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qrcodeFC.png')
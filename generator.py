import qrcode
import os 
from PIL import Image

def main():
    # query user for link to be encoded
    link = input('Enter link to be encoded: ')

    while True:
        path_query = input('Do you have an image to upload? (y/n): ').lower()
        if path_query == 'y': 
            image_path = input('Enter image path: ')

            # validate that the path exists
            if not os.path.exists(image_path): 
                print('\nInvalid path. Please try again')
            else:
                while True: 
                    color_query = input('Would you like the photo to keep its color? (y/n): ')            
                    if color_query == 'y': 
                        keep_img_color = True
                        break
                    elif color_query == 'n': 
                        keep_img_color = False
                        break
                    else: 
                        print('\nInvalid input. Please try again')
                break
        elif path_query == 'n':
            image_path = ''
            keep_img_color = False
            break
        else: 
            print('\nInvalid input. Please try again')

    # pass information to qr code creation function 
    createQRCode(link, image_path, keep_img_color)
    
def createQRCode(data, image_path, keep_img_color): 
    """Create and save the QR Code."""

    # create a qr code object
    qr = qrcode.QRCode(
        # version # corresponds to the number of small modules/squares in the code
        # the higher the version number, the larger the QR code will be
        version=3, 

        # controls the size of each module in the QR code
        box_size=20,
        
        border=2, 

        # error correction has 4 levels (L, M, Q, H)
        # the higher the error correction level, the more data can be recovered if the QR code is damaged
        # higher levels of error correction require more modules, which means the QR code needs to be larger to be scannable
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # add link to the qr code object
    qr.add_data(data)

    # make the QR code 
    qr.make(fit=True)
        
    if keep_img_color: 
        # create an image from the qr code with a black fill color and white background, preserve image color when added 
        img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    else: 
        img = qr.make_image(fill_color="black", back_color="white")

    if not image_path: 
        # save the QR code image
        img.save("qr_code.png")
    else: 
        # open the image file
        logo = Image.open(image_path)
        
        # position the logo in the center of the QR code
        img_w, img_h = img.size
        logo_w, logo_h = logo.size
        pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)

        # paste the logo or image onto the QR code
        img.paste(logo, pos)

        # save the qr code image with logo
        img.save("qr_code_with_logo.png")
    
    # update user
    print('QR code successfully saved')
main()

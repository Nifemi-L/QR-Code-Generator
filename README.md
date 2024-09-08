# QR Code Generator

This is a Python tool that creates QR codes from user-provided links, with the option to embed a logo or image. 

## Features
- Generate a QR code from any link.
- Optionally embed an image or logo in the QR code.
- Choose whether to retain the image's original colors.
- Save the final QR code as a PNG image.

## Requirements
- Python 3.x
- Required libraries: `qrcode`, `Pillow`

Install the dependencies with:
```bash
pip install qrcode
```
```bash
pip install pillow
```

## Usage
Run the script:
```bash
python generator.py
```
1. Enter the link to encode.
2. Choose whether to embed an image.
3. If embedding an image, select if you'd like to keep the image's colors.
4. The QR code is saved as either `qr_code.png` or `qr_code_with_logo.png`.

## Example
```bash
Enter link to be encoded: https://example.com
Do you have an image to upload? (y/n): y
Enter image path: /path/to/image.png
Would you like the photo to keep its color? (y/n): y
```

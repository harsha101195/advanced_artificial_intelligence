import qrcode
from PIL import Image

def generate_qr(url, filename="qrcode.png"):
    # Create a qrcode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    # Provide data
    qr.add_data(url)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    # Open the image
    img = Image.open(filename)
    img.show()

if __name__ == "__main__":
    url = input("Enter the URL to generate QR code: ")
    generate_qr(url)
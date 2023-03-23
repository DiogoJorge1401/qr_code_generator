import os
import qrcode


def generate_qrcode(text: str):
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.ERROR_CORRECT_L, box_size=10, border=4
    )
    qr.add_data(text)
    qr.make()
    img = qr.make_image(fill_color="#4B0082", back_color="#FFFFE0")
    img.save("qrimg.png")


if __name__ == "__main__":
    url = input("Enter your url: ")
    generate_qrcode(url)
    image_path = os.path.join(os.getcwd(), "qrimg.png")
    print("Your QR code is saved at:", image_path)

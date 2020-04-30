
import base64
from PIL import Image
from PIL import ImageGrab
import pyperclip
from io import BytesIO

im = ImageGrab.grabclipboard()


def pil_base64(image):
    img_buffer = BytesIO()
    w, h = image.size
    # image.thumbnail((128, 128))
    image.save(img_buffer, format='JPEG', quality=95)
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


if isinstance(im, Image.Image):
    # print(im.format, im.size, im.mode)
    px = im.load()
    msg = str(pil_base64(im))
    msg = 'data:image/png;base64,' + msg[2:-2]
    print(msg)
    pyperclip.copy(msg)

else:
    pass


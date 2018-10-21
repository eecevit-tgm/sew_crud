"""
.. module:: encoder
   :synopsis: Restful User-Service image encoder
.. moduleauthor:: Ecevit Emre Okan <github.com/eecevit-tgm>

"""
import base64

def encode(file):
    """
    A base64 encoder for Images

    :param file: Path of the Image which should be encoded. !IMPORTANT! file ending e.g.: eecevit.jpg
    :return: the encoded Image as base64 String
    """
    with open(file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string

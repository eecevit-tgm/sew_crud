import base64



def encode(file):
    with open(file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string



# Saída da imagem que é convertida em string usando Base64
import base64

with open("image/flower.jpg", "rb") as image2string:
    converted_string =  base64.b64encode(image2string.read())
print(converted_string)

with open("encode.py", "wb") as file:
    file.write(converted_string)
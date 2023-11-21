from PIL import Image
import base64
from io import BytesIO

# Lê a imagem original
with open('image/borboleta.jpg', 'rb') as file:
    image_bytes = file.read()

# Codifica a imagem para base64
base64_string = base64.b64encode(image_bytes).decode('utf-8')

# Decodifica a string base64 para bytes
decoded_bytes = base64.b64decode(base64_string)

# Cria uma nova imagem a partir dos bytes decodificados
decoded_image = Image.open(BytesIO(decoded_bytes))

# Exibe a nova imagem   
decoded_image.show()

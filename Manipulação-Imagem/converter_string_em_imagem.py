import base64

file = open('image/encode.bin', 'rb')
byte = file.read()
file.close()

decodeit = open('image/flower2.jpg', 'wb')
decodeit.write(base64.b64encode(byte))
decodeit.close()
from PIL import Image

def encode_text(image_path, text, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    binary_text = ''.join(format(ord(char), '08b') for char in text) + '11111111'
    binary_idx = 0

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            if binary_idx < len(binary_text):
                pixels[i, j] = (r & ~1 | int(binary_text[binary_idx]), g, b)
                binary_idx += 1
            else:
                break
    img.save(output_path)

encode_text("input.jpg", "Secret Message", "output.png")

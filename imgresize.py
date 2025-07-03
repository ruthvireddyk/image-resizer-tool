import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 600)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                img_resized = img.resize(size)
                save_path = os.path.join(output_folder, filename)
                img_resized.save(save_path)
                print(f"Resized and saved: {save_path}")

resize_images("input_images", "output_images", size=(800, 600))

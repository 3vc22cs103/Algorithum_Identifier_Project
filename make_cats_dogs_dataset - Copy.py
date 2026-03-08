import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

base_dir = "cats_dogs_dataset"
os.makedirs(base_dir, exist_ok=True)

categories = ["cats", "dogs"]
num_images = 10

# Create category folders
for cat in categories:
    os.makedirs(os.path.join(base_dir, cat), exist_ok=True)

def create_image(filepath, label, color):
    img = Image.new("RGB", (128, 128), color=color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((40, 55), label, fill=(255, 255, 255), font=font)
    img.save(filepath, "JPEG")

rows = []
colors = {
    "cats": (150, 50, 50),  # reddish
    "dogs": (50, 50, 150)   # bluish
}

for cat in categories:
    for i in range(1, num_images + 1):
        filename = f"{cat}{i}.jpg"
        filepath = os.path.join(base_dir, cat, filename)
        create_image(filepath, cat[:-1].upper(), colors[cat])
        rows.append([f"{cat}/{filename}", cat[:-1]])

# Save labels.csv
labels_df = pd.DataFrame(rows, columns=["filename", "target"])
labels_df.to_csv(os.path.join(base_dir, "labels.csv"), index=False)

print("Cats vs Dogs dataset created successfully!")

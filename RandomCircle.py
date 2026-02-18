import random
from PIL import Image, ImageDraw

def random_circle_position(image_width, image_height, circle_radius):
    """
    Generate a random position (x, y) for a circle within the image boundaries.
    """
    x = random.randint(circle_radius, image_width - circle_radius)
    y = random.randint(circle_radius, image_height - circle_radius)
    return (x, y)

# === CONFIG ===
circle_r = 100
original_path = "OriginalImage.png"
preview_path = "OriginalImage_with_circle.png"
mask_path = "mask.png"

# 1) Load original image
original = Image.open(original_path).convert("RGBA")
W, H = original.size

# 2) Pick random position
position = random_circle_position(W, H, circle_r)

# 3) Draw opaque circle on a preview image (for you)
preview = original.copy()
draw_preview = ImageDraw.Draw(preview)
draw_preview.ellipse(
    (
        position[0] - circle_r,
        position[1] - circle_r,
        position[0] + circle_r,
        position[1] + circle_r,
    ),
    fill=(255, 0, 0, 255),   # solid red
)
preview.save(preview_path)
print(f"✅ Preview with opaque circle saved as {preview_path}")

# 4) Create DALL·E mask:
#    - White = protected
#    - Transparent circle = area DALL·E can change
mask = Image.new("RGBA", (W, H), (255, 255, 255, 255))
draw_mask = ImageDraw.Draw(mask)
draw_mask.ellipse(
    (
        position[0] - circle_r,
        position[1] - circle_r,
        position[0] + circle_r,
        position[1] + circle_r,
    ),
    fill=(0, 0, 0, 0),   # transparent
)
mask.save(mask_path)
print(f"✅ Mask for DALL·E saved as {mask_path}")
print(f"   Circle center: {position}, radius: {circle_r}")

# 5) Save data for Python version (if you still want it)
with open("game_data.txt", "w") as f:
    f.write(f"{position[0]},{position[1]},{circle_r}")

# 6) Save data for the browser (JS)
with open("game_data.js", "w") as f:
    f.write(
        "const circleData = "
        f"{{ x: {position[0]}, y: {position[1]}, r: {circle_r}, "
        f"imgWidth: {W}, imgHeight: {H} }};\n"
    )

print("✅ game_data.txt and game_data.js written!")

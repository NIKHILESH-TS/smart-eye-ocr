import cv2
import numpy as np
import pytesseract
import os


# --------------------------------------------------
# 1. Tesseract configuration
# --------------------------------------------------

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# --------------------------------------------------
# 2. Load input image
# --------------------------------------------------

image = cv2.imread("sample/input.jpeg")

if image is None:
    raise FileNotFoundError("Could not load sample/input.jpeg")

print("Image loaded successfully")
print("Image shape:", image.shape)


# --------------------------------------------------
# 3. Define four corners of the sign
# --------------------------------------------------

points = [
    (465, 585),   # top-left
    (750, 565),   # top-right
    (755, 730),   # bottom-right
    (465, 750)    # bottom-left
]


# --------------------------------------------------
# 4. Perspective correction
# --------------------------------------------------

src_points = np.float32(points)

dst_points = np.float32([
    [0, 0],
    [380, 0],
    [380, 180],
    [0, 180]
])

matrix = cv2.getPerspectiveTransform(
    src_points,
    dst_points
)

warped = cv2.warpPerspective(
    image,
    matrix,
    (380, 180)
)

cv2.imwrite(
    "outputs/perspective.jpeg",
    warped
)


# --------------------------------------------------
# 5. Crop the English text region
# --------------------------------------------------

english_warped = warped[105:170, 10:370]

cv2.imwrite(
    "outputs/english_warped.jpeg",
    english_warped
)


# --------------------------------------------------
# 6. Convert to grayscale
# --------------------------------------------------

english_gray = cv2.cvtColor(
    english_warped,
    cv2.COLOR_BGR2GRAY
)


# --------------------------------------------------
# 7. Upscale the text
# --------------------------------------------------

english_upscaled = cv2.resize(
    english_gray,
    None,
    fx=3,
    fy=3,
    interpolation=cv2.INTER_CUBIC
)

cv2.imwrite(
    "outputs/ocr_input.jpeg",
    english_upscaled
)

print("OCR input shape:", english_upscaled.shape)


# --------------------------------------------------
# 8. OCR using Tesseract
# --------------------------------------------------

text = pytesseract.image_to_string(
    english_upscaled,
    lang="eng"
)


# --------------------------------------------------
# 9. Display and save output
# --------------------------------------------------

print("\n--- OCR OUTPUT ---")
print(text)

os.makedirs("outputs", exist_ok=True)

with open(
    "outputs/output.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(text)
with open("outputs/output.txt", "w", encoding="utf-8") as f:
    f.write(text.strip())
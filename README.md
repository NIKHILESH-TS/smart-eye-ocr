# Smart Eye OCR

A small Python-based OCR pipeline that extracts text from real-world images using OpenCV and Tesseract OCR.

## Approach

The pipeline performs the following steps:

1. Load the input image using OpenCV.
2. Apply perspective correction to straighten the sign.
3. Crop the relevant English text region.
4. Convert the cropped region to grayscale.
5. Upscale the image to improve OCR readability.
6. Extract text using Tesseract OCR.
7. Save the extracted text as `outputs/output.txt`.

## Technologies Used

- Python
- OpenCV
- NumPy
- Tesseract OCR
- Pytesseract

## Project Structure

```text
smart-eye-ocr/
│
├── sample/
│   └── input.jpeg
│
├── outputs/
│   ├── perspective.jpeg
│   ├── english_warped.jpeg
│   ├── ocr_input.jpeg
│   └── output.txt
│
├── ocr_pipeline.py
├── requirements.txt
└── README.md

Sample Input

The pipeline was tested on a real-world photograph of a signboard.

Sample Output
TRANSPORTATION SECTION
INDIAN INSTITUTE OF TECHNOLOGY ROORKEE
How to Run

Install the Python dependencies:

pip install -r requirements.txt

Make sure Tesseract OCR is installed and available at:

C:\Program Files\Tesseract-OCR\tesseract.exe

Then run:

python ocr_pipeline.py

The extracted text will be displayed in the terminal and saved to:

outputs/output.txt
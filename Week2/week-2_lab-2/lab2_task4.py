import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
image = cv2.imread('team2.jpg')
image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ============================================================
# Part 1: Experiment with different division factors
# ============================================================

# Divide by different factors
divided_05 = cv2.divide(image_RGB, 0.5)  # Dividing by 0.5 = multiplying by 2
divided_2 = cv2.divide(image_RGB, 2)      # Factor 2
divided_3 = cv2.divide(image_RGB, 3)      # Factor 3

# Display comparison
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(divided_05)
plt.title('Divided by 0.5 (Brighter)')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(image_RGB)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(divided_3)
plt.title('Divided by 3.0 (Darker)')
plt.axis('off')

plt.suptitle('Part 1: Effect of Different Division Factors')
plt.tight_layout()
plt.show()

# Additional comparison with more factors
divided_03 = cv2.divide(image_RGB, 0.3)  # Dividing by 0.3 = multiplying by ~3.33
divided_07 = cv2.divide(image_RGB, 0.7)  # Dividing by 0.7 = multiplying by ~1.43
divided_4 = cv2.divide(image_RGB, 4)      # Factor 4

plt.figure(figsize=(18, 5))

plt.subplot(1, 5, 1)
plt.imshow(divided_03)
plt.title('÷0.3 (Very Bright)')
plt.axis('off')

plt.subplot(1, 5, 2)
plt.imshow(divided_05)
plt.title('÷0.5 (Bright)')
plt.axis('off')

plt.subplot(1, 5, 3)
plt.imshow(image_RGB)
plt.title('Original (÷1.0)')
plt.axis('off')

plt.subplot(1, 5, 4)
plt.imshow(divided_2)
plt.title('÷2.0 (Dark)')
plt.axis('off')

plt.subplot(1, 5, 5)
plt.imshow(divided_4)
plt.title('÷4.0 (Very Dark)')
plt.axis('off')

plt.suptitle('Comparison of Multiple Division Factors')
plt.tight_layout()
plt.show()

# ============================================================
# Part 2: Comparison of division factors > 1 vs < 1
# ============================================================

print("""
============================================================
Part 2: Comparing Division by Numbers > 1 vs < 1
============================================================

Division is the inverse of multiplication:
  pixel / n  =  pixel × (1/n)

--------------------------------------------------------------
DIVIDING BY NUMBER > 1 (e.g., 2, 3, 4) - DECREASES BRIGHTNESS
--------------------------------------------------------------

Mathematical effect:
- Dividing by 2 = Multiplying by 0.5
- Dividing by 3 = Multiplying by 0.33
- Dividing by 4 = Multiplying by 0.25

Example with divisor = 3:
  - Pixel value 255 -> 255 ÷ 3 = 85  (white becomes gray)
  - Pixel value 150 -> 150 ÷ 3 = 50  (bright becomes dark)
  - Pixel value 60  -> 60 ÷ 3 = 20   (gray becomes very dark)

Result:
- Image becomes DARKER
- Contrast DECREASES (values compressed toward 0)
- Larger divisor = darker image

--------------------------------------------------------------
DIVIDING BY NUMBER < 1 (e.g., 0.5, 0.3) - INCREASES BRIGHTNESS
--------------------------------------------------------------

Mathematical effect:
- Dividing by 0.5 = Multiplying by 2
- Dividing by 0.3 = Multiplying by 3.33
- Dividing by 0.25 = Multiplying by 4

Example with divisor = 0.5:
  - Pixel value 50  -> 50 ÷ 0.5 = 100  (dark becomes mid-tone)
  - Pixel value 100 -> 100 ÷ 0.5 = 200 (mid becomes bright)
  - Pixel value 150 -> 150 ÷ 0.5 = 255 (saturated to white)

Result:
- Image becomes BRIGHTER
- Contrast INCREASES (values stretched toward 255)
- Smaller divisor = brighter image (risk of overexposure)

--------------------------------------------------------------
DIVIDING BY 1 - NO CHANGE
--------------------------------------------------------------
- pixel / 1 = pixel
- Image remains identical

--------------------------------------------------------------
SUMMARY TABLE
--------------------------------------------------------------

| Divisor | Equivalent To  | Brightness | Contrast  |
|---------|----------------|------------|-----------|
| > 1     | Multiply < 1   | Decreases  | Decreases |
| = 1     | No change      | No change  | No change |
| < 1     | Multiply > 1   | Increases  | Increases |

--------------------------------------------------------------
RELATIONSHIP: Division vs Multiplication
--------------------------------------------------------------

Division and multiplication are inverse operations:

| Division        | Equivalent Multiplication |
|-----------------|---------------------------|
| ÷ 0.25          | × 4.0                     |
| ÷ 0.5           | × 2.0                     |
| ÷ 1.0           | × 1.0                     |
| ÷ 2.0           | × 0.5                     |
| ÷ 4.0           | × 0.25                    |

This means:
- cv2.divide(image, 2) produces the same result as cv2.multiply(image, 0.5)
- cv2.divide(image, 0.5) produces the same result as cv2.multiply(image, 2)

--------------------------------------------------------------
PRACTICAL USE CASES
--------------------------------------------------------------

Division by > 1 (Darkening):
- Reduce overexposure in bright images
- Create shadow/night effects
- Prepare images for low-light display

Division by < 1 (Brightening):
- Enhance underexposed images
- Increase visibility of dark regions
- Create high-key/bright effects
""")

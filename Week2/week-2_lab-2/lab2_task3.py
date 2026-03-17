import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
image = cv2.imread('team2.jpg')
image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ============================================================
# Part 1: Experiment with different multiplication factors
# ============================================================

# Multiply by different factors
# For factors < 1, we need to use numpy or convert to float
multiplied_05 = cv2.multiply(image_RGB, np.array([0.5]))  # Factor 0.5
multiplied_20 = cv2.multiply(image_RGB, 2)                 # Factor 2.0

# Display comparison
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(multiplied_05.astype(np.uint8))
plt.title('Multiplied (x0.5) - Darker')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(image_RGB)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(multiplied_20)
plt.title('Multiplied (x2.0) - Brighter')
plt.axis('off')

plt.suptitle('Part 1: Effect of Different Multiplication Factors')
plt.tight_layout()
plt.show()

# Additional comparison with more factors
multiplied_03 = cv2.multiply(image_RGB, np.array([0.3]))
multiplied_15 = cv2.multiply(image_RGB, np.array([1.5]))
multiplied_30 = cv2.multiply(image_RGB, 3)

plt.figure(figsize=(18, 5))

plt.subplot(1, 5, 1)
plt.imshow(multiplied_03.astype(np.uint8))
plt.title('x0.3 (Very Dark)')
plt.axis('off')

plt.subplot(1, 5, 2)
plt.imshow(multiplied_05.astype(np.uint8))
plt.title('x0.5 (Dark)')
plt.axis('off')

plt.subplot(1, 5, 3)
plt.imshow(image_RGB)
plt.title('Original (x1.0)')
plt.axis('off')

plt.subplot(1, 5, 4)
plt.imshow(multiplied_20)
plt.title('x2.0 (Bright)')
plt.axis('off')

plt.subplot(1, 5, 5)
plt.imshow(multiplied_30)
plt.title('x3.0 (Very Bright)')
plt.axis('off')

plt.suptitle('Comparison of Multiple Factors')
plt.tight_layout()
plt.show()

# ============================================================
# Part 2: Discussion of multiplication impact
# ============================================================

print("""
============================================================
Part 2: Impact of Multiplication Factors on Image Contrast
============================================================

Pixel values range from 0 (black) to 255 (white).
Multiplication scales these values, affecting brightness and contrast.

--------------------------------------------------------------
FACTOR > 1 (e.g., 1.5, 2.0, 3.0) - INCREASES BRIGHTNESS/CONTRAST
--------------------------------------------------------------

Effect:
- All pixel values are scaled UP
- Dark pixels become brighter
- Bright pixels become even brighter (may saturate to 255)

Example with factor = 2:
  - Pixel value 50  -> 50 × 2 = 100 (darker gray becomes lighter)
  - Pixel value 100 -> 100 × 2 = 200 (mid-gray becomes bright)
  - Pixel value 150 -> 150 × 2 = 255 (saturated to white)

Result:
- Image appears brighter overall
- INCREASED CONTRAST: difference between dark and bright areas grows
- Risk of OVEREXPOSURE: bright regions lose detail (clipped to 255)

--------------------------------------------------------------
FACTOR < 1 (e.g., 0.3, 0.5, 0.7) - DECREASES BRIGHTNESS/CONTRAST
--------------------------------------------------------------

Effect:
- All pixel values are scaled DOWN
- Bright pixels become darker
- Dark pixels become even darker (approach 0)

Example with factor = 0.5:
  - Pixel value 200 -> 200 × 0.5 = 100 (bright becomes mid-tone)
  - Pixel value 100 -> 100 × 0.5 = 50  (mid-gray becomes dark)
  - Pixel value 50  -> 50 × 0.5 = 25   (dark becomes very dark)

Result:
- Image appears darker overall
- DECREASED CONTRAST: difference between dark and bright areas shrinks
- Risk of UNDEREXPOSURE: dark regions lose detail (approach 0)

--------------------------------------------------------------
FACTOR = 1 - NO CHANGE
--------------------------------------------------------------
- Pixel values remain unchanged
- Image appears identical to original

--------------------------------------------------------------
SUMMARY TABLE
--------------------------------------------------------------

| Factor  | Brightness | Contrast  | Risk                    |
|---------|------------|-----------|-------------------------|
| < 1     | Decreases  | Decreases | Loss of shadow detail   |
| = 1     | No change  | No change | None                    |
| > 1     | Increases  | Increases | Loss of highlight detail|

--------------------------------------------------------------
KEY DIFFERENCE: Addition/Subtraction vs Multiplication
--------------------------------------------------------------

Addition/Subtraction: Shifts all pixels by same amount
  - 50 + 100 = 150, 200 + 100 = 255 (same shift)

Multiplication: Scales pixels proportionally
  - 50 × 2 = 100, 200 × 2 = 255 (different absolute change)

This proportional scaling is why multiplication affects CONTRAST,
while addition/subtraction mainly affects BRIGHTNESS uniformly.
""")

import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('team2.jpg')
image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ============================================================
# Part 1: Experiment with different intensity values (30, 100)
# ============================================================

# Subtract different intensity values
subtracted_30 = cv2.subtract(image_RGB, 30)
subtracted_100 = cv2.subtract(image_RGB, 100)

# Display comparison
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image_RGB)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(subtracted_30)
plt.title('Subtracted (-30)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(subtracted_100)
plt.title('Subtracted (-100)')
plt.axis('off')

plt.suptitle('Part 1: Effect of Different Subtraction Values')
plt.tight_layout()
plt.show()

# ============================================================
# Part 2: Explanation (printed to console)
# ============================================================

print("""
============================================================
Part 2: Why does the image become darker when we subtract more?
============================================================

Pixel intensity values range from 0 (black) to 255 (white).

- When we subtract a value from each pixel, we reduce its brightness.
- Subtracting 30: Each pixel loses a small amount of brightness (slight darkening)
- Subtracting 100: Each pixel loses more brightness (significant darkening)

Key points:
1. Lower pixel values = darker pixels
2. cv2.subtract() uses saturation arithmetic:
   - If result < 0, it becomes 0 (pure black)
   - This prevents negative values and "wrapping around"
3. The more we subtract, the more pixels reach 0 (black),
   causing loss of detail in dark regions.

Example: A pixel with value 80
   - Subtract 30: 80 - 30 = 50 (still visible, darker)
   - Subtract 100: 80 - 100 = 0 (becomes black, detail lost)
""")

# ============================================================
# Part 3: Reduce intensity of RED channel only
# ============================================================

# Create a copy of the original image
image_red_reduced = image_RGB.copy()

# Subtract only from the Red channel (index 0 in RGB)
# Method 1: Direct subtraction with saturation handling
image_red_reduced[:, :, 0] = cv2.subtract(image_red_reduced[:, :, 0], 100)

# Display the result
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_RGB)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(image_red_reduced)
plt.title('Red Channel Reduced (-100)')
plt.axis('off')

plt.suptitle('Part 3: Reducing Red Channel Intensity Only')
plt.tight_layout()
plt.show()

print("""
============================================================
Part 3: Red Channel Reduction Explanation
============================================================

In RGB images, each pixel has 3 values: [Red, Green, Blue]
- Index 0 = Red channel
- Index 1 = Green channel
- Index 2 = Blue channel

By subtracting only from index 0, we reduce red intensity while
keeping green and blue unchanged. This makes the image appear
more cyan/blue-green (the opposite of red).

Code used:
    image_red_reduced[:, :, 0] = cv2.subtract(image_red_reduced[:, :, 0], 100)

Where [:, :, 0] selects all rows, all columns, but only channel 0 (Red).
""")

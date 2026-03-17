import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('team2.jpg')
image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ============================================================
# Part 1: Experiment with different intensity values (30, 100)
# ============================================================

# Add different intensity values
added_30 = cv2.add(image_RGB, 30)
added_100 = cv2.add(image_RGB, 100)

# Display comparison
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image_RGB)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(added_30)
plt.title('Added (+30)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(added_100)
plt.title('Added (+100)')
plt.axis('off')

plt.suptitle('Part 1: Effect of Different Addition Values')
plt.tight_layout()
plt.show()

# ============================================================
# Part 2: Explanation (printed to console)
# ============================================================

print("""
============================================================
Part 2: Why does the image become brighter when we add more?
============================================================

Pixel intensity values range from 0 (black) to 255 (white).

- When we add a value to each pixel, we increase its brightness.
- Adding 30: Each pixel gains a small amount of brightness (slight brightening)
- Adding 100: Each pixel gains more brightness (significant brightening)

Key points:
1. Higher pixel values = brighter pixels
2. cv2.add() uses saturation arithmetic:
   - If result > 255, it becomes 255 (pure white)
   - This prevents overflow and "wrapping around"
3. The more we add, the more pixels reach 255 (white),
   causing loss of detail in bright regions (overexposure).

Example: A pixel with value 200
   - Add 30: 200 + 30 = 230 (still visible, brighter)
   - Add 100: 200 + 100 = 255 (becomes white, detail lost)

Note: This is different from using the + operator directly:
   - cv2.add(img, 100) -> saturates at 255
   - img + 100 -> wraps around (e.g., 200 + 100 = 44, not 255)
""")

# ============================================================
# Part 3: Increase intensity of RED channel only
# ============================================================

# Create a copy of the original image
image_red_increased = image_RGB.copy()

# Add only to the Red channel (index 0 in RGB)
image_red_increased[:, :, 0] = cv2.add(image_red_increased[:, :, 0], 100)

# Display the result
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_RGB)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(image_red_increased)
plt.title('Red Channel Increased (+100)')
plt.axis('off')

plt.suptitle('Part 3: Increasing Red Channel Intensity Only')
plt.tight_layout()
plt.show()

print("""
============================================================
Part 3: Red Channel Increase Explanation
============================================================

In RGB images, each pixel has 3 values: [Red, Green, Blue]
- Index 0 = Red channel
- Index 1 = Green channel
- Index 2 = Blue channel

By adding only to index 0, we increase red intensity while
keeping green and blue unchanged. This makes the image appear
more red/warm tinted.

Code used:
    image_red_increased[:, :, 0] = cv2.add(image_red_increased[:, :, 0], 100)

Where [:, :, 0] selects all rows, all columns, but only channel 0 (Red).
""")

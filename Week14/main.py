import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load original image
img = cv2.imread("crack.jpg")
original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 1. Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Contrast Enhancement (CLAHE) — make dark crack stand out more
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced = clahe.apply(gray)

# 3. Denoising — bilateral filter preserves edges while smoothing surface texture
denoised = cv2.bilateralFilter(enhanced, 9, 75, 75)

# 4. Edge Detection (Canny)
edges = cv2.Canny(denoised, 50, 150)

# 5. Threshold — focus on the darkest regions (the crack is black)
# Use a fixed low threshold to isolate only the darkest pixels (crack + hole)
_, thresh = cv2.threshold(denoised, 80, 255, cv2.THRESH_BINARY_INV)

# 6. Defect Mask — clean up threshold result
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
kernel_large = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 7))  # Vertical kernel for vertical crack

# Remove small noise
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
# Connect crack segments vertically
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel_large, iterations=3)
# Clean up
defect_mask = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel, iterations=1)

# Remove small blobs — keep only significant defects
contours_filter, _ = cv2.findContours(defect_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
defect_mask_clean = np.zeros_like(defect_mask)
for cnt in contours_filter:
    if cv2.contourArea(cnt) > 200:
        cv2.drawContours(defect_mask_clean, [cnt], -1, 255, -1)
defect_mask = defect_mask_clean

# 7. Final Result — mark detected defects on original image
contours, _ = cv2.findContours(defect_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = original.copy()
for cnt in contours:
    # Red contour
    cv2.drawContours(result, [cnt], -1, (255, 0, 0), 2)
    # Green bounding box
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(result, "Defect", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

# Display all 8 steps
titles = [
    "1. Original",
    "2. Grayscale",
    "3. Contrast Enhanced (CLAHE)",
    "4. Denoised",
    "5. Edge Detection (Canny)",
    "6. Threshold",
    "7. Defect Mask",
    "8. Final Result - Detected Defects"
]

images = [original, gray, enhanced, denoised, edges, thresh, defect_mask, result]
cmaps = [None, "gray", "gray", "gray", "gray", "gray", "gray", None]

fig, axes = plt.subplots(2, 4, figsize=(20, 10))
fig.suptitle("Defect Detection Pipeline", fontsize=18, fontweight="bold")

for i, ax in enumerate(axes.flat):
    ax.imshow(images[i], cmap=cmaps[i])
    ax.set_title(titles[i], fontsize=12, fontweight="bold")
    ax.axis("off")

plt.tight_layout()
plt.savefig("defect_detection_result.png", dpi=150, bbox_inches="tight")
plt.show()

print("Done! Results saved to 'defect_detection_result.png'")
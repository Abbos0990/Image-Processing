# Lab 04 - Intensity Transformation I

This project contains a simple notebook solution for Lab 04.

## Main Files
- `lab4.pdf`: original lab instructions.
- `lab04.ipynb`: final notebook (simple style, minimal comments).
- `lab04_assets/images`: input test images (`1.png` to `5.jpg`).
- `lab04_outputs`: generated results.

## What the Notebook Does
1. Loads all images from `lab04_assets/images`.
2. Applies gamma correction with selected gamma values for each image.
3. Saves Task 1 outputs and comparison figures.
4. Demonstrates the normalized-image save issue.
5. Applies contrast stretching using required parameter sets.
6. Saves Task 2 outputs and comparison figures.
7. Writes a short report to `lab04_outputs/lab04_brief_report.md`.

## How to Run
Open `lab04.ipynb` and run all cells in order.

## Output Structure
- `lab04_outputs/task1_gamma`: gamma-corrected images.
- `lab04_outputs/task2_contrast`: contrast-stretched images.
- `lab04_outputs/figures`: side-by-side screenshots for submission.
- `lab04_outputs/lab04_brief_report.md`: short written report.

## Note About Saving Normalized Images
If pixel values are in `[0, 1]`, do not cast directly to `uint8`.
Scale first (`x * 255`) and then convert to `uint8`.

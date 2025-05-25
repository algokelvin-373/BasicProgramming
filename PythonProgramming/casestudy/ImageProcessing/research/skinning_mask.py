import cv2
from skimage import morphology

# Misal: Mask dari mediapipe (poin 2)
mask = cv2.imread("D:/output_no_bg_1745829248.7853775.jpg", cv2.IMREAD_GRAYSCALE)

# 1. Hilangkan noise kecil
clean_mask = morphology.remove_small_objects(mask.astype(bool), min_size=500)
clean_mask = clean_mask.astype('uint8') * 255

# 2. Tutup lubang kecil (opsional)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
clean_mask = cv2.morphologyEx(clean_mask, cv2.MORPH_CLOSE, kernel)

# Simpan hasil
cv2.imwrite("output_mask_cleaned.jpg", clean_mask)
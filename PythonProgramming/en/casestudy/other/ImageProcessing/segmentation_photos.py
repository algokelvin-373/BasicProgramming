import cv2
import numpy as np

# 1. Baca gambar dari file
input_path = "D:/ai_tools.png"  # Ganti dengan path gambar Anda
image = cv2.imread(input_path)

if image is None:
    raise ValueError("Gambar tidak ditemukan atau path salah!")

# 2. Preprocessing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. Adaptive Thresholding
thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV, 11, 2
)

# 4. Morphological Operation
kernel = np.ones((3, 3), np.uint8)
morphed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 5. Deteksi Kulit
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)
skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

# 6. Gabungkan Hasil
final_mask = cv2.bitwise_and(morphed, morphed, mask=~skin_mask)
final_mask[skin_mask > 0] = 255  # Kulit = putih, pakaian = hitam

# 7. Penyempurnaan (Opsional)
contours, _ = cv2.findContours(final_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) < 1000:
        cv2.drawContours(final_mask, [cnt], -1, 0, -1)

# 8. Simpan hasil
output_path = "D:/output_mask.jpg"
cv2.imwrite(output_path, final_mask)

# 9. Tampilkan hasil (opsional)
# cv2.imshow("Hasil Segmentasi", final_mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
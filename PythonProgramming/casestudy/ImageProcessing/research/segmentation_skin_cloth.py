import cv2
import mediapipe as mp
import time as time

# Inisialisasi model
mp_selfie_segmentation = mp.solutions.selfie_segmentation
segmentor = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)  # 1=general model

# Baca gambar
image = cv2.imread("D:/output_no_bg_1745824787.4842954.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Segmentasi
results = segmentor.process(rgb)
mask = results.segmentation_mask  # Mask (0-1)

# Konversi ke mask biner (kulit = putih, lainnya = hitam)
mask_binary = (mask > 0.5).astype('uint8') * 255

# Simpan hasil
times = time.time()
cv2.imwrite(f"D:/output_mask_{times}.jpg", mask_binary)
import cv2
import numpy as np
import time as time


def is_plain_background(image, threshold=0.9):
    """
    Cek apakah background polos (contoh: putih/hijau) atau tidak.
    Threshold = toleransi keseragaman warna (0-1).
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Cari warna dominan di tepi gambar (asumsi background ada di tepi)
    edges = cv2.Canny(image, 100, 200)
    edge_pixels = image[np.where(edges != 0)]

    if len(edge_pixels) == 0:
        return False

    # Hitung deviasi standar warna tepi
    std_dev = np.std(edge_pixels, axis=0)
    return np.mean(std_dev) < 15  # Semakin kecil, semakin polos


def process_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Gambar tidak ditemukan!")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # ===== AUTO-DETECT BACKGROUND =====
    if is_plain_background(image):
        print("Background polos terdeteksi. Menggunakan color thresholding...")
        # Hapus background hijau/putih
        lower_bg = np.array([35, 20, 20])  # Range untuk hijau
        upper_bg = np.array([90, 255, 255])
        bg_mask = cv2.inRange(hsv, lower_bg, upper_bg)
        bg_mask = cv2.bitwise_not(bg_mask)
    else:
        print("Background kompleks terdeteksi. Menggunakan GrabCut...")
        # Gunakan GrabCut untuk background beragam
        mask = np.zeros(image.shape[:2], np.uint8)
        bgd_model = np.zeros((1, 65), np.float64)
        fgd_model = np.zeros((1, 65), np.float64)
        rect = (50, 50, image.shape[1] - 100, image.shape[0] - 100)  # ROI
        cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
        bg_mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # ===== SEGMENTASI KULIT =====
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Gabungkan dengan mask background
    final_mask = cv2.bitwise_and(skin_mask, bg_mask)
    final_mask[final_mask > 0] = 255  # Kulit = putih

    # Simpan hasil
    times = time.time()
    cv2.imwrite(f"D:/output_mask_{times}.jpg", final_mask)
    print("Hasil disimpan sebagai output_mask.jpg")


# Contoh penggunaan
process_image("D:/photos3.jpg")
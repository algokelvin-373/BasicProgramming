from PIL import Image
import numpy as np
import os


def load_image(path, size=None):
    img = Image.open(path).convert("RGB")
    if size:
        img = img.resize(size)
    return np.array(img)


def save_image(array, path):
    Image.fromarray(array).save(path)
    print(f"Saved: {path}")


def get_cloth_mask_from_parsing(parsing_path, original_path, cloth_rgb=(128, 0, 128)):
    parsing_img_arr = load_image(parsing_path)
    original_img_arr = load_image(original_path)

    cloth_rgb = (128, 0, 128)  # contoh: warna ungu dari parsing
    cloth_mask = np.all(parsing_img_arr == cloth_rgb, axis=-1)
    output_white = np.ones_like(original_img_arr) * 255
    output_white[cloth_mask] = original_img_arr[cloth_mask]

    return output_white


def generate_bw_mask(cloth_only_img):
    cloth_arr = np.array(cloth_only_img)
    cloth_mask = ~np.all(cloth_arr == [255, 255, 255], axis=-1)

    mask_canvas = np.zeros_like(cloth_arr)
    mask_canvas[cloth_mask] = [255, 255, 255]

    return mask_canvas


def transfer_cloth_rgb(base_img_path, cloth_rgb_img_path, mask_img_path, output_path):
    base_img_arr = load_image(base_img_path)
    cloth_rgb_img_arr = load_image(cloth_rgb_img_path, size=base_img_arr.shape[1::-1])
    mask_arr = load_image(mask_img_path, size=base_img_arr.shape[1::-1])

    cloth_area = np.all(mask_arr == [255, 255, 255], axis=-1)
    base_img_arr[cloth_area] = cloth_rgb_img_arr[cloth_area]

    save_image(base_img_arr, output_path)


def main():
    # Path setup
    base_dir = "D:/My_Research/"

    # Loop for multi process data
    data = 1
    while data <= 5:
        paths = {
            "original": os.path.join(base_dir, f"gambar{data}.jpg"),
            "img_viton": os.path.join(base_dir, f"gambar{data}_result.jpg"),
            "parsing": os.path.join(base_dir, f"gambar{data}_result.png"),
            "cloth_only": os.path.join(base_dir, f"gambar{data}_hasil_cloth_only.jpg"),
            "bw_mask": os.path.join(base_dir, f"gambar{data}_hasil_cloth_mask_bw.jpg"),
            "final_output": os.path.join(base_dir, f"gambar{data}_fixed.jpg")
        }

        # Step 1: Generate hasil_cloth_only.jpg
        cloth_only = get_cloth_mask_from_parsing(paths["parsing"], paths["original"])
        save_image(cloth_only, paths["cloth_only"])

        # Step 2: Generate hasil_cloth_mask_bw.jpg
        cloth_only_img = Image.open(paths["cloth_only"]).convert("RGB")
        cloth_bw = generate_bw_mask(cloth_only_img)
        save_image(cloth_bw, paths["bw_mask"])

        # Step 3: Apply RGB transfer
        transfer_cloth_rgb(
            base_img_path=paths["original"],
            cloth_rgb_img_path=paths["img_viton"],
            mask_img_path=paths["bw_mask"],
            output_path=paths["final_output"]
        )

        data += 1


if __name__ == "__main__":
    main()

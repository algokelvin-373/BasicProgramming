import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import BSpline

# === Dot control ===
control_points = np.array([
    [0, 0],
    [1, 2],
    [2, 3],
    [3, 2],
    [2, 0]
])
x = control_points[:, 0]
y = control_points[:, 1]
n_points = len(control_points)

# === Make B-spline ===
p = 3  # derajat kubik
n = n_points - 1
knots = np.concatenate((
    np.zeros(p),
    np.linspace(0, 1, n - p + 2),
    np.ones(p)
))
spl_x = BSpline(knots, x, p, extrapolate=False)
spl_y = BSpline(knots, y, p, extrapolate=False)

# Evaluasi kurva penuh untuk referensi
t_full = np.linspace(0, 1, 300)
curve_full_x = spl_x(t_full)
curve_full_y = spl_y(t_full)

# === Setup plot ===
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 3.5)
ax.set_title('Animasi Menggambar B-spline')
ax.grid(True)
ax.axis('equal')

# Elemen animasi (awalnya kosong)
line_control, = ax.plot([], [], 'ro--', alpha=0.7, label='Titik kontrol', linewidth=1.5)
line_curve, = ax.plot([], [], 'b-', linewidth=2.5, label='B-spline')
ax.legend()

# Total frame: cukup untuk tampilkan semua titik + semua segmen kurva
frames_control = n_points          # untuk garis kontrol
frames_curve = len(t_full)         # untuk kurva
total_frames = frames_control + frames_curve

# === Fungsi animasi ===
def animate(frame):
    if frame < frames_control:
        # Tahap 1: Gambar titik kontrol & garis penghubung per titik
        k = frame + 1
        line_control.set_data(x[:k], y[:k])
        line_curve.set_data([], [])  # kurva belum muncul
    else:
        # Tahap 2: Gambar kurva secara bertahap
        idx = frame - frames_control
        line_curve.set_data(curve_full_x[:idx], curve_full_y[:idx])
        # Titik kontrol tetap utuh
        line_control.set_data(x, y)
    return line_control, line_curve

# === Buat animasi ===
anim = FuncAnimation(
    fig,
    animate,
    frames=total_frames,
    interval=50,   # 20 FPS
    blit=True,
    repeat=True
)

plt.show()
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Siapkan data
x = np.linspace(-10, 10, 400)
y = x  # y = x

# Buat figure dan axis
fig, ax = plt.subplots(figsize=(8, 8))

# Atur tampilan dasar (sumbu, grid, dll)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_xticks(range(-10, 11))
ax.set_yticks(range(-10, 11))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Animasi: Menggambar y = x')

# Garis kosong yang akan diisi perlahan
line, = ax.plot([], [], color='red', linewidth=2, label='y = x')
ax.legend()

# Fungsi init: dipanggil sekali di awal
def init():
    line.set_data([], [])
    return line,

# Fungsi animasi: dipanggil setiap frame
def animate(i):
    # i adalah indeks frame (0 sampai len(x))
    line.set_data(x[:i], y[:i])
    return line,

# Buat animasi
ani = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=len(x),  # jumlah frame = jumlah titik
    interval=20,    # waktu antar frame dalam milidetik (50 fps ≈ 20 ms)
    blit=True,
    repeat=True
)

# Tampilkan
plt.show()
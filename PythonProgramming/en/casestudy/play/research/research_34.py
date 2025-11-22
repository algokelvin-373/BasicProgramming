import matplotlib.pyplot as plt
import numpy as np

# Buat figure dan axis
fig, ax = plt.subplots(figsize=(8, 8))

# Rentang nilai x dari -10 sampai 10
x = np.linspace(-10, 10, 400)  # 400 titik untuk garis mulus
y = x  # y = x

# Plot fungsi y = x
ax.plot(x, y, color='red', label='y = x')

# Atur rentang sumbu
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Gambar garis sumbu X dan Y
ax.axhline(0, color='black', linewidth=0.8)  # Sumbu X
ax.axvline(0, color='black', linewidth=0.8)  # Sumbu Y

# Tambahkan grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Atur ticks
ax.set_xticks(range(-10, 11))
ax.set_yticks(range(-10, 11))

# Label dan judul
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.title('Grafik Fungsi y = x')

# Tampilkan legenda
ax.legend()

# Tampilkan grafik
plt.show()
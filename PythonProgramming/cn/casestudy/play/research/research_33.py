import matplotlib.pyplot as plt

# Make figure dan axis
fig, ax = plt.subplots(figsize=(8, 8))

# Setting sumbu
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Draw line sumbu X and Y
ax.axhline(0, color='black', linewidth=0.8)  # X (horizontal)
ax.axvline(0, color='black', linewidth=0.8)  # Y (vertical)

# Add grid
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Atur ticks agar sesuai dengan rentang -10 sampai 10
ax.set_xticks(range(-10, 11))
ax.set_yticks(range(-10, 11))

# Add label
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Judul grafik
plt.title('Grafik Sumbu X dan Y (-10 sampai 10)')

# Tampilkan grafik
plt.show()
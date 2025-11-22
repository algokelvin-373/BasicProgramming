import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Kategori': ['A', 'B', 'C', 'D'],
    '2022': [15, 20, 12, 25],
    '2023': [18, 22, 16, 20],
    '2024': [10, 25, 14, 15],
}

df = pd.DataFrame(data)

df = df.set_index('Kategori')

df.plot(kind='bar',
        color=['skyblue', 'salmon', 'lightgreen'],
        width=0.8)

plt.title("Penjualan per Kategori (2022, 2023, 2024)")
plt.xlabel("类别")
plt.ylabel("Penjualan")
plt.xticks(rotation=0)
plt.legend(title="Year")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['A', 'B', 'C', 'D'],
    '2022': [15, 20, 12, 25],
    '2023': [18, 22, 16, 20],
    '2024': [10, 25, 14, 15],
}

df = pd.DataFrame(data)
df = df.set_index('Category')
df.plot(kind='line',
        color=['skyblue', 'salmon', 'lightgreen'],
        linewidth=2)

plt.title("Data per Category (2022, 2023, 2024)")
plt.xlabel("类别")
plt.ylabel("Category")
plt.xticks(rotation=0)
plt.legend(title="Year")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
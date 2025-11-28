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

year = '2024'
values = df[year]
labels = df.index

plt.figure(figsize=(7, 7))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'salmon', 'lightgreen', 'gold'])
plt.title(f"Distribution per Category ({year})")
plt.axis('equal')  # Make pie chart likes circle perfect
plt.show()
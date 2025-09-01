import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 12]}

df = pd.DataFrame(data)

# Make diagram batang
df.plot(x='Category', y='Value', kind='bar',
        title='Diagram Batang dengan Pandas',
        color='skyblue', legend=False)

plt.xlabel("Category")
plt.ylabel("Value")
plt.xticks(rotation=0)
plt.show()
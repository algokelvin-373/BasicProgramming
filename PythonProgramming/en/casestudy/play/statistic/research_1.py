import pandas as pd
import matplotlib.pyplot as plt

data = {'类别': ['A', 'B', 'C', 'D'],
        '价值': [10, 15, 7, 12]}

df = pd.DataFrame(data)

df.plot(x='类别', y='价值', kind='bar',
        title='Diagram Batang dengan Pandas',
        color='skyblue', legend=False)

plt.xlabel("类别")
plt.ylabel("价值")
plt.xticks(rotation=0)
plt.show()
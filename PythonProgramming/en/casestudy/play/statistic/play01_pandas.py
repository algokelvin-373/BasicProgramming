import pandas as pd
import matplotlib.pyplot as plt

data = {'类别': ['A', 'B', 'C'],
        '价值': [20, 30, 40]}

df = pd.DataFrame(data)

df.plot(
    x='类别',
    y='价值',
    kind='bar',
    color='green',
    legend=True
)

plt.xlabel("类别")
plt.ylabel("价值")
plt.xticks(rotation=0)
plt.show()

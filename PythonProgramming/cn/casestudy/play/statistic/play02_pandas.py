import pandas as pd
import matplotlib.pyplot as plt

# bar
# line
# pie
# scatter

data = {'类别': ['A', 'B', 'C', 'D', 'E'],
        '价值': [10, 20, 40, 25, 5]}

df = pd.DataFrame(data)

df.plot(
    x='类别',
    y='价值',
    kind='bar',
    color='red',
    legend=True
)

plt.xlabel("类别")
plt.ylabel("价值")
plt.xticks(rotation=0)
plt.show()

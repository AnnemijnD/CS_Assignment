import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('istherecorrelation.csv', sep=";", decimal=',')

ax = plt.gca()


df.plot(kind='line',x='Year',y='WO [x1000]',ax=ax)
df.plot(kind='line',x='Year',y='NL Beer consumption [x1000 hectoliter]', color='red', secondary_y=True,ax=ax, title="Beer consumption and WO in the Netherlands")


ax.set_ylabel("WO [x1000]")

file = "figure.png"
plt.savefig(file, dpi=300, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
plt.show()

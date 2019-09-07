import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Dikpalsinh/Desktop/exc_rate_sep.csv', index_col=0, engine='python')
fig, ax = plt.subplots()
my_splot = ax.scatter(
df["INR per Unit"], df["Currency name "])

ax.set_xlabel("Ruppes per Unit")
ax.set_ylabel("Currency name")

plt.show()
#df.head()
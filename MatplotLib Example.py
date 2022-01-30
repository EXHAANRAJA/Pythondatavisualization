# Blank Axis and Figure Section 
import matplotlib.pyplot as plt 
import pandas as pd
ax,figure = plt.subplots()
# plt.show()

# Style Used through MatplotLib
plt.style.use("classic")
df = pd.read_csv("D:/Python Runs/csv/austin_weather.csv")

plt.title("Average Rainfall Per Month")
plt.xlabel("Month")
plt.ylabel("Average RainFall")

plt.plot(df['Month'],df['MLY-PRCP-NORMAL'])
plt.show()
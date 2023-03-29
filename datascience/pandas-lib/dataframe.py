import matplotlib.pyplot as plt
import pandas as pd


dataframe = {
  "one": pd.Series([1,2,3,4,5,5,5,6,3,2,2,2]),
  "two": pd.Series([1,2,3,4,5],index=["A","B","C","D","G"])
}

df = pd.DataFrame(dataframe)
print(df)
df.to_csv("xd.csv")

# df.plot(x="one", kind="bar")

ax = df.plot.hist(column=["one"])
plt.show()
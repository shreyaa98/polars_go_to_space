import pandas as pd
import seaborn as sns
import polars as pl

df = sns.load_dataset("penguins")
df2 = pl.from_pandas(sns.load_dataset("penguins"))

pd.pivot_table(
      data=df,
      index="island",
      values="bill_length_mm",
      aggfunc="mean"
   )


df2.pivot(
      values="bill_length_mm",
      index="island",
      aggregate_function="mean"
)
   
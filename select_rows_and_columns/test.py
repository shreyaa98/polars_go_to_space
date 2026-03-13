### Polars version

import polars as pl

df = pl.read_csv("C:\\Users\\shrey\\polars_go_to_space\\select_rows_and_columns\\crew.csv")

# print(df.columns)
# print(df['id'])
# print(df[['black_spots', 'white_spots']])
# print(df.slice(10,10).select(df.columns[1:4]))
# print(df.slice(10,10))
# result = df.filter(pl.col('ears') == 'pink')
# print(result)
# print(df.filter(pl.col('ears') == 'pink'))
# print( df.filter(pl.col('black_spots') < 3))
# print(df.filter(pl.col('black_spots').is_between(3, 7)))
# print(df.filter((pl.col('black_spots') < 3) & (pl.col('white_spots') > 7)))
print(df.sample(7))

### Pandas version

import pandas as pd

df = pd.read_csv("C:\\Users\\shrey\\polars_go_to_space\\select_rows_and_columns\\crew.csv")

# print(df.columns)
# print(df['id'])
# print(df[['black_spots', 'white_spots']])
# print(df.iloc[:, 1:4])
# print(df.iloc[10:20])
# earcolor = df.set_index('ears')  
# result = earcolor.loc['pink']    
# print(result)
# print(df[df['ears'] == 'pink'])
# print(df[df['black_spots'] < 3])
# print(df[df['black_spots'].between(3, 7)])
# print(df[(df['black_spots'] < 3) & (df['white_spots'] > 7)])
print(df.sample(7))
import polars as pl
import numpy as np

names = open("names.txt").read().split("\n")

# create a table with planets
names = np.array(names)
np.random.seed(42)  # the answer to everything
np.random.shuffle(names)
n = len(names)

# create galaxy coordinates
a = np.zeros(shape=(500, 500), dtype=np.uint8)
r = np.linspace(0, 200, num=n)
angle = np.linspace(0, 9, num=n)
sign = np.tile([1, -1], n//2)
x = np.cos(angle) * r * sign + 250 + np.random.normal(loc=0.0, scale=0.9, size=n) * (250-r) / 10
y = np.sin(angle) * r * sign + 250 + np.random.normal(loc=0.0, scale=0.9, size=n) * (250-r) / 10
z = np.random.normal(loc=0.0, scale=20.0, size=n)


planets = pl.DataFrame({
    'name': names,
    'x': x.round(2),
    'y': y.round(2),
    'z': z.round(2),
    'class': np.random.choice(np.array(list('MABC')), size=(n,)),
    'size': np.random.randint(1, 20, size=(n,)),
    'angle': angle,
})

# write planets to files
planets.filter(pl.col("angle") < 3)[:,:6].write_csv('panda_sector.csv')
planets.filter(pl.col("angle") > 6).write_csv('amoeba_sector.csv')
planets.filter(pl.col("angle").is_between(3, 6))[:,:6].write_csv('penguin_sector.csv')

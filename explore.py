#ISM2411 Lab 13 

# Self-Assessment

# 1. What does a boolean filter do, in plain English?
#    It checks every row against a condition (like region == 'South') and
#    produces a True/False value for each row. Pandas then keeps only the
#    rows marked True and drops the rest.
#
# 2. Difference between df["revenue"] and df[["revenue"]]?
#    df["revenue"] returns a Series, which is one column
#    of values. df[["revenue"]] returns a DataFrame with
#    one column. It matters when a function needs a DataFrame (2D, with
#    column labels) rather than a Series, or when you want to keep the
#    table structure instead of a plain list-like column. Double brackets
#    are also how you select several columns at once.
#
# 3. Most compelling reason to choose pandas over Excel?
#    Pandas is repeatable and scales. A script can be rerun on new data in
#    seconds with the exact same steps, handles far more rows than Excel
#    comfortably can, and every step is written down so it can be checked,
#    shared, and version-controlled.

import os
import pandas as pd

# EXERCISE 1: Load it

print("=" * 60)
print("EXERCISE 1: Load it")
print("=" * 60)

df = pd.read_csv("data/retail_sales.csv")

print("\nhead():")
print(df.head())

print("\nshape:", df.shape)  # expect (5000, 6)

print("\ncolumns:", df.columns.tolist())

print("\ndtypes:")
print(df.dtypes)

# EXERCISE 2:

print("\n" + "=" * 60)
print("EXERCISE 2: Filter by region")
print("=" * 60)

south = df[df["region"] == "South"]

print("\nNumber of South rows:", len(south))
print("\nsouth.head():")
print(south.head())

# EXERCISE 3:

print("\n" + "=" * 60)
print("EXERCISE 3: Top 5 by revenue")
print("=" * 60)

top5 = df.sort_values("revenue", ascending=False).head(5)
print(top5)
# Note: the index values are not 0-4 because the index was not reset.
# They are the original row numbers of the highest-revenue orders.

# EXERCISE 4:

print("\n" + "=" * 60)
print("EXERCISE 4: Two-condition filter")
print("=" * 60)

big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print("\nNumber of South rows with revenue > 1000:", len(big_south))
print("\nbig_south.head():")
print(big_south.head())

# EXERCISE 5: A new column

print("\n" + "=" * 60)
print("EXERCISE 5: A new column")
print("=" * 60)

df["per_unit"] = df["revenue"] / df["quantity"]

print("\nhead() with new per_unit column:")
print(df.head())

print("\nMean per-unit price:", df["per_unit"].mean())

# EXERCISE 6:

print("\n" + "=" * 60)
print("EXERCISE 6: Unique values")
print("=" * 60)

print("\nUnique regions:")
print(df["region"].unique())

print("\nRegion counts (including nulls):")
print(df["region"].value_counts(dropna=False))

# EXERCISE 7:

print("\n" + "=" * 60)
print("EXERCISE 7: Select columns")
print("=" * 60)

subset = df[["region", "product", "revenue"]]

print("\nSubset shape:", subset.shape)
print(subset.head())

# EXERCISE 8:

print("\n" + "=" * 60)
print("EXERCISE 8: Save")
print("=" * 60)

df.to_csv("data/explored.csv", index=False)

print("\nFile exists:", os.path.exists("data/explored.csv"))

with open("data/explored.csv") as f:
    print("Header row:", f.readline().strip())
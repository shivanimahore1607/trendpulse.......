import pandas as pd

data = pd.read_json("data/trends_20240115.json")
print("Loaded", len(data), "stories from data/trends_20240115.json")

data = data.drop_duplicates()
print("After removing duplicates:", len(data))

data = data.dropna()
print("After removing nulls:", len(data))

data["score"] = data["score"].astype(int)

data = data[data["score"] >= 5]
print("After removing low scores:", len(data))

data["title"] = data["title"].str.strip()

data.to_csv("data/trends_clean.csv", index=False)
print("Saved", len(data), "rows to data/trends_clean.csv")

print("\nStories per category:")
print(data["category"].value_counts())
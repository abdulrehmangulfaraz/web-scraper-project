import pandas as pd

df = pd.read_json("data_scrapy.json")
df.to_excel("data_scrapy.xlsx", index=False)


print("Scrapy data converted to Excel successfully!")

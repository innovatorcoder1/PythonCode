import pandas as pd
import numpy as np

data = {
    "Name": ["Ali","Abu Buker","Awais"],
    "Age": [22,34,20],
    "City": ["Islamabad","Lahore","Karachi"]

}
df = pd.DataFrame(data)
print(df)
print("-----------------------------------")
df["Country"] = ["Pakistan","India","USA"]
print(df)
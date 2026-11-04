# Fixed: each DataFrame column must contain the same number of values.
import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 45],
})
print(df)

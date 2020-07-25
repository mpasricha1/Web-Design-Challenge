import pandas as pd

cities_df = pd.read_csv("../Resources/cities.csv")

cities_df.to_html('table.html')
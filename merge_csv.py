
import pandas as pd

df1 = pd.read_csv("houseprices_nb.csv")
df2 = pd.read_csv("houseprices_nb1.csv")

final_df = pd.concat([df1,df2],ignore_index=True)
final_df.to_csv("houseprices_nb_merged.csv",index=False)

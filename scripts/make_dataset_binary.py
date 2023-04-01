import pandas as pd

# read the input CSV file into a Pandas dataframe
df = pd.read_csv("/home/rajashri/Documents/Visual_Code_Working_directory/INEURON_INTERNSHIP/data/output.csv")


# convert "sex", "fbs", and "exang" columns to binary
df['sex'] = df['sex'].astype(int)
df['fbs'] = df['fbs'].replace({'false': 0, 'true': 1})
df['exang'] = df['exang'].replace({'false': 0, 'true': 1})
print(df['sex'].unique())


# save the modified dataset
df.to_csv("heart_disease.csv", index=False)



import pandas as pd

# Read data from CSV file
df = pd.read_csv('Homo sapiens_9056.csv', header=None, names=["PDB ID", "Source Organism", "Accession Code"])

# Filter the data based on criteria
filtered_df = df[(df["Source Organism"] == "Homo sapiens") & (df["Accession Code"].str.count(",") == 2)]

# Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_output.csv", index=False, header=False, mode="a")

print("Filtered data saved to filtered_output.csv")

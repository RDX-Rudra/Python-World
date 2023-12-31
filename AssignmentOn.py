import pandas as pd
from itertools import combinations

# Load the data from the "Homo_sapience.csv" file
data = pd.read_csv("Homo sapiens_9056.csv")

# Filter data for Homo sapiens with only three accession codes
homo_sapiens_data = data[data['Source Organism'] == 'Homo sapiens']
accession_counts = homo_sapiens_data['EntryID'].value_counts()

# Select PDB IDs with only three accession codes
selected_EntryIDs = accession_counts[accession_counts == 3].index.tolist()

# Filter data for selected PDB IDs
selected_data = homo_sapiens_data[homo_sapiens_data['EntryID'].isin(selected_EntryIDs)]

# Write selected PDB IDs with Source Organism and accession codes to a separate CSV file
selected_data.to_csv("selected_PDBs_with_accession.csv", index=False)

# Generate accession code combinations of two for each PDB ID
accession_combinations = {}
for EntryID in selected_EntryIDs:
    codes = selected_data[selected_data['EntryID'] == EntryID]['Accession Code(s)'].tolist()
    code_combinations = list(combinations(codes, 2))
    accession_combinations[EntryID] = code_combinations

# Print or store the accession code combinations for each PDB ID
for EntryID, combinations_list in accession_combinations.items():
    print(f"{EntryID}: {combinations_list}")


# ... (existing code)

# Store accession code combinations for each PDB ID in a new DataFrame
output_data = pd.DataFrame(columns=['EntryID', 'Combinations'])
for EntryID, combinations_list in accession_combinations.items():
    output_data = output_data.append({'EntryID': EntryID, 'Combinations': combinations_list}, ignore_index=True)

# Write the combinations to a new CSV file
output_data.to_csv("accession_code_combinations.csv", index=False)

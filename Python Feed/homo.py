import pandas as pd
data = pd.read_csv('Homo sapiens_9056.csv')

data = data.ffill()

mask = (data['Source Organism'] == 'Homo sapiens') & (data['Accession Code(s)'].apply(lambda x: len(str(x).split(' ')) if pd.notna(x) else 0) == 3)

filtered_data = data[mask]
filtered_data.to_csv('filtered_data.csv', index=False)



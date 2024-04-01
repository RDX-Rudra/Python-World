import csv
import pandas as pd

data = pd.read_csv('filtered_data.csv')
def generate_combinations(lst, n):
   """Generate all combinations of n items from the list."""
   if n == 0:
       return [[]]
   l = []
   for i in range(0, len(lst)):
       m = lst[i]
       remLst = lst[i + 1:]
       remainlst_combo = generate_combinations(remLst, n - 1)
       for p in remainlst_combo:
         l.append([m, *p])
   return l

pdb_id_combinations = {}

for _, row in data.iterrows():
   pdb_id = row['Entry ID']
   accession_codes = str(row['Accession Code(s)']).split(' ')
   combinations = generate_combinations(accession_codes, 2)
   pdb_id_combinations[pdb_id] = combinations

def write_to_csv(pdb_id_combinations, filename):
  """Write the combinations of PDB IDs and accession codes to a CSV file."""
  with open(filename, 'w', newline='') as csvfile:
     writer = csv.writer(csvfile)
     for pdb_id, combinations in pdb_id_combinations.items():
        for combination in combinations:
           writer.writerow([pdb_id] + combination)

write_to_csv(pdb_id_combinations, 'combinations.csv')



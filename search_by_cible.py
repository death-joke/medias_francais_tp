import pandas as pd
from merge_data_set import print_cible

# Load the datasets tsv files
data = pd.read_csv('merged_data_set.tsv', sep='\t')


#create a loop to ask the user to enter a cible and print the result of print_cible and a the possibility to quit the program
while True:
    cible = input('Entrez une cible (or q to quit): ')
    if cible == 'q':
        break
    if cible not in data['cible'].unique():
        print('Cette cible n\'existe pas')
        continue
    print_cible(cible)






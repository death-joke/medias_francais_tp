import pandas as pd

# Load the datasets tsv files
medias = pd.read_csv('medias_francais.tsv', sep='\t')
relations = pd.read_csv('relations_medias_francais.tsv', sep='\t')

print(medias.head())
print(relations.head())

# Merge the datasets on the nom field for medias and origine field for relations and keep only the field nom, typeLibelle, valeur and cible 
merged_data_set = pd.merge(medias, relations, left_on='nom', right_on='origine')[['nom', 'typeLibelle', 'valeur', 'cible']]
print(merged_data_set.head())

#save the merged dataset in a tsv file
merged_data_set.to_csv('merged_data_set.tsv', sep='\t', index=False)

#print the different typeLibelle
def print_cible(cible):
    print(cible+' est possede par les medias suivants :')
    valeur,nom,label = merged_data_set[merged_data_set['cible'] == cible][['valeur', 'nom', 'typeLibelle']].values.T
    for valeur,nom,label in zip(valeur,nom,label):
        if valeur == 'contrôle':
            print('\tpar ',nom,' (',label,')')
        else:
            print('\t',valeur,'% par ',nom,' (',label,')')
    print('\n')

#print_cible on all the different cible in the dataset
for cible in merged_data_set['cible'].unique():
    print_cible(cible)
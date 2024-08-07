import os
from Bio import SeqIO
import string

def filter_non_gap_sequences(seq_dict):
    return {name: seq for name, seq in seq_dict.items() if any(char != '-' for char in seq)}


#Longueur de chaque gène aligné
cas_gene_lengths = {
        "Cas1": 1233,
        "Cas2": 358,
        "Cas3": 3362,
        "Cas4": 1166,
        "Cas5": 1222,
        "Cas6": 1241,
        "Cas7": 1440
    }

# Répertoire qui contient les gènes alignés
input_dir = ''#TO COMPLETE
# Path du fichier qui contiendra la concaténation
output_file = ''#TO COMPLETE
# Path du fichier qui contient le nom des organismes
organism_file = ''#TO COMPLETE

# Créer une séquence de gaps générique
def create_generic_sequence(length):
    return '-' * length

# Construire le array des noms
with open(organism_file, 'r') as f:
    organisms = [line.strip() for line in f if line.strip()]

# translation table qui sera utilisée pour enlever tout espace blanc
translation_table = str.maketrans('', '', string.whitespace)

# Initialisation d'un dictionnaire qui contiendra les séquences concaténées pour chaque espèce
final_sequences = {name: "" for name in organisms}

# Modifie les gènes que tu veux considérer dans la concaténation ici.
files = ["Cas1", "Cas2", "Cas3", "Cas4", "Cas5", "Cas6", "Cas7"]

for cas_gene in files:
    input_file = os.path.join(input_dir, f'all_{cas_gene}_aligned.fna')

    if os.path.exists(input_file):
        try:
            
            sequences = {record.id: str(record.seq).translate(translation_table) for record in SeqIO.parse(input_file, 'fasta')}
            
            for bacteria_name in organisms:
                total_sequence = ""
                for record_id, sequence in sequences.items():
                    if bacteria_name.lower() in record_id.lower():
                        
                        total_sequence += sequence

                if total_sequence:
                    
                    final_sequences[bacteria_name] += total_sequence
                else:
                    
                    generic_sequence = create_generic_sequence(cas_gene_lengths[cas_gene])
                    final_sequences[bacteria_name] += generic_sequence
        except Exception as e:
            print(f"Error processing file {input_file}: {e}")
    else:
        print(f"File {input_file} does not exist")

final_sequences = filter_non_gap_sequences(final_sequences)

#Création du output file
try:
    with open(output_file, 'w') as outfile:
        for bacteria_name, sequence in final_sequences.items():
            # Remove any remaining whitespace from the sequence before writing
            cleaned_sequence = sequence.translate(translation_table)
            outfile.write(f'>{bacteria_name}\n')
            outfile.write(f'{cleaned_sequence}\n')
    print(f'Final sequences written to {output_file}')
except Exception as e:
    print(f"Error writing to file {output_file}: {e}")

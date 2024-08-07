# KnowledgeTransfer

Archaea contient les génomes de tous les organismes considérés dans l’itération la plus récente. Il y aura un répertoire pour chaque organisme. Dans ce répertoire, on pourra retrouver le génome complet et la synténie.

Le répertoire all_Cas contient chaque gène Cas. Seuls les gènes qui avaient plus de 4 exemples dans nos organismes ont été gardés. all_Cas_aligned contient ces mêmes fichiers alignés. Cas1-Cas10_trees et rest_of_trees contiennent le output de RAxML-NG sur tous ces fichiers alignés. 

Le répertoire ASTRAL_trees contient 4 fichiers, all_gene_trees.txt est le input d’ASTRAL. All_trees_consensus_pruned.nw est la sortie d’ASTRAL à laquelle on a retiré feuilles avec de très faibles valeur de support. consensus_pruned_divergence.txt et consensus_pruned_midpoint.txt sont les deux enracinements essayés à partir de all_trees_consensus_pruned.nw. Pour obtenir le unpruned consensus tree, il suffit de rouler ASTRAL sur all_gene_trees.txt (très rapide). 

Le répertoire synesth_input contient les deux arbres consensus enracinés formattés pour Synesth et synesth_output contient les output correspondants.

Process_all_genomes.ipynb est un jupyter notebook utilisé pour extraire les bons gènes. La construction des dictionnaires a été faite manuellement considérant le faible nombre d’espèces considérées, mais l’automatisation de ce processus est très simple. 
create_concat_alignment.py permet de produire la concaténation de gènes alignés. Attention, il faut modifier les paths sur votre machine. 


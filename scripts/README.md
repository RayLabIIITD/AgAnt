# Agonist-antagonist
##Work in Progress

bindfeat - extracts features generated by fpocket binding pocket descriptors.  
cleaner - removes pdb files which have dna/rna.  
counter - hack code to seperate pdb files into agonist-and-antagonist/agonist/antagonist/none. Output needs to be manually verified.  
download_dssp - download dssp files for a list of pdb ids.  
download_ligand - download ligand files for the required ligand ids.  
download_pdb - download pdb files for a list of pdb ids.  
filter - basic filter to seperate agonist/antagonist files  
labeller_ago/ant - Manual filtering script. Fetches the molecules present in the pdb file and also the pubmed abstract linked to the pdb. Excel fille is generated which is then iterated to manually label the pdb.  
model_gnn - One of the Graph Neural Network model used.
remover - file mover  
seq_dict - create word2vec embeddings for the pdb files in a directory/list of pdb ids.  
seq_embed - create vector embeddings of protein sequences of length k for use in word2vec  

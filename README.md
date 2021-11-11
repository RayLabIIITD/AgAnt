# AgAnt

[Link to Paper]()

Activity modulation of proteins is an  essential biochemical process in cell. The interplay of the protein, as receptor, and it's corresponding ligand dictates the functional effect. An agonist molecule when bound to a receptor produces a response within the cell while an antagonist will block the binding site/produce the opposite effect of that of an agonist. Complexity grows with scenarios where some ligands might act as an agonist in certain conditions while as an antagonist in others. It is imperative to decipher the receptor-ligand functional effect for understanding native biochemical processes as well as for drug discovery. Experimental activity determination is a time extensive process and computational solution towards prediction of activity specific to the receptor-ligand interaction would be of wide interest.

We created our dataset by filtering through RCSB for entries which matched our criteria and further refined the results by performing additional filtering. The [data](https://github.com/RayLabIIITD/AgAnt/tree/main/data) folder contains the relevant data files.
 - `labels.xlsx`: Contains all PDB IDS scrapped with labels assigned to them.
 - `labels_ago.xlsx` and `labels_ant.xlsx`: Contain PDB IDS corresponding to agonists and antagonists respectively.
 - `pairwise_smiles.xlsx`: Contains all filtered PDB IDS with their respective receptor and ligand information.

In summary, we have demonstrated our models ability to differentiate between agonist and antagonist protein-ligand pairs with high accuracy. We have examined various representations of proteins and different machine learning models that can be used for classification problems. AdaBoost model trained on ProtVec and SMILES representations was the most precise and accurate model. Our results demonstrate that featurizing both the ligand and protein is not only theoretically accurate, it experimentally performs better than only considering a single entity. In the future, we want to experiment with better representations of proteins on specialized language models. The success of models based only the sequence of the protein show potential for the application of specialized transformer models for proteins.

My [BTech Project](https://github.com/RayLabIIITD/AgAnt/blob/main/BTP.pdf) report gives an overview of all the work done.

Our model is hosted on [agant.raylab.iiitd.edu.in](http://agant.raylab.iiitd.edu.in:8005) and can make predictions for any given PDB ID-Ligand ID pair or Protein Sequence-Ligand SMILES pair. Additional usage instructions are detailed on the web page.

This repository contains mostly uncommented code although the jupyter notebooks have the detailed experiments on the ProtVec and SMILES based models. 

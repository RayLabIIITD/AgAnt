
import rstoolbox as rs
import matplotlib.pyplot as plt
#print(rs.show_versions())
#baseline = rs.io.get_sequence_and_structure('4u0g.pdb')
#print(baseline)
from propy import PyPro
from propy.GetProteinFromUniprot import GetProteinSequence
from Bio.PDB import *
parser = PDBParser()
structure = parser.get_structure("PHA-L", "4u0g.pdb")
ppb = PPBuilder()
for n,m in enumerate(structure):
    proteinsequence=str(ppb.build_peptides(structure)[n].get_sequence())
    print(structure)
    print(proteinsequence)
#for pp in ppb.build_peptides(structure):
#    print(pp.get_sequence())
#proteinsequence = GetProteinSequence("P48039")    # download the protein sequence by uniprot id
#print(proteinsequence)
DesObject = PyPro.GetProDes(proteinsequence)      # construct a GetProDes object
#print(DesObject.GetCTD())                         # calculate 147 CTD descriptors
#print(DesObject.GetAAComp())                      # calculate 20 amino acid composition descriptors
paac = DesObject.GetPAAC(lamda=10,weight=0.05)    # calculate 30 pseudo amino acid composition descriptors

#print(paac)

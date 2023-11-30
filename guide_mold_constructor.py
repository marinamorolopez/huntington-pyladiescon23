# -*- coding: utf-8 -*- 
"""
Created on Thu Nov 30 18:10:55 2023

@author: Marina Moro López
"""

from tkinter.filedialog import askopenfile

def main():

    gene_file = askopenfile(mode='r')
    gene_seq = gene_file.readlines()[1:]
    gene_seq = ''.join(gene_seq).replace('\n', '')
    
    DNA_guide, mutated_gene_seq, mold, patient_reps = repeated_seq(gene_seq)
    
    mutated_gene_file = open('MUTATED_SEQUENCE.txt', 'w')
    mutated_gene_file.write(mutated_gene_seq)
    mutated_gene_file.close()
    
    guide_file = open('GUIDE.txt', 'w')
    guide_file.write(DNA_to_RNA(DNA_guide))
    guide_file.close()
    
    mold_file = open('MOLD.txt', 'w')
    mold_file.write(mold)
    mold_file.close()


def repeated_seq(gene_seq):

    mutation_position = int(input("Introduce the numeric position of the mutation base (e.g. 1, 25, 203): "))
    while mutation_position <= 0:
        print('Invalid input. Introduce positive number. ')
        mutation_position = int(input("Introduce the numeric position of the mutation base (e.g. 1, 25, 203): "))
    
    rep_letters = input("Introduce the letters that are repeated (e.g. AAT, CAG, CCGT, GACTA): ")
    
    healthy_reps = int(input("Introduce the healthy number of repetitions (e.g. 20, 35, 42): "))
    while healthy_reps <= 0:
        print('Invalid input. Introduce positive number. ')
        healthy_reps = int(input("Introduce the healthy number of repetitions (e.g. 20, 35, 42): "))
    
    patient_reps = []
    gene_seq_slice = gene_seq[mutation_position-1:]
    i = 0
    while gene_seq_slice.find(rep_letters) != -1:
        patient_reps.append(gene_seq_slice.find(rep_letters))
        if i >= 2:
            if patient_reps[-1] - patient_reps[-2] != len(rep_letters):
                break
        gene_seq_slice = gene_seq_slice.replace(rep_letters, "*" * len(rep_letters), 1)
        i += 1
        
    DNA_guide = rep_letters * (len(patient_reps)-1)
    mold = rep_letters * healthy_reps
    mutated_gene_seq = gene_seq[:mutation_position-1] + mold + gene_seq[mutation_position+(len(patient_reps)-1)*len(rep_letters)-1:]
    
    return DNA_guide, mutated_gene_seq, mold, patient_reps


def DNA_to_RNA(DNA_guide):
    
    RNA_guide = ""
    for base in DNA_guide:
        if base == "T":
            RNA_guide += "A"
        elif base == "A":
            RNA_guide += "U"
        elif base == "C":
            RNA_guide += "G"
        elif base == "G":
            RNA_guide += "C"
    
    return RNA_guide


main()

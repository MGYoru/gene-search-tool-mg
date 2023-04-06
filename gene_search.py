from Bio import Entrez
import ssl
import tkinter as tk
from tkinter import ttk
import threading


Entrez.email = "unimgwork@gmail.com"

def get_gene_ids(chromosome, name):

    # Define the search term to be used
    search_term = f"{name}[Gene Name] AND {chromosome}[Chromosome] AND alive[prop] AND human[organism]"

    # Line used to bypass the certificate error
    ssl._create_default_https_context = ssl._create_unverified_context
        
    # We use the "esearch" function to get the list of IDs
    handle = Entrez.esearch(db="gene", term=search_term, retmax=20)

    # We read the handle returned by the "esearch" function
    record = Entrez.read(handle)
    handle.close()

    # We save the list of IDs
    gene_ids = record["IdList"]
    return gene_ids

def get_gene_data(gene_id):
    # We use the "esummary" function to get all the data for each gene
    handle = Entrez.esummary(db="gene", id=gene_id, retmode = "xml")

    # We read the handle returned by the "esummary" function
    record = Entrez.read(handle)
    handle.close()
            
    # We loop the dictionary to access the data
    for information_dictionary in record["DocumentSummarySet"]["DocumentSummary"]:

        chromosome = information_dictionary.get("Chromosome", "N/A")
        gene_name = information_dictionary.get("Name", "N/A")
        description = information_dictionary.get("Description", "N/A")
        location = information_dictionary.get("MapLocation", "N/A")
        summary = information_dictionary.get("Summary", "N/A")

        for genomic_info in information_dictionary["GenomicInfo"]:
            if "ChrStart" in genomic_info:
                start = genomic_info["ChrStart"]
            if "ChrStop" in genomic_info:
                end = genomic_info["ChrStop"]
            break

    return {"Chromosome": chromosome, "Gene Name": gene_name,
            "Description": description, "Location": location, "Start": start, "End": end,
            "Summary": summary}


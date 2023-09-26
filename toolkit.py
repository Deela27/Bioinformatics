import collections

#DNA nucleotides
nucleotides=["A","T","G","C"]

# Validate a Sequence to ensure nucleotides are correct and uppercase.
def validateSeq(dnaSeq):
    tmpSeq= dnaSeq.upper()
    for nucleotide in tmpSeq:
        if nucleotide not in nucleotides:
            return False
        return tmpSeq
    

#Function for transcribed mrna, a-t, g-c
def codon(sequence):
    list(sequence)
    seq=[]
    for i in sequence:
        if i == "A":
           seq.append("T") 
        elif i =="T":
            seq.append("A")
        elif i=="G":
            seq.append("C")
        else:
            seq.append("G")
    print(seq)


""" def rnaCodon(sequence):
    list(sequence)
    seq=[]
    for i in sequence:
        if i == "A":
           seq.append("U") 
        elif i =="T":
            seq.append("A")
        elif i=="G":
            seq.append("C")
        else:
            seq.append("G")
    return seq
 """

    

def countNucFreq(seq):
    #tempFreqDict = {"A":0, "T":0,"G":0,"C":0 }
    #for nuc in seq:
    #    tempFreqDict[nuc]+=1
    #return tempFreqDict
    return dict(collections.Counter(seq))

""" def rnaCodon(sequence):
    rna_dict = {"A": "U", "T": "A", "G": "C", "C": "G"}
    return [rna_dict.get(nuc, "N") for nuc in sequence] """

#Convert a list to a string.
def listToString(list):
    str1=""
    return  (str1.join(list))

# Transcribe a DNA to its corresonding RNA strand
def rnaCodon(sequence):
    list(sequence)
    seq=[]
    for i in sequence:
        if i == "A":
           seq.append("A") 
        elif i =="T":
            seq.append("U")
        elif i=="G":
            seq.append("G")
        else:
            seq.append("C")
    return seq

#Takes a string as an argument and returns the reverse of the string.
def reverseStr(dna):
    return dna[::-1]

# Function to find complement of DNA 3' to 5' and return as string
def dnaComplement(sequence):
    dna_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return listToString([dna_dict.get(nuc, "N") for nuc in sequence]) 


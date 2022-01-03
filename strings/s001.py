# Problem: Write a program that takes a DNA strand as input, and returns
#          a mRNA sequence

# Code Logic:
#    1 - Take the DNA strand from the user
#    2 - Verify if it is a correct strand (can only contain A,C,T,G letters)
#    3 - Replace T occurrences by U
#    4 - Print the RNA strand into the console

# YouTube Channel: Automation and Data Science
#                  ▶️https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg

# - - - - - - - - - - - - - - - - - - - - - - - -

dna_strand = input('Please, state the DNA sequence: ').upper().strip()

bases = set(dna_strand)

isCorrect = True
for base in bases:
    if base not in 'ACGT':
        print(f"{base!r} is not a valid letter. Detected at index position: {dna_strand.find(base)}")
        isCorrect = False
        break

if isCorrect:
    rna_seq = dna_strand.replace('T', 'U')
    print(f"Corresponding RNA sequence:\n{rna_seq}")

# Problem: Write a program that takes a DNA strand as input, and returns
#          the first three codons, one per line.

# Code Logic:
#    1 - Take the DNA strand from the user
#    2 - Verify if it is a correct strand (can only contain A,C,T,G letters)
#    3 - Verify it the correct strand has at least 10 bases
#    4 - Print the first three codons one per line

# YouTube Channel: Automation and Data Science
#                  ▶️https://www.youtube.com/channel/UCOGLG_-uQco3Z7YGXtbEbEg

# - - - - - - - - - - - - - - - - - - - - - - - -

dna_strand = input('Please, state the DNA sequence: ').upper().strip()

bases = set(dna_strand)

isCorrect = True
for base in bases:
    if base not in 'ACGT' and len(dna_strand) >= 9:
        print(f"{base!r} is not a valid letter. Detected at index position: {dna_strand.find(base)}")
        isCorrect = False
        break

if len(dna_strand) < 9:
    print(f"Your DNA sequence is too short. Current len = {len(dna_strand)}, Min len = 9")
    isCorrect = False

if isCorrect:
    for n in range(3):
        codon = dna_strand[3 * n:3 * n + 3]
        print(f"{codon = !r}")

# Transcribes DNA to RNA.
# dna_seq - string, DNA sequence.
def transcribe(dna_seq):
    x = list(dna_seq)
    for i in range(len(x)):
        if x[i] == 'T':
            x[i] = 'U'
        if x[i] == 't':
            x[i] = 'u'
    x = (''.join(x))
    return x


# Reverses the nucleic acid sequence.
# seq - string, DNA or RNA sequence.
def reverse(seq):
    return seq[::-1]


# Builds and returns a complementary strand of DNA or RNA.
# seq - string, DNA or RNA sequence; rna=True for RNA.
def complement(seq, rna=False):
    x = list(seq)
    main_code = {
        'A': 'T', 'a': 't',
        'T': 'A', 't': 'a',
        'G': 'C', 'g': 'c',
        'C': 'G', 'c': 'g'
    }

    code_rna = {
        'A': 'U', 'a': 'u',
        'U': 'A', 'u': 'a',
        'G': 'C', 'g': 'c',
        'C': 'G', 'c': 'g'
    }

    if rna:
        main_code = code_rna
    new_seq = []
    for i in x:
        i = main_code[i]
        new_seq.append(i)
    x = (''.join(new_seq))
    return x


# Checks nucleic acid sequence.
# seq - string, DNA or RNA sequence.
def check_your_seq(seq):
    # Valid sequence elements.
    list_of_na = ['A', 'C', 'G', 'T', 'U', 'a', 'c', 'g', 't', 'u']
    x = True
    for i in list(seq):
        if i not in list_of_na:
            x = False
    # Uracil and thymine cannot be in the same sequence.
    for i in list(seq.lower()):
        if i == 't':
            for j in list(seq.lower()):
                if j == 'u':
                    x = False
    return x


# Checks whether the input string is DNA or RNA sequence. DNA should not contain uracil.
# seq - string, DNA or RNA sequence.
def is_it_dna(seq):
    list_of_rna = ['U', 'u']
    x = True
    for i in list(seq):
        if i in list_of_rna:
            x = False
    return x


# Endless cycle.
n = True

# Valid commands.
list_of_command = ['transcribe', 'reverse', 'complement', 'reverse complement']
while n:
    print('Enter command')
    to_do = input()

    # Exits the program if the command is "exit".
    if to_do == 'exit':
        print('Bye-Bye!')
        n = False

    # Checks whether the command can be executed.
    if to_do in list_of_command:
        m = True
        while m:
            print('Enter sequence')
            sequence = input()

            correct_seq = check_your_seq(sequence)

            # Sequence without errors.
            if correct_seq:

                if to_do == 'transcribe':
                    # Checks whether the input string is DNA or RNA sequence.
                    if is_it_dna(sequence):
                        print(transcribe(sequence))
                    else:
                        print('I can not translate RNA :(')

                if to_do == 'reverse':
                    print(reverse(sequence))

                if to_do == 'complement':
                    # Checks whether the input string is DNA or RNA sequence.
                    if is_it_dna(sequence):
                        print(complement(sequence))
                    else:
                        print(complement(sequence, rna=True))

                if to_do == 'reverse complement':
                    # Checks whether the input string is DNA or RNA sequence.
                    if is_it_dna(sequence):
                        print(complement(reverse(sequence)))
                    else:
                        print(complement(reverse(sequence), rna=True))
                break

            # Sequence with errors.
            else:
                print('Try again!')

    # If command cannot be executed, shows an error message and continues the endless cycle.
    else:
        print('I do not understand')
        continue

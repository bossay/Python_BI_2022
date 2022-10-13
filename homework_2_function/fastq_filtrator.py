# GC-content calculator.
# reads - string, DNA sequence.
def count_gc_content(reads):
    reads = list(reads)
    return (reads.count('G') + reads.count('C')) / len(reads) * 100


# Creates a list with an interval for filtering.
# interval - tuple, int or float.
def create_interval(interval):
    if type(interval) == tuple:
        return list(interval)
    elif (type(interval) == int) | (type(interval) == float):
        interval_list = [0, interval]
        return interval_list
    else:
        print('Not supported types')

# Mean quality calculator.
# read_quality - string, score phred33.
def medium_quality(read_quality):
    read_quality = list(read_quality)
    sum_quality = 0
    for i in read_quality:
        sum_quality += ord(i) - 33
    return sum_quality / len(read_quality)


# Reads specific line numbers.
# path_to_file - string, from start to end
def read_fastq(path_to_file, start=0, end=100):
    with open(path_to_file) as file:
        lines = file.readlines()
    return lines[start:end]


# Counts how many lines are in a file.
# path_to_file - string.
def length_file(path_to_file):
    with open(path_to_file, 'r') as file:
        count_lines = sum(1 for line in file)
    return count_lines


# The main function for filtering by quality, length and GC-content.
# input_fastq, output_file_prefix - strings
# gc_bounds, length_bounds - tuple, int or float
# quality_threshold - int or float
# save_filtered - bool
def main(input_fastq,
         output_file_prefix,
         gc_bounds=(0, 100),
         length_bounds=(0, 2**32),
         quality_threshold=0,
         save_filtered=False):

    # Empty list to add reads.
    good_list = []
    bad_list = []

    # List with an interval for filtering.
    gc_bounds = create_interval(gc_bounds)
    length_bounds = create_interval(length_bounds)

    start_line = 0

    # Filtering loop
    while start_line < length_file(input_fastq):

        if gc_bounds[1] < gc_bounds[0]:
            print('Attention! Wrong interval for GC-content.')
            break
        if length_bounds[1] < length_bounds[0]:
            print('Attention! Wrong interval for length.')
            break

        # List of 4 lines from .fastq file
        read_seq = read_fastq(input_fastq, start_line, start_line+4)

        gc_test = True
        quality_test = True
        len_test = True

        # Conditions for filtering
        if (count_gc_content(read_seq[1]) < gc_bounds[0]) | (count_gc_content(read_seq[1]) > gc_bounds[1]):

            gc_test = False
        if medium_quality(read_seq[3]) < quality_threshold:
            quality_test = False
        if (len(read_seq[1]) < length_bounds[0]) | (len(read_seq[1]) > length_bounds[1]):
            len_test = False
        if gc_test & quality_test & len_test:
            good_list += read_seq
        else:
            bad_list += read_seq
        start_line += 4

    # Set path and file name.
    name_good = output_file_prefix + '_passed.fastq'
    name_bad = output_file_prefix + '_failed.fastq'

    # Writes files.
    with open(name_good, "w") as file:
        file.writelines(good_list)
    if save_filtered:
        with open(name_bad, "w") as file:
            file.writelines(bad_list)

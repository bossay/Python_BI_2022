# Introduction to Pandas and Visualization

Pandas (Python Data Analysis Library) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

[More about Pandas](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)

## About Panda Bear

The feature set allows you to work with the annotation of the ribosomal RNA metagenomic dataset in GFF format and with the alignment of the metagenomic assembly to the same dataset in BED 6 format.

OS: Windows 10, 21H2, x64
Python 3.11.0

## About functions

+ `read_gff` - read file in GFF format
+ `read_bed6` - read file in BED format with six column
+ `simple_attribute` - leave only rRNA type data in GFF-file
+ `count_type_of_rna` - creating a table counting each rRNA type by chromosome

The script also contains commands that let you know how much rRNA was successfully assembled during the assembly process.

## About volcano-plot

The script contains commands for visualizing differential gene expression data. This is a special type of graph - volcano plot:

+ On the X-axis it shows the logarithmic fold change - how many times the gene expression has changed
+ The Y-axis shows the significance level of these changes as a negative decimal logarithm of p-value (adjusted for multiple comparisons)

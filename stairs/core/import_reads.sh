cat ../source/minion_BTI_run2.fastq | ./flatten_reads.py | ./filter_reads.py | ./store_reads.py data/reads.dat
